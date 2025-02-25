from models import GameState, Character, Enemy, Spell, Ability
from typing import Optional
from uuid import UUID
import random

def calculate_turn_order(game_state: GameState):
    all_entities = game_state.characters + game_state.enemies
    sorted_entities = sorted(
        all_entities,
        key=lambda entity: entity.stats.get('action_speed', 0),
        reverse=True
    )
    game_state.turn_order = [entity.id for entity in sorted_entities]

def get_entity_by_id(game_state: GameState, entity_id: UUID):
    for character in game_state.characters:
        if character.id == entity_id:
            return character
    for enemy in game_state.enemies:
        if enemy.id == entity_id:
            return enemy
    return None

def perform_attack(attacker: Character, target: Character, game_state: GameState):
    if attacker.stats['accuracy'] < random.random():
        return {"message": f"{attacker.name}'s attack missed!"}
    
    damage = attacker.stats['attack_damage']
    for _ in range(attacker.stats['hit_count']):
        if target.stats['agility'] > random.random():
            return {"message": f"{target.name} evaded the attack!"}
        actual_damage = max(0, damage - target.stats['physical_defense'])
        target.stats['health'] -= actual_damage
    return {"message": f"{attacker.name} attacked {target.name} for {damage} damage."}

def enemy_ai(game_state: GameState, enemy: Enemy):
    # Simple AI: If enemy has heal spell and a party member is below 50% health, heal
    low_health_chars = [char for char in game_state.characters if char.stats['health'] < (char.stats['max_health'] / 2)]
    if enemy.spells:
        heal_spells = [spell for spell in enemy.spells if spell.type == 'heal']
        if heal_spells and low_health_chars:
            spell = random.choice(heal_spells)
            target = random.choice(low_health_chars)
            # Implement spell casting (not detailed here)
            return {"action": "cast_spell", "spell": spell, "target": target}
    # Otherwise, perform a basic attack
    target = random.choice(game_state.characters)
    return {"action": "attack", "target": target}

def check_victory(game_state: GameState):
    if not game_state.enemies:
        game_state.status = "victory"
        return True
    return False

def check_defeat(game_state: GameState):
    if not game_state.characters:
        game_state.status = "defeat"
        return True
    return False

# Add more game logic functions as needed