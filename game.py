from models import GameState, Character, Enemy, Spell, Ability, Effect, StatusEffect
from typing import Any, Dict, Optional, Union, List
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

def perform_attack(attacker: Character | Enemy, target: Character | Enemy, game_state: GameState) -> Dict[str, List[str]]:
    messages: List[str] = []

    print(f"[Debug] {attacker.name} attacks {target.name}")

    true_accuracy = attacker.stats['accuracy'] - target.stats['agility']
    damage = attacker.stats['attack_damage']
    total_damage = 0
    for i, _ in enumerate(range(int(attacker.stats['hit_count']))):
        
        if true_accuracy < random.random():
            messages.append(f"{attacker.name}'s Attack {i} missed!")
            continue
        actual_damage = max(0, damage - target.stats['physical_defense'])
        target.stats['health'] -= actual_damage
        messages.append(f"{attacker.name}'s Attack {i} hit the target.")
        total_damage += actual_damage
        print(f"[Debug] Attack {i}: {actual_damage} damage")
    messages.append(f"{attacker.name} attacks {target.name} for {total_damage} damage!")
    print(f"[Debug] {total_damage = }, {target.stats['health'] = }")
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

    for enemy in game_state.enemies:
        if enemy.stats['health'] > 0:
            return False
    game_state.status = "victory"
    return True

def check_defeat(game_state: GameState):
    for character in game_state.characters:
        if character.stats['health'] > 0:
            return False
    game_state.status = "defeat"
    return True
    

def apply_effect(source: Union[Character, Enemy], target: Union[Character, Enemy], effect: Effect, game_state: GameState) -> List[str]:
    """Apply a single effect to target"""
    message: List[str] = []
    # statuses: List[Dict[str, any]] = []
    
    if 'damage' in effect.type:
        # Calculate damage
        base_damage = effect.value
        if hasattr(source, 'stats'):
            base_damage += source.stats['spell_damage']
        
        # Apply magical defense
        defense = target.stats['magical_defense']
        damage_reduction = defense / (defense + 50)
        actual_damage = max(1, base_damage * (1 - damage_reduction))
        
        # Apply defending reduction (*0.3)
        if target.is_defending:
            from constants import DEFENDING_DAMAGE_MULTIPLIER
            actual_damage *= DEFENDING_DAMAGE_MULTIPLIER

        if isinstance(target, Enemy) and target.is_undead:
            from constants import UNDEAD_DAMAGE_MULTIPLIER
            mult = 1 if 'undead' in effect.type else UNDEAD_DAMAGE_MULTIPLIER
            print("Undead-Slayer") if 'undead' in effect.type else print("Undead Target! Damage is reduced!")
            actual_damage *= mult
            message.append("Undead-Slayer") if 'undead' in effect.type else message.append("Undead")
        
        # Apply damage
        target.stats['health'] -= int(actual_damage)
        target.stats['health'] = max(0, target.stats['health'])
        message.append(f"Deals {int(actual_damage)} damage to {target.name}!")
    
    elif 'heal' in effect.type:
        healing = effect.value
        if hasattr(source, 'stats'):
            healing += source.stats['spell_damage'] * 0.5
        
        target.stats['health'] += int(healing)
        target.stats['health'] = min(target.stats['health'], target.stats['max_health'])
        message = f"Healed {target.name} for {int(healing)} health."
    
    elif 'buff' in effect.type or 'debuff' in effect.type:
        status = StatusEffect(
            name=f"{effect.type.capitalize()} {effect.target_stat}",
            effect=effect,
            source_id=source.id,
            remaining_turns=effect.duration
        )
        target.status_effects.append(status)
        
        value_text = f"{effect.value}%" if effect.is_percentage else str(effect.value)
        message = f"Applies {effect.type} to {target.name}'s {effect.target_stat}: {value_text} for {effect.duration} turns."
    
    elif 'dot' in effect.type or 'hot' in effect.type:
        status = StatusEffect(
            name="Continuous Damage over Time" if effect.type == 'dot' else "Continuus Healing over Time",
            effect=effect,
            source_id=source.id,
            remaining_turns=effect.duration
        )
        target.status_effects.append(status)
        message = f"Applies {effect.type.upper()} to {target.name}: {effect.value} per turn for {effect.duration} turns."
    
    return {"message": message}

def get_stat(entity: Character | Enemy, stat: str):
    """Get a stat value from an entity, including status effects"""
    total = entity.stats.get(stat, 0)

    for status_idx in range(len(entity.status_effects) - 1, -1, -1):
        status = entity.status_effects[status_idx]
        
        # Check that effect is not a percentage
        if status.effect.is_percentage:
            continue

        if 'debuff' in status.effect.type or 'buff' in status.effect.type:
            value = status.effect.value
            if status.effect.target_stat == stat:
                total += value
            



    # Repeat for percentage-based
    for status_idx in range(len(entity.status_effects) - 1, -1, -1):
        status = entity.status_effects[status_idx]
        
        # Check that effect is a percentage
        if not status.effect.is_percentage:
            continue

        if 'debuff' in status.effect.type or 'buff' in status.effect.type:
            value = status.effect.value * total
            if status.effect.target_stat == stat:
                total += value
    
