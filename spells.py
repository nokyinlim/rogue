from models import Spell
from typing import Callable

fireball: Callable[[int], Spell] = lambda level:Spell(
    name = f"Fireball Lvl. {level}",
    description = "Launch a fireball against an enemy dealing low damage. Damage increased based on Spell level.",
    type = "damage",
    cost = 5 + 2 * level,
    effects = [Effect(
        type = "damage",
        value = 15 + 5 * level,
        duration = 1
    )],
    target_type = "single",
)

heal: Callable[[int], Spell] = lambda level:Spell(
    name = f"Heal Lvl. {level}",
    description = f"Heal a target for minor health. Heal amount further increased based on Spell level.",
    type = "heal",
    cost = 5 + 3 * level,
    effects = [Effect(
        type = "heal",
        value = 25 + 15 * level,
        duration = 1
    )],
    target_type = "single"
)


dodge: Callable[[int], Spell] = lambda level:Spell(
    name = f"Dodge Lvl. {level}",
    description = "Increased agility for 3 turns. Agility buff further increased based on Spell level.",
    type = "buff",
    cost = 3 + 1 * level,
    effects = [Effect(
        type = "buff",
        target_stat = "agility",
        value = 0.15 + level * 0.05,
        duration = 3
    )],
    target_type = "all_enemies"
)

ignition: Callable[[int], Spell] = lambda level:Spell(
    name = f"Ignition Lvl. {level}",
    description = "Deals very minor damage but ignites enemy for 2 turns. Damage over Time and Initial Damage increased based on Spell level.",
    type = "dot",
    cost = 5 + 2 * level,
    effects = [Effect(
        type = "damage",
        value = 5 + level * 2,
        duration = 1
    ), Effect(
        type = "dot",
        value = 10 + level * 5,
        duration = 2,
    )],
    target_type = "single"
)

smoke_bomb: Callable[[int], Spell] = lambda level:Spell(
    name = f"Smoke Bomb Lvl. {level}",
    description = f"Blinds enemies within smoke, reducing their accuracy for {3 + level // 3} turns. Accuracy decrease and turn count further improved based on Spell level.",
    type = "debuff",
    cost = 3 + 2 * level,
    effects = [Effect(
        type = "damage",
        target_stat = "accuracy",
        value = 0.2 + 0.1 * level,
        duration = 3 + level // 3
    )],
    target_type = "all_enemies"
)

glue_bomb: Callable[[int], Spell] = lambda level:Spell(
    
)


def get_spell(spell_id: str, spell_level: int) -> Spell:



    pass