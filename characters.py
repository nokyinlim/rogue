

from uuid import uuid4
from models import Character

import abilities
import spells

hero = lambda level, abilities = {
    "heavy_attack": 1
}, spells = {}, id = None, experience = 0, owner_id = None: Character(
    id = id if id else uuid4(),
    owner_id=owner_id,
    name="Hero",
    level=level,
    experience=experience,
    stats={
        # 'health': 100,
        # 'max_health': 100,
        # 'physical_defense': 10,
        # 'magical_defense': 5,
        # 'mana_points': 50,
        # 'max_mana_points': 50,
        # 'ability_points': 30,
        # 'max_ability_points': 30,
        # 'attack_damage': 40,
        # 'spell_damage': 30,
        # 'hit_count': 1,
        # 'agility': 0.1,
        # 'accuracy': 0.8,
        # 'critical_hit_chance': 0.05,
        # 'action_speed': 10
        'health': 100 + 10 * level + 1.1 ** min(10, level),
        'max_health': 100 + 10 * level + 1.1 ** min(10, level),
        'physical_defense': 10 + 1 * level + 1.1 ** min(10, level),
        'magical_defense': 5 + 1 * level + 1.1 ** min(10, level),
        'mana_points': 50 + 5 * level + 1.1 ** min(10, level),
        'max_mana_points': 50 + 5 * level + 1.1 ** min(10, level),
        'ability_points': 30 + 3 * level + 1.1 ** min(10, level),
        'max_ability_points': 30 + 3 * level + 1.1 ** min(10, level),
        'attack_damage': 40 + 4 * level + 1.1 ** min(10, level),
        'spell_damage': 30 + 3 * level + 1.1 ** min(10, level),
        'hit_count': 1,
        'agility': 0.1 + 0.01 * level + 1.1 ** min(10, level),
        'accuracy': 0.8 + 0.01 * level + 1.1 ** min(10, level),
        'critical_hit_chance': 0.05 + 0.01 * level + 1.1 ** min(10, level),
        'action_speed': 10 + 1 * level + 1.1 ** min(10, level)
    },
    base_stats={
        'strength': 10 + level * 0.8,
        'dexterity': 8 + level * 0.8,
        'intelligence': 4 + level * 0.9,
        'speed': 6 + level * 0.6,
    },
    abilities=abilities,
    spells=spells
)