def generate_random_numbers(seed: Any = 'game') -> List[float]:
    while True:
        random.seed(seed)  # Set a seed for reproducibility
        numbers = sorted([random.random() for _ in range(2)])
        numbers.append(1 - sum(numbers))
        if len(set(numbers)) == 3 and 0 <= max(numbers) - min(numbers) <= 0.9:
            return numbers

def process_status_effects(entity: Character | Enemy, game_state: GameState):
    """Process all active status effects on an entity"""
    messages = []

    print(f"[Debug] Processing status effects for {entity.name}")
    
    # goes from last to first
    for status_idx in range(len(entity.status_effects) - 1, -1, -1):
        status = entity.status_effects[status_idx]
        
        # Check that effect is not a percentage
        if status.effect.is_percentage:
            continue

        if status.effect.type == 'dot':
            damage = status.effect.value
            entity.stats['health'] -= int(damage)
            entity.stats['health'] = max(0, entity.stats['health'])
            messages.append(f"{entity.name} takes {int(damage)} damage from DoT.")
            print(f"[Debug] {entity.name} takes {int(damage)} damage from DoT.")
        
        elif status.effect.type == 'hot':
            healing = status.effect.value
            entity.stats['health'] += int(healing)
            entity.stats['health'] = min(entity.stats['health'], entity.stats['max_health'])
            messages.append(f"{entity.name} heals for {int(healing)} from HoT.")
            print(f"[Debug] {entity.name} heals for {int(healing)} from HoT.")
        
        status.remaining_turns -= 1
        if status.remaining_turns <= 0:
            entity.status_effects.pop(status_idx)
            messages.append(f"{status.name} on {entity.name} has expired.")
            print(f"[Debug] {status.name} on {entity.name} has expired.")

    # Repeat for percentage-based
    for status_idx in range(len(entity.status_effects) - 1, -1, -1):
        status = entity.status_effects[status_idx]
        
        # Check that effect is not a percentage
        if not status.effect.is_percentage:
            continue

        if status.effect.type == 'dot':
            damage = status.effect.value * entity.stats['max_health']
            entity.stats['health'] -= int(damage)
            entity.stats['health'] = max(0, entity.stats['health'])
            messages.append(f"{entity.name} takes {int(damage)} damage from DoT.")
            print(f"[Debug] {entity.name} takes {int(damage)} damage from DoT.")
        
        elif status.effect.type == 'hot':
            healing = status.effect.value * entity.stats['max_health']
            entity.stats['health'] += int(healing)
            entity.stats['health'] = min(entity.stats['health'], entity.stats['max_health'])
            messages.append(f"{entity.name} heals for {int(healing)} from HoT.")
            print(f"[Debug] {entity.name} heals for {int(healing)} from HoT.")
        
        status.remaining_turns -= 1
        if status.remaining_turns <= 0:
            entity.status_effects.pop(status_idx)
            messages.append(f"{status.name} on {entity.name} has expired.")
            print(f"[Debug] {status.name} on {entity.name} has expired.")
    
    return {"message": messages}




