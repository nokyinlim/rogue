# main.py

import asyncio
from fastapi import FastAPI, Query, Request, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.params import Body
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from models import GameState, Character, Enemy, Spell, Ability
from game import (
    calculate_turn_order, cast_spell, get_entity_by_id, perform_attack,
    enemy_ai, check_victory, check_defeat, process_turn, update_game_state,
    execute_turn, process_enemy_turns, generate_random_numbers, use_ability
)

from abilities import get_ability
from spells import get_spell
from utils import save_game, load_game, serialize_game_state
from uuid import UUID, uuid4
from typing import Dict, Optional

from constants import *

from enemies import generate_wave_enemies
from characters import hero

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tracks all games
active_connections: Dict[UUID, WebSocket] = {}

@app.post("/start_game/")
def start_game(player_id: UUID = Query(...)):

    print(f"Start New Game: {player_id = }")
    if not player_id:
        raise HTTPException(status_code=400, detail=f"Player ID is required. FastAPI received request")

    # Initialize game state
    game_state = GameState(
        player_id=player_id,
        characters=[
            hero(1, owner_id=uuid4())
        ],
        enemies=generate_wave_enemies(1)
        ,
    )
    calculate_turn_order(game_state)
    save_game(game_state)
    return {"game_id": game_state.game_id, 'player_id': player_id}

@app.post("/load_game/")
async def load_game_endpoint(game_id: str = Query(...)):
    print(f"Load Game: {game_id = }")
    if not game_id:
        raise HTTPException(status_code=400, detail=f"Game ID is required, but none was provided.")
    game_state = load_game(game_id)
    if not game_state:
        raise HTTPException(status_code=404, detail=f"Game not found. {game_id = }")
    return game_state

@app.post('/get_end_wave_heal/')
async def get_end_wave_heal(game_id: str = Query(...)):
    game_state = load_game(game_id)
    multiplier = BASE_WAVE_REWARD_STRENGTH + WAVE_REWARD_STRENGTH_SCALING * game_state.wave

    options = []

    for _ in range(3):
        distribution = generate_random_numbers()

        healing = LEVEL_HEAL_HEALTH_MULTIPLIER + LEVEL_HEAL_HEALTH_SCALING * game_state.wave
        mana_regen = LEVEL_HEAL_MANA_MULTIPLIER + LEVEL_HEAL_MANA_SCALING * game_state.wave
        ability_regen = LEVEL_HEAL_ABILITY_MULTIPLIER + LEVEL_HEAL_ABILITY_SCALING * game_state.wave

        options.append({
            'health': healing * distribution[0],
            'mana_points': mana_regen * distribution[1],
            'ability_points': ability_regen * distribution[2],
            'health_distribution': distribution[0],
            'mana_distribution': distribution[1],
            'ability_distribution': distribution[2]
        })
    
    print(options)
    
    return options

@app.post('/apply_end_wave_heal/')
async def apply_end_wave_heal(game_id: str = Query(...), heal_option: Dict[str, float] = Body(...)):
    game_state = load_game(game_id)

    for i in range(len(game_state.characters)):
        game_state.characters[i].stats['health'] += int(heal_option['health'])
        game_state.characters[i].stats['mana_points'] += int(heal_option['mana_points'])
        game_state.characters[i].stats['ability_points'] += int(heal_option['ability_points'])
        game_state.characters[i].stats['health'] = min(game_state.characters[i].stats['health'], game_state.characters[i].stats['max_health'])
        game_state.characters[i].stats['mana_points'] = min(game_state.characters[i].stats['mana_points'], game_state.characters[i].stats['max_mana_points'])
        game_state.characters[i].stats['ability_points'] = min(game_state.characters[i].stats['ability_points'], game_state.characters[i].stats['max_ability_points'])
    
    save_game(game_state)

@app.post('/level_rewards/')
async def level_rewards(game_id: str = Query(...)):
    print(f"Level Rewards: {game_id = }")
    game_state = load_game(game_id)
    if not game_state:
        raise HTTPException(status_code=404, detail=f"Game not found. {game_id = }")
    
    print(f"Current Level: {game_state.wave}")
    # Get the new rewards that are going to be for the next level
    for i in range(len(game_state.characters)):
        level = game_state.characters[i].level


        pass

    save_game(game_state)

