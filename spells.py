from models import Spell, Effect
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
        type = "debuff",
        target_stat = "accuracy",
        value = 0.2 + 0.1 * level,
        duration = 3 + level // 3
    )],
    target_type = "all_enemies"
)

glue_bomb: Callable[[int], Spell] = lambda level:Spell(
    name = f"Glue Bomb Lvl. {level}",
    description = f"Reduces Agility of enemies within glue for {3 + level // 3} turns. Agility decrease and turn count further improved based on Spell level.",
    type = "debuff",
    cost = 3 + 2 * level,
    effects = [Effect(
        type = "debuff",
        target_stat = "agility",
        value = 0.2 + 0.1 * level,
        duration = 3 + level // 3
    )],
    target_type = "all_enemies"
)

magic_barrier: Callable[[int], Spell] = lambda level:Spell(
    name = f"Magic Barrier Lvl. {level}",
    description = f"Creates a barrier reduces Magic Damage for {3 + level // 4} turns. Damage reduction and turn count further improved based on Spell level.",
    type = "buff",
    cost = 4 + 2 * level,
    effects = [Effect(
        type = "buff",
        target_stat = "magical_defense",
        value = 30 + 15 * level,
        duration = 3 + level // 4
    )],
    target_type = "all_allies"
)

lightning_strike: Callable[[int], Spell] = lambda level:Spell(
    name = f"Lightning Strike Lvl. {level}",
    description = "Strikes an enemy with lightning, dealing moderate damage. Damage increased based on Spell level.",
    type = "damage",
    cost = 6 + 4 * level,
    effects = [Effect(
        type = "damage",
        value = 20 + 15 * level,
        duration = 1
    )],
    target_type = "single"
)

divine_radiance: Callable[[int], Spell] = lambda level:Spell(
    name = f"Divine Radiance Lvl. {level}",
    description = "Shines a light, dealing minor damage with major damage bonus against Undead. Damage bonus further increased based on Spell level.",
    type = "damage-undead",
    cost = 5 + 3 * level,
    effects = [Effect(
        type = "damage-undead",
        value = 30 + 20 * level,
        duration = 1
    )],
)

warrior_cry: Callable[[int], Spell] = lambda level:Spell(
    name = f"Warrior Cry Lvl. {level}",
    description = f"Increases self attack power and reduces defense power for {4 + level // 4} turns. Damage increase, duration, and defense decrease further improved based on Spell level.",
    type = "buff",
    cost = 4 + 2 * level,
    effects = [Effect(
        type = "buff",
        target_stat = "attack_damage",
        value = 10 + 5 * level,
        duration = 3
    )],
    target_type = "self"
)

ice_shard: Callable[[int], Spell] = lambda level:Spell(
    name = f"Ice Shard Lvl. {level}",
    description = "Launches a shard of ice at an enemy, dealing moderate damage and slowing them. Damage and slow effect increased based on Spell level.",
    type = "damage",
    cost = 4 + 2 * level,
    effects = [Effect(
        type = "damage",
        value = 18 + 10 * level,
        duration = 1
    ), Effect(
        type = "debuff",
        target_stat = "speed",
        value = 0.1 + 0.05 * level,
        duration = 2
    )],
    target_type = "single"
)

earthquake: Callable[[int], Spell] = lambda level:Spell(
    name = f"Earthquake Lvl. {level}",
    description = "Shakes the ground, dealing damage to all enemies and reducing their defense. Damage and defense reduction increased based on Spell level.",
    type = "damage",
    cost = 8 + 3 * level,
    effects = [Effect(
        type = "damage",
        value = 25 + 10 * level,
        duration = 1
    ), Effect(
        type = "debuff",
        target_stat = "defense",
        value = 0.1 + 0.05 * level,
        duration = 3
    )],
    target_type = "all_enemies"
)

wind_blast: Callable[[int], Spell] = lambda level:Spell(
    name = f"Wind Blast Lvl. {level}",
    description = "Blasts an enemy with wind, dealing damage and pushing them back. Damage and push effect increased based on Spell level.",
    type = "damage",
    cost = 5 + 2 * level,
    effects = [Effect(
        type = "damage",
        value = 20 + 10 * level,
        duration = 1
    ), Effect(
        type = "debuff",
        target_stat = "position",
        value = 1 + level,
        duration = 1
    )],
    target_type = "single"
)

poison_cloud: Callable[[int], Spell] = lambda level:Spell(
    name = f"Poison Cloud Lvl. {level}",
    description = "Creates a cloud of poison, dealing damage over time to all enemies. Damage over time increased based on Spell level.",
    type = "dot",
    cost = 6 + 3 * level,
    effects = [Effect(
        type = "dot",
        value = 10 + 5 * level,
        duration = 3
    )],
    target_type = "all_enemies"
)

def get_spell(spell_id: str, spell_level: int) -> Spell:
    spells = {
        "fireball": fireball,
        "heal": heal,
        "dodge": dodge,
        "ignition": ignition,
        "smoke_bomb": smoke_bomb,
        "glue_bomb": glue_bomb,
        "magic_barrier": magic_barrier,
        "lightning_strike": lightning_strike,
        "divine_radiance": divine_radiance,
        "warrior_cry": warrior_cry,
        "ice_shard": ice_shard,
        "earthquake": earthquake,
        "wind_blast": wind_blast,
        "poison_cloud": poison_cloud,
    }
    return spells[spell_id](spell_level)


# Non-learnable spells

ice_bolt = lambda level: Spell(
    name = "Ice Bolt",
    description = "Launches a bolt of ice at an enemy, dealing moderate damage.",
    type = "damage",
    cost = 5,
    effects = [Effect(
        type = "damage",
        value = 80 + 20 * level,
        duration = 1
    )],
    target_type = "single"
)

lightning_bolt = lambda level: Spell(
    name = "Lightning Bolt",
    description = "Strikes an enemy with lightning, dealing moderate damage.",
    type = "damage",
    cost = 5,
    effects = [Effect(
        type = "damage",
        value = 80 + 20 * level,
        duration = 1
    )],
    target_type = "single"
)
