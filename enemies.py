from models import Enemy
from typing import Dict


goblin = Enemy(
    name="Goblin",
    level=0,
    stats={
        'health': 50,
        'max_health': 50,
        'physical_defense': 5,
        'magical_defense': 2,
        'mana_points': 20,
        'ability_points': 10,
        'attack_damage': 20,
        'spell_damage': 5,
        'hit_count': 1,
        'agility': 0.05,
        'accuracy': 0.85,
        'critical_hit_chance': 0.02,
        'action_speed': 8
    }
)

goblin_cleric = Enemy(
    name = "Goblin Cleric",
    level = 0,
    stats = {
        "health": 30,
        'max_health': 30,
        'physical_defense': 2,
        'magical_defense': 5,
        'mana_points': 20,
        'ability_points': 20,
        'attack_damage': 10,
        'spell_damage': 20,
        'hit_count': 1,
        'agility': 0.02,
        'accuracy': 0.7,
        'critical_hit_chance': 0,
        'action_speed': 6
    },
    spells = []
)

ENEMIES: Dict[str, Enemy] = {}

def initialize_enemy(enemy_id: str, level: int) -> Enemy:
    pass