@app.post('/next_wave/')
async def next_wave(game_id: str = Query(...)):
    print(f"Next Wave: {game_id = }")
    game_state = load_game(game_id)
    game_state.wave += 1
    if not game_state:
        raise HTTPException(status_code=404, detail=f"Game not found. {game_id = }")
    
    # Get the new enemies that are going to be for the next wave

    new_enemies = generate_wave_enemies(game_state.wave)

    game_state.enemies = new_enemies
    save_game(game_state)
    print("Next Wave: Enemies spawned")
    return {"message": "Enemy wave spawned", "status": "success"}


@app.get("/get_status/")
async def get_victory(game_id: str):
    game_state = load_game(game_id)
    if not game_state:
        raise HTTPException(status_code=404, detail=f"Game not found. {game_id = }")
    return game_state.status

@app.post("/action/enemy/")
def execute_enemy_turn(game_id: str = Query(...)):
    game_state = load_game(game_id)
    if not game_state:
        raise HTTPException(status_code=404, detail=f"Game not found: {game_id = }")
    
    messages = []
    print(f"[Debug] Processing enemy turn")
    print(f"{game_state.status = }")
    # Process only the next enemy's turn
    if game_state.status == "waiting":
        print(game_state.characters)
        print(f"{game_state.current_turn = }")
        print(f"{game_state.turn_order = }")
        print(f"{game_state.current_turn = }")
        print(f"{game_state.turn_order[game_state.current_turn] = }")
        print(f"{game_state.turn_order = }")
        print(f"Upcoming: {game_state.turn_order[game_state.current_turn]}")
        enemy = get_entity_by_id(game_state, game_state.turn_order[game_state.current_turn])
        print(f"[Debug] Processing {enemy.name}'s turn")

        print(f"[Debug] Processing enemy turns")
        enemy_result = process_enemy_turns(game_state, game_state.turn_order[game_state.current_turn])
        messages.append(enemy_result['message'])
        game_state = enemy_result['game_state']
        print(f"[Debug] Enemy's turn - {game_state.turn_order[game_state.current_turn]}")
        process_turn(game_state)
    



@app.post("/action/attack/")
def attack_action(game_id: str = Query(...), attacker_id: UUID = Query(...), target_id: UUID = Query(...)):
    # for debug, log the names
    print(f"Attack Action: {game_id = }, {attacker_id = }, {target_id = }")
    
    

    game_state = load_game(game_id)
    if not game_state:
        print(f"Game not found: {game_id = }")
        raise HTTPException(status_code=404, detail=f"Game not found: {game_id = }")
    
    # Verify it's the attacker's turn
    current_entity_id = game_state.turn_order[game_state.current_turn]
    if current_entity_id != attacker_id:
        print(f"Not {attacker_id}'s turn. Current turn: {current_entity_id}")
        raise HTTPException(
            status_code=400, 
            detail=f"Not {attacker_id}'s turn. Current turn: {current_entity_id}"
        )
    
    attacker = get_entity_by_id(game_state, attacker_id)
    target = get_entity_by_id(game_state, target_id)
    
    if not isinstance(attacker, Character) or not isinstance(target, Enemy):
        raise HTTPException(status_code=400, detail="Invalid attacker or target")
    
    # Execute attack and process turn
    attack_result = perform_attack(attacker, target, game_state)
    result = execute_turn(game_state, attack_result)
    
    # Save final state
    save_game(result['game_state'])
    return {"message": result['message'], "status": result['status']}

@app.post("/action/defend/")
def defend_action(game_id: str = Query(...), character_id: UUID = Query(...)):
    game_state = load_game(game_id)
    if not game_state:
        raise HTTPException(status_code=404, detail=f"Game not found: {game_id = }")
    
    # Verify it's the character's turn
    current_entity_id = game_state.turn_order[game_state.current_turn]
    if current_entity_id != character_id:
        raise HTTPException(
            status_code=400,
            detail=f"Not {character_id}'s turn. Current turn: {current_entity_id}"
        )
    
    character = get_entity_by_id(game_state, character_id)
    if not isinstance(character, Character):
        raise HTTPException(status_code=400, detail="Only player characters can defend")
    
    # Execute defend and process turn
    character.is_defending = True
    defend_result = {
        'message': f"{character.name} is defending",
        'status': 'success',
        'game_state': game_state
    }
    result = execute_turn(game_state, defend_result)
    
    # Save final state
    save_game(result['game_state'])
    return {"message": result['message'], "status": result['status']}


