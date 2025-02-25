# main.py

import asyncio
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import HTMLResponse
from models import GameState, Character, Enemy, Spell, Ability
from game import (
    calculate_turn_order, get_entity_by_id, perform_attack,
    enemy_ai, check_victory, check_defeat
)
from utils import save_game, load_game
from uuid import UUID
from typing import Dict
import uuid

app = FastAPI()

# Tracks all games
active_connections: Dict[UUID, WebSocket] = {}

@app.post("/start_game/")
async def start_game(request: Request):
    data = await request.json()
    player_id = data.get('player_id', None)

    if not player_id:
        raise HTTPException(status_code=400, detail=f"Player ID is required. FastAPI received request: {request.json() = }")

    # Initialize game state
    game_state = GameState(
        player_id=player_id,
        characters=[
            Character(
                name="Hero",
                stats={
                    'health': 100,
                    'max_health': 100,
                    'physical_defense': 10,
                    'magical_defense': 5,
                    'mana_points': 50,
                    'ability_points': 30,
                    'attack_damage': 15,
                    'spell_damage': 10,
                    'hit_count': 1,
                    'agility': 0.1,
                    'accuracy': 0.8,
                    'critical_hit_chance': 0.05,
                    'action_speed': 10
                },
                base_stats={
                    'strength': 5,
                    'intelligence': 3,
                    'dexterity': 4,
                    'speed': 2
                },
                owner_id=player_id
            )
        ],
        enemies=[
            Enemy(
                name="Goblin",
                level=1,
                stats={
                    'health': 50,
                    'max_health': 50,
                    'physical_defense': 5,
                    'magical_defense': 2,
                    'mana_points': 20,
                    'ability_points': 10,
                    'attack_damage': 10,
                    'spell_damage': 5,
                    'hit_count': 1,
                    'agility': 0.05,
                    'accuracy': 0.7,
                    'critical_hit_chance': 0.02,
                    'action_speed': 8
                }
            )
        ],
    )
    calculate_turn_order(game_state)
    save_game(game_state)
    return {"game_id": game_state.game_id}

@app.post("/load_game/{game_id}")
async def load_game_endpoint(request: Request):
    data = await request.json()
    game_id: str = data.get("game_id", None)
    game_state = load_game(game_id)
    if not game_state:
        raise HTTPException(status_code=404, detail=f"Game not found. FastAPI received request: {request.json() = }")
    return game_state

@app.post("/action/{game_id}/attack/")
def attack_action(game_id: str, attacker_id: UUID, target_id: UUID):
    game_state = load_game(game_id)
    if not game_state:
        raise HTTPException(status_code=404, detail=f"Game not found: {game_id = }")
    
    attacker = get_entity_by_id(game_state, attacker_id)
    target = get_entity_by_id(game_state, target_id)
    
    if not isinstance(attacker, Character) or not isinstance(target, Enemy):
        raise HTTPException(status_code=400, detail=f"Invalid attacker or target: {attacker_id = }, {target_id = }\n{attacker = }, {target = } - The attacker must be a Character and the target must be an Enemy.")
    
    result = perform_attack(attacker, target, game_state)
    
    # Remove enemy if dead
    if target.stats['health'] <= 0:
        game_state.enemies = [enemy for enemy in game_state.enemies if enemy.id != target.id]
        result['message'] += f" {target.name} has been defeated!"
    
    # Check victory
    if check_victory(game_state):
        save_game(game_state)
        return {"message": result['message'], "status": "victory"}
    
    # Execute enemy turns
    for enemy in game_state.enemies:
        ai_action = enemy_ai(game_state, enemy)
        if ai_action['action'] == 'attack':
            enemy_target = get_entity_by_id(game_state, ai_action['target'].id)
            attack_result = perform_attack(enemy, enemy_target, game_state)
            result['message'] += f" {attack_result['message']}"
            if enemy_target.stats['health'] <= 0:
                game_state.characters = [char for char in game_state.characters if char.id != enemy_target.id]
                result['message'] += f" {enemy_target.name} has been defeated!"
        elif ai_action['action'] == 'cast_spell':
            # Implement spell casting logic
            pass  # Placeholder
        
        # Check defeat
        if check_defeat(game_state):
            save_game(game_state)
            return {"message": result['message'], "status": "defeat"}
    
    calculate_turn_order(game_state)
    save_game(game_state)
    return {"message": result['message'], "status": game_state.status}

# main.py (FastAPI WebSocket handler)
# Update the websocket_endpoint to send game state updates
@app.websocket("/ws/{game_id}")
async def websocket_endpoint(websocket: WebSocket, game_id: str):
    await websocket.accept()
    try:
        while True:
            # Send the current game state periodically or on changes
            game_state = load_game(game_id)
            if game_state:
                await websocket.send_json(game_state.dict())
            await asyncio.sleep(1)  # Adjust the interval as needed
    except WebSocketDisconnect:
        print(f"WebSocket disconnected for game {game_id}")

# You can add more endpoints for different actions like defend, skip, cast_spell, etc.