from typing import Optional
import json
from models import GameState
import os

GAMES_DIR = 'games'

def save_game(game_state: GameState):
    if not os.path.exists(GAMES_DIR):
        os.makedirs(GAMES_DIR)
    with open(f"{GAMES_DIR}/{game_state.game_id}.json", 'w') as f:
        json.dump(game_state.dict(), f, default=str, indent=4)

def load_game(game_id: str) -> Optional[GameState]:
    try:
        with open(f"{GAMES_DIR}/{game_id}.json", 'r') as f:
            data = json.load(f)
            return GameState(**data)
    except FileNotFoundError:
        return None