@app.post('/action/enemy_turn/')
def enemy_turn(game_id: str = Query(...)):
    """
    This function takes in a game ID and will perform exactly one enemy turn ahead of it.
    ### Parameters
    - game_id: str > The ID of the game to perform the enemy turn in.

    ### Returns: Dict[str, Any]
    - message: List[str] > the list of messages to be displayed to the player
    - status: str > status of whether the turn was successful or not. "success" if True
    """

    ret_json = {
        "status": "success"
    }

    print(f"[Debug] Checking for an Enemy Turn.")
    game_state = load_game(game_id)
    if not game_state:
        raise HTTPException(status_code=404, detail=f"Game not found: {game_id = }")
    
    messages = []

    # Process only the next enemy's turn

    if game_state.status == "waiting":
        enemy_id = game_state.turn_order[game_state.current_turn]

        enemy = get_entity_by_id(game_state, enemy_id)
    else:
        ret_json["status"] = "failed"
        return ret_json
    
    print(f"[Debug] Processing {enemy.name}'s turn")

    enemy_result = process_enemy_turns(game_state, enemy_id)

    messages.extend(enemy_result['message'])
    game_state = enemy_result["game_state"]

    state = process_turn(game_state)

    save_game(state)

    ret_json["message"] = messages
    print("Logging Enemy Turn")
    [print(f"[Debug] {msg}") for msg in messages]

    return ret_json




@app.post("/action/spell/")
def spell_action(
    game_id: str = Query(...), 
    caster_id: UUID = Query(...), 
    spell_name: str = Query(...),
    spell_level: int = Query(1),
    target_id: Optional[UUID] = Query(None)
):
    print(f"Spell Action: {game_id=}, {caster_id=}, {spell_name=}, {target_id=}")
    
    game_state = load_game(game_id)
    if not game_state:
        print(f"Game not found: {game_id=}")
        raise HTTPException(status_code=404, detail=f"Game not found: {game_id=}")
    
    # Verify it's the caster's turn
    current_entity_id = game_state.turn_order[game_state.current_turn]
    if current_entity_id != caster_id:
        print(f"Not {caster_id}'s turn. Current turn: {current_entity_id}")
        raise HTTPException(
            status_code=400, 
            detail=f"Not {caster_id}'s turn. Current turn: {current_entity_id}"
        )
    
    caster = get_entity_by_id(game_state, caster_id)
    if not caster:
        raise HTTPException(status_code=400, detail="Caster not found")
    
    # Find the spell by name
    if isinstance(caster, Character):
        spell = get_spell(spell_name, spell_level)
    elif isinstance(caster, Enemy):
        spell = next((s for s in caster.spells if s.name == spell_name), None)
    else:
        raise HTTPException(status_code=400, detail="Invalid caster type")
    
    if not spell:
        raise HTTPException(status_code=400, detail=f"Spell '{spell_name}' not found")
    
    # Handle target based on spell target_type
    target = None
    if spell.target_type == "single":
        if not target_id:
            raise HTTPException(status_code=400, detail="Target ID required for single target spells")
        target = get_entity_by_id(game_state, target_id)
        if not target:
            raise HTTPException(status_code=400, detail="Target not found")
    elif spell.target_type == "self":
        target = caster
    elif spell.target_type == "all_enemies":
        # Target selection handled in cast_spell
        pass
    elif spell.target_type == "all_allies":
        # Target selection handled in cast_spell
        pass
    
    # Execute the spell and process turn
    spell_result = cast_spell(caster, spell, target, game_state)
    if not spell_result["success"]:
        raise HTTPException(status_code=400, detail=spell_result["message"])
        
    result = execute_turn(game_state, spell_result)
    
    # Save final state
    save_game(result['game_state'])
    return {"message": result['message'], "status": result['status']}