def cast_spell(caster: Union[Character, Enemy], spell: Spell, target: Optional[Union[Character, Enemy, List[Union[Character, Enemy]]]], game_state: GameState):
    """
    Cast a spell on target(s)
    ### Parameters
    - caster: Character or Enemy casting the spell
    - spell: Spell to cast
    - target [Optional]: Character, Enemy, or List of Characters/Enemies to target
    ### Returns
    - message: String message describing the result of the spell cast
    - success: Boolean indicating if the spell was successfully
    """

    print(f"[Debug] {caster.name} casts {spell.name} of type {spell.type}")
    if caster.stats['mana_points'] < spell.cost:
        return {"message": f"Not enough mana to cast {spell.name}.", "success": False}
    
    if spell.current_cooldown > 0:
        return {"message": f"{spell.name} is on cooldown.", "success": False}
    
    caster.stats['mana_points'] -= spell.cost
    spell.current_cooldown = spell.cooldown
    
    # Determine targets based on spell.target_type
    targets = []
    
    if spell.target_type == "single":
        if target is None:
            return {"message": "Target required for single-target spell", "success": False}
        targets = [target]
    elif spell.target_type == "self":
        targets = [caster]
    elif spell.target_type == "all_enemies":
        # Target all entities from the opposing team
        is_character = isinstance(caster, Character)
        targets = game_state.enemies if is_character else game_state.characters
        targets = [e for e in targets if e.stats['health'] > 0]  # Only target living entities
    elif spell.target_type == "all_allies":
        # Target all entities from the same team
        is_character = isinstance(caster, Character)
        targets = game_state.characters if is_character else game_state.enemies
        targets = [e for e in targets if e.stats['health'] > 0]  # Only target living entities
    
    results = []
    for current_target in targets:
        target_results = []
        for effect in spell.effects:
            result = apply_effect(caster, current_target, effect, game_state)
            target_results.append(result["message"])
        results.append(f"{' '.join(target_results)}")
    
    message = f"{caster.name} casts {spell.name}. {' '.join(results)}"
    return {"message": message, "success": True}

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
                if not isinstance(spell, Spell):
                    continue
                if spell.current_cooldown > 0:
                    spell.current_cooldown -= 1
        
        if hasattr(entity, 'abilities'):
            for ability in entity.abilities:
                if not isinstance(ability, Ability):
                    continue
                if ability.current_cooldown > 0:
                    ability.current_cooldown -= 1
    game_state.current_turn += 1
    game_state.current_turn = game_state.current_turn % len(game_state.turn_order)
    return game_state

def defend(entity: Character, game_state: GameState):
    entity.is_defending = True

    return {"message": f"{entity.name} is defending.", "success": True}

def update_game_state(game_state: GameState) -> GameState:
    """Updates game state after any action"""
    # Remove defeated entities
    # game_state.enemies = [e for e in game_state.enemies if e.stats['health'] > 0]
    # game_state.characters = [c for c in game_state.characters if c.stats['health'] > 0]
    
    # Update turn order if entities were removed
    calculate_turn_order(game_state)

    # Make sure the current turn index is within bounds
    game_state.current_turn = game_state.current_turn % len(game_state.turn_order)
    
    
    # Check victory/defeat conditions
    if check_victory(game_state):
        game_state.status = "victory"
    elif check_defeat(game_state):
        game_state.status = "defeat"
    
    return game_state

def process_enemy_turns(game_state: GameState, enemy_id: UUID | str) -> Dict[str, str]:
    """Process all enemy turns and return results"""
    messages = []

    print(f"[Debug] Processing enemy turns within function")
    
    enemy = get_entity_by_id(game_state, entity_id=enemy_id)
        
    print(f"[Debug] Processing enemy {enemy.name}: {enemy.id = }")

    process_status_effects(enemy, game_state)

    ai_action = enemy_ai(game_state, enemy)

    print(f"[Debug] {ai_action = }")
    
    if ai_action['action'] == 'attack':
        print(f"[Debug] {enemy.name} decided to attack {ai_action['target'].name}")
        enemy_target = get_entity_by_id(game_state, ai_action['target'].id)
        result = perform_attack(enemy, enemy_target, game_state)
        messages.extend(result['message'])
        
    elif ai_action['action'] == 'cast_spell':
        result = cast_spell(enemy, ai_action['spell'], ai_action['target'], game_state)
        if result['success']:
            messages.append(result['message'])
            
    elif ai_action['action'] == 'defend':
        result = defend(enemy, game_state)
        messages.append(result['message'])
    
    # Update game state after each enemy action
    game_state = update_game_state(game_state)

    
    return {
        "message": messages if messages else [f"{enemy.name} used Wait and See..."],
        "game_state": game_state
    }

def execute_turn(game_state: GameState, action_result: Dict) -> Dict:
    """Execute a full turn not including enemy actions"""
    messages = [action_result['message']]
    
    # Process status effects and advance turn
    game_state = process_turn(game_state)
    
    # Process enemy turns if game is still ongoing
    if game_state.status in ["ongoing", "waiting"]:
        print(f"{game_state.current_turn = }")
        print(f"{game_state.turn_order = }")
        enemy = get_entity_by_id(game_state, entity_id=game_state.turn_order[game_state.current_turn])
        while enemy.stats["health"] <= 0:
            game_state.current_turn += 1
            game_state.current_turn = game_state.current_turn % len(game_state.turn_order)
            enemy = get_entity_by_id(game_state, entity_id=game_state.turn_order[game_state.current_turn])
        
        if isinstance(enemy, Enemy):
            print(f"[Debug] Enemy is Going Next")
            game_state.status = "waiting"
            

        print(f"[Debug] {game_state.status = }")
        print(f"[Debug] Player's turn - {game_state.turn_order[game_state.current_turn]}")
    
    # Final state update
    game_state = update_game_state(game_state)
    
    return {
        "message": messages,
        "status": game_state.status,
        "game_state": game_state,
        "next_is_enemy": game_state.status == "waiting"
    }


# ...