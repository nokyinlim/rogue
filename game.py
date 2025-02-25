from models import GameState, Character, Enemy, Spell, Ability, Effect, StatusEffect
from typing import Dict, Optional, Union, List
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

def perform_attack(attacker: Character, target: Character, game_state: GameState) -> Dict[str, List[str]]:
    messages: List[str] = []

    damage = attacker.stats['attack_damage']
    for _ in range(attacker.stats['hit_count']):
        if attacker.stats['accuracy'] < random.random():
            messages.append(f"{attacker.name}'s attack missed!")
            continue
        if target.stats['agility'] > random.random():
            messages.append(f"{target.name} dodged an attack!")
            continue
        actual_damage = max(0, damage - target.stats['physical_defense'])
        target.stats['health'] -= actual_damage
    messages.append(f"{attacker.name} attacks {target.name} for {actual_damage} damage!")
    return {"message": messages}

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

def apply_effect(source: Union[Character, Enemy], target: Union[Character, Enemy], effect: Effect, game_state: GameState):
    """Apply a single effect to target"""
    message = ""
    
    if effect.type == 'damage':
        # Calculate damage
        base_damage = effect.value
        if hasattr(source, 'stats'):
            base_damage += source.stats['spell_damage']
        
        # Apply magical defense
        defense = target.stats['magical_defense']
        damage_reduction = defense / (defense + 50)
        actual_damage = max(1, base_damage * (1 - damage_reduction))
        
        # Apply defending reduction
        if target.is_defending:
            actual_damage *= 0.5
        
        # Apply damage
        target.stats['health'] -= int(actual_damage)
        target.stats['health'] = max(0, target.stats['health'])
        message = f"Deals {int(actual_damage)} damage to {target.name}."
    
    elif effect.type == 'heal':
        healing = effect.value
        if hasattr(source, 'stats'):
            healing += source.stats['spell_damage'] * 0.5
        
        target.stats['health'] += int(healing)
        target.stats['health'] = min(target.stats['health'], target.stats['max_health'])
        message = f"Heals {target.name} for {int(healing)} health."
    
    elif effect.type in ['buff', 'debuff']:
        status = StatusEffect(
            name=f"{effect.type.capitalize()} {effect.target_stat}",
            effect=effect,
            source_id=source.id,
            remaining_turns=effect.duration
        )
        target.status_effects.append(status)
        
        value_text = f"{effect.value}%" if effect.is_percentage else str(effect.value)
        message = f"Applies {effect.type} to {target.name}'s {effect.target_stat}: {value_text} for {effect.duration} turns."
    
    elif effect.type in ['dot', 'hot']:
        status = StatusEffect(
            name="Continuous Damage over Time" if effect.type == 'dot' else "Continuus Healing over Time",
            effect=effect,
            source_id=source.id,
            remaining_turns=effect.duration
        )
        target.status_effects.append(status)
        message = f"Applies {effect.type.upper()} to {target.name}: {effect.value} per turn for {effect.duration} turns."
    
    return {"message": message}

def process_status_effects(entity: Character | Enemy, game_state: GameState):
    """Process all active status effects on an entity"""
    messages = []
    
    for status_idx in range(len(entity.status_effects) - 1, -1, -1):
        status = entity.status_effects[status_idx]
        
        if status.effect.type == 'dot':
            damage = status.effect.value
            entity.stats['health'] -= int(damage)
            entity.stats['health'] = max(0, entity.stats['health'])
            messages.append(f"{entity.name} takes {int(damage)} damage from DoT.")
        
        elif status.effect.type == 'hot':
            healing = status.effect.value
            entity.stats['health'] += int(healing)
            entity.stats['health'] = min(entity.stats['health'], entity.stats['max_health'])
            messages.append(f"{entity.name} heals for {int(healing)} from HoT.")
        
        status.remaining_turns -= 1
        if status.remaining_turns <= 0:
            entity.status_effects.pop(status_idx)
            messages.append(f"{status.name} on {entity.name} has expired.")
    
    return {"message": " ".join(messages)}

def cast_spell(caster: Union[Character, Enemy], spell: Spell, target: Union[Character, Enemy, List[Union[Character, Enemy]]], game_state: GameState):
    """Cast a spell on target(s)"""
    if caster.stats['mana_points'] < spell.cost:
        return {"message": f"Not enough mana to cast {spell.name}.", "success": False}
    
    if spell.current_cooldown > 0:
        return {"message": f"{spell.name} is on cooldown.", "success": False}
    
    caster.stats['mana_points'] -= spell.cost
    spell.current_cooldown = spell.cooldown
    
    results = []
    targets = [target] if not isinstance(target, list) else target
    
    for current_target in targets:
        for effect in spell.effects:
            result = apply_effect(caster, current_target, effect, game_state)
            results.append(result["message"])
    
    return {"message": f"{caster.name} casts {spell.name}. " + " ".join(results), "success": True}

def use_ability(user: Union[Character, Enemy], ability: Ability, target: Union[Character, Enemy, List[Union[Character, Enemy]]], game_state: GameState):
    """Use an ability on target(s)"""
    if user.stats['ability_points'] < ability.cost:
        return {"message": f"Not enough ability points to use {ability.name}.", "success": False}
    
    if ability.current_cooldown > 0:
        return {"message": f"{ability.name} is on cooldown.", "success": False}
    
    user.stats['ability_points'] -= ability.cost
    ability.current_cooldown = ability.cooldown
    
    results = []
    targets = [target] if not isinstance(target, list) else target
    
    for current_target in targets:
        if ability.type == 'damage':
            accuracy = user.stats['accuracy'] + ability.accuracy_bonus
            if random.random() > accuracy:
                results.append(f"{ability.name} missed {current_target.name}!")
                continue
        
        for effect in ability.effects:
            result = apply_effect(user, current_target, effect, game_state)
            results.append(result["message"])
    
    return {"message": f"{user.name} uses {ability.name}. " + " ".join(results), "success": True}

def process_turn(game_state: GameState):
    """Process end of turn effects"""
    current_entity_id = game_state.turn_order[game_state.current_turn]
    entity = get_entity_by_id(game_state, current_entity_id)
    
    if entity:
        process_status_effects(entity, game_state)
        
        # Reduce cooldowns
        if hasattr(entity, 'spells'):
            for spell in entity.spells:
                if spell.current_cooldown > 0:
                    spell.current_cooldown -= 1
        
        if hasattr(entity, 'abilities'):
            for ability in entity.abilities:
                if ability.current_cooldown > 0:
                    ability.current_cooldown -= 1
    
    game_state.current_turn = (game_state.current_turn + 1) % len(game_state.turn_order)
    
    # Reset statuses at round end
    if game_state.current_turn == 0:
        for entity in game_state.characters + game_state.enemies:
            entity.is_defending = False
            entity.is_vulnerable = False
    
    return game_state

# Add more game logic functions as needed