@app.post("/get_castables/")
def get_actions(game_id: str = Query(...), entity_id: UUID = Query(...)):
    # This returns all abilities and spells
    game_state = load_game(game_id)
    if not game_state:
        raise HTTPException(status_code=404, detail=f"Game not found: {game_id = }")
    
    entity: Character | Enemy = get_entity_by_id(game_state, entity_id)
    if not entity:
        raise HTTPException(status_code=400, detail="Entity not found")

    spells = []
    abilities = []

    if isinstance(entity, Enemy):
        spells = entity.spells
        abilities = entity.abilities
    elif isinstance(entity, Character):
        
        for spellName, spellLevel in entity.spells:
            spells.append(get_spell(spellName, spellLevel))

        for abilityName, abilityLevel in entity.abilities:
            abilities.append(get_ability(abilityName, abilityLevel))
    
    
    return {"spells": spells, "abilities": abilities}


@app.post("/action/ability/")
def ability_action(
    game_id: str = Query(...), 
    user_id: UUID = Query(...), 
    ability_name: str = Query(...),
    target_id: Optional[UUID] = Query(None)
):
    print(f"Ability Action: {game_id=}, {user_id=}, {ability_name=}, {target_id=}")
    
    game_state = load_game(game_id)
    if not game_state:
        print(f"Game not found: {game_id=}")
        raise HTTPException(status_code=404, detail=f"Game not found: {game_id=}")
    
    # Verify it's the user's turn
    current_entity_id = game_state.turn_order[game_state.current_turn]
    if current_entity_id != user_id:
        print(f"Not {user_id}'s turn. Current turn: {current_entity_id}")
        raise HTTPException(
            status_code=400, 
            detail=f"Not {user_id}'s turn. Current turn: {current_entity_id}"
        )
    
    user = get_entity_by_id(game_state, user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    
    # Find the ability by name
    ability = None
    if isinstance(user, Character) and hasattr(user, 'abilities'):
        ability = next((a for a in user.abilities if a.name == ability_name), None)
    elif isinstance(user, Enemy) and hasattr(user, 'abilities'):
        ability = next((a for a in user.abilities if a.name == ability_name), None)
    
    if not ability:
        raise HTTPException(status_code=400, detail=f"Ability '{ability_name}' not found")
    
    # Handle target based on ability target_type
    target = None
    if ability.target_type == "single":
        if not target_id:
            raise HTTPException(status_code=400, detail="Target ID required for single target abilities")
        target = get_entity_by_id(game_state, target_id)
        if not target:
            raise HTTPException(status_code=400, detail="Target not found")
    elif ability.target_type == "self":
        target = user
    elif ability.target_type == "all_enemies":
        # Target selection handled in use_ability
        pass
    elif ability.target_type == "all_allies":
        # Target selection handled in use_ability
        pass
    
    # Execute the ability and process turn
    ability_result = use_ability(user, ability, target, game_state)
    if not ability_result["success"]:
        raise HTTPException(status_code=400, detail=ability_result["message"])
        
    result = execute_turn(game_state, ability_result)
    
    # Save final state
    save_game(result['game_state'])
    return {"message": result['message'], "status": result['status']}


@app.post('/action/skip/')
def skip_turn(game_id: str = Query(...), player_id: str = Query(...)):
    print("A Character is Skipping Their Turn")
    


# main.py (FastAPI WebSocket handler)
# Update the websocket_endpoint to send game state updates
@app.websocket("/ws/{game_id}")
async def websocket_endpoint(websocket: WebSocket, game_id: str):
    await websocket.accept()
    try:
        while True:
            game_state = load_game(game_id)
            if game_state:
                # Always ensure game state is up to date before sending
                game_state = update_game_state(game_state)
                save_game(game_state)
                # Use the new serialization function
                await websocket.send_json({
                    "event": "game_state_update",
                    "message": ""
                })
    except WebSocketDisconnect:
        print(f"WebSocket disconnected for game {game_id}")

# skip, ability endpoints not created



