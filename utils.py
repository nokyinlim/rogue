from typing import Optional, Any
import json
from models import GameState
import os
from uuid import UUID
from time import time
import threading

GAMES_DIR = 'games'

class Scheduler:
    def __init__(self):
        self.fns = [] # tuple of (fn, time)

        # The lock prevents 2 threads from messing with fns at the same time;
        # also lets us use Condition
        self.lock = threading.RLock()

        # The condition lets one thread wait, optionally with a timeout,
        # and lets other threads wake it up
        self.condition = threading.Condition(self.lock)

        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000

            with self.lock:
                # Prevent the other thread from adding to fns while we're sorting
                # out the jobs to run now, and the jobs to keep for later

                to_run = [fn for fn, due in self.fns if due <= now]
                self.fns = [(fn, due) for (fn, due) in self.fns if due > now]

            # Run all the ready jobs outside the lock, so we don't keep it
            # locked longer than we have to
            for fn in to_run:
                fn()

            with self.lock:
                if not self.fns:
                    # If there are no more jobs, wait forever until a new job is 
                    # added in delay(), and notify_all() wakes us up again
                    self.condition.wait()
                else:
                    # Wait only until the soonest next job's due time.
                    ms_remaining = min(due for fn, due in self.fns) - time()*1000
                    if ms_remaining > 0:
                        self.condition.wait(ms_remaining / 1000)

    def delay(self, f, n):
        with self.lock:
            self.fns.append((f, time() * 1000 + n))

            # If the scheduler thread is currently waiting on the condition,
            # notify_all() will wake it up, so that it can consider the new job's
            # due time.
            self.condition.notify_all()

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, UUID):
            return str(obj)
        return super().default(obj)

def save_game(game_state: GameState):
    if not os.path.exists(GAMES_DIR):
        os.makedirs(GAMES_DIR)
    with open(f"{GAMES_DIR}/{game_state.game_id}.json", 'w') as f:
        json.dump(game_state.dict(), f, cls=UUIDEncoder, indent=4)

def load_game(game_id: str) -> Optional[GameState]:
    try:
        with open(f"{GAMES_DIR}/{game_id}.json", 'r') as f:
            data = json.load(f)
            # Convert string UUIDs back to UUID objects
            if 'game_id' in data:
                data['game_id'] = UUID(data['game_id'])
            if 'player_id' in data:
                data['player_id'] = UUID(data['player_id'])
            return GameState(**data)
    except FileNotFoundError:
        return None

def serialize_game_state(game_state: GameState) -> dict:
    """Serialize game state to JSON-compatible dict"""
    data = game_state.dict()
    return json.loads(json.dumps(data, cls=UUIDEncoder))