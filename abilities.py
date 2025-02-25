from models import Ability, Effect
from typing import Callable

slash: Callable[[int], Ability] = lambda level:Ability(
    name = f"Slash Lvl. {level}",
    description = "A basic sword attack dealing moderate damage. Damage increases with Ability level.",
    type = "damage",
    cost = 3 + level,
    effects = [Effect(
        type = "damage",
        value = 20 + 10 * level,
        duration = 1
    )],
    target_type = "single",
    accuracy_bonus = 0.1,
    critical_bonus = 0.05
)

heavy_attack: Callable[[int], Ability] = lambda level:Ability(
    name = f"Heavy Attack Lvl. {level}",
    description = "A moderate physical attack with high accuracy. Damage increases with Ability level.",
    type = "damage",
    cost = 2 + 3 * level,
    effects = [Effect(
        type = "damage",
        value = 25 + 12 * level,
        duration = 1
    )],
    target_type = "single",
    accuracy_bonus = 0.4 + 0.1 * level,
    critical_bonus = 0.1 + 0.02 * level
)

double_strike: Callable[[int], Ability] = lambda level:Ability(
    name = f"Double Strike Lvl. {level}",
    description = "Two quick strikes in succession. Damage and accuracy increase with Ability level.",
    type = "damage",
    cost = 5 + 2 * level,
    effects = [Effect(
        type = "damage",
        value = 15 + 8 * level,
        duration = 1
    )] * 2,
    target_type = "single",
    accuracy_bonus = 0.05 + 0.02 * level,
    critical_bonus = 0.1 + 0.02 * level
)

shield_bash: Callable[[int], Ability] = lambda level:Ability(
    name = f"Shield Bash Lvl. {level}",
    description = "Target immobilized, reducing defense and agility and deals minor damage. Damage, immobilization duration and stat reduced amount increase with Ability level.",
    type = "damage",
    cost = 4 + 2 * level,
    effects = [
        Effect(type = "damage", value = 10 + 5 * level, duration = 1),
        Effect(type = "debuff", target_stat = "physical_defense", value = -10 - 5 * level, duration = 1 + level // 3),
        Effect(type = "debuff", target_stat = "agility", value = -0.1 - 0.05 * level, duration = 1 + level // 3),
    ],
    target_type = "single",
    accuracy_bonus = 0.15,
    critical_bonus = -0.3
)

whirlwind: Callable[[int], Ability] = lambda level:Ability(
    name = f"Whirlwind Lvl. {level}",
    description = "Spin attack hitting all enemies with reduced accuracy. Damage increases with Ability level.",
    type = "damage",
    cost = 6 + 2 * level,
    effects = [Effect(
        type = "damage",
        value = 15 + 8 * level,
        duration = 1
    )],
    target_type = "all_enemies",
    accuracy_bonus = -0.2,
    critical_bonus = -0.1 * level
)

precise_strike: Callable[[int], Ability] = lambda level:Ability(
    name = f"Precise Strike Lvl. {level}",
    description = "A precise attack with high accuracy and critical chance. Accuracy and critical hit chance increases with Ability level.",
    type = "damage",
    cost = 5 + level,
    effects = [Effect(
        type = "damage",
        value = 25,
        duration = 1
    )],
    target_type = "single",
    accuracy_bonus = 0.3 + 0.05 * level,
    critical_bonus = 0.2 + 0.05 * level
)

backstab: Callable[[int], Ability] = lambda level:Ability(
    name = f"Backstab Lvl. {level}",
    description = "A sneaky attack dealing high damage. Bonus damage against vulnerable targets, and Damage further increased based on Ability level.",
    type = "damage",
    cost = 6 + 6 * level,
    effects = [Effect(
        type = "damage",
        value = 35 + 15 * level,
        duration = 1
    )],
    target_type = "single",
    accuracy_bonus = 0.2,
    critical_bonus = 0.15
)

disarming_strike: Callable[[int], Ability] = lambda level:Ability(
    name = f"Disarming Strike Lvl. {level}",
    description = "Reduces target's attack damage while dealing moderate damage.",
    type = "damage",
    cost = 4 + 2 * level,
    effects = [
        Effect(type = "damage", value = 20 + 8 * level, duration = 1),
        Effect(type = "debuff", target_stat = "attack_damage", value = -(10 + 5 * level), duration = 2 + level // 2)
    ],
    target_type = "single",
    accuracy_bonus = 0.1
)

battle_stance: Callable[[int], Ability] = lambda level:Ability(
    name = f"Battle Stance Lvl. {level}",
    description = "Enter a fighting stance increasing attack damage and defense.",
    type = "buff",
    cost = 5 + level,
    effects = [
        Effect(type = "buff", target_stat = "attack_damage", value = 15 + 8 * level, duration = 3),
        Effect(type = "buff", target_stat = "physical_defense", value = 10 + 5 * level, duration = 3)
    ],
    target_type = "self",
    cooldown = 4
)

execute: Callable[[int], Ability] = lambda level:Ability(
    name = f"Execute Lvl. {level}",
    description = "Powerful finishing move that deals more damage to low health targets. Cooldown of 3 turns.",
    type = "damage",
    cost = 8 + 8 * level,
    effects = [Effect(
        type = "damage",
        value = 50 + 20 * level,
        duration = 1
    )],
    target_type = "single",
    accuracy_bonus = 0.15,
    critical_bonus = 0.2,
    cooldown = 3
)

eruption_strike: Callable[[int], Ability] = lambda level:Ability(
    name = f"Eruption Strike Lvl. {level}",
    description = "A fiery strike that deals major damage to one target",
    type = "damage",
    cost = 6 + 2 * level,
    effects = [
        Effect(type = "damage", value = 25 + 10 * level, duration = 1),
    ],
    target_type = "single",
    accuracy_bonus = 0.1,
    critical_bonus = 0.1
)

wild_strike: Callable[[int], Ability] = lambda level:Ability(
    name = f"Wild Strike Lvl. {level}",
    description = "A wild strike that deals High damage to one target. Afterward, own Agility is reduced. Damage, and Agility reduction amount and turns increased based on Ability level.",
    type = "damage",
    cost = 6 + 3 * level,
    effects = [
        Effect(type = "damage", value = 30 + 15 * level, duration = 1),
        Effect(type = "debuff", target_stat = "agility", value = -0.1 - 0.05 * level, duration = 2 + level // 2)
    ],
    target_type = "single",
    accuracy_bonus = 0.05,
    critical_bonus = 0
)

mental_unity: Callable[[int], Ability] = lambda level:Ability(
    name = f"Mental Unity Lvl. {level}",
    description = "Mental focus that increases own magical defense and spell damage for 4 turns. Magical Defense and Spell Damage increase based on Ability level.",
    type = "buff",
    cost = 4 + 2 * level,
    effects = [
        Effect(type = "buff", target_stat = "magical_defense", value = 10 + 5 * level, duration = 4),
        Effect(type = "buff", target_stat = "spell_damage", value = 15 + 8 * level, duration = 4)
    ],
    target_type = "self",
    cooldown = 4,
    accuracy_bonus=0,
    critical_bonus=0
)


def get_ability(ability_id: str, ability_level: int) -> Ability:
    abilities = {
        "slash": slash,
        "double_strike": double_strike,
        "shield_bash": shield_bash,
        "whirlwind": whirlwind,
        "precise_strike": precise_strike,
        "backstab": backstab,
        "disarming_strike": disarming_strike,
        "battle_stance": battle_stance,
        "execute": execute,
        "eruption_strike": eruption_strike,
        "heavy_attack": heavy_attack,
        "wild_strike": wild_strike,
        "mental_unity": mental_unity
    }
    return abilities[ability_id](ability_level)


""" NOT LEARNABLE ABILITIES """

smile = lambda level:Ability(
    name = "Nonchalant Smile",
    description = "",
    type = "buff",
    cost = 3 + level * 2,
    effects = [
        Effect(type = "buff", target_stat = "agility", value = 0.1 + 0.05 * level, duration = 3 + level // 3),
        Effect(type = "buff", target_stat = "accuracy", value = 0.1 + 0.05 * level, duration = 3 + level // 3)
    ],
    target_type = "all_allies",
    accuracy_bonus = 0,
    critical_bonus = 0
)

king_sword = lambda level:Ability(
    name = "King's Sword",
    description = "",
    type = "damage",
    cost = 5 + level * 3,
    effects = [
        Effect(type = "damage", value = 25 + 15 * level, duration = 1)
    ],
    target_type = "single",
    accuracy_bonus = 0.1,
    critical_bonus = 0
)

warrior_cry = lambda level:Ability(
    name = "Warrior Cry",
    description = "",
    type = "buff",
    cost = 4 + 2 * level,
    effects = [
        Effect(type = "buff", target_stat = "attack_damage", value = 10 + 5 * level, duration = 3)
    ],
    target_type = "self",
    accuracy_bonus = 0,
    critical_bonus = 0
)

brutal_slam = lambda level:Ability(
    name = "Brutal Slam",
    description = "",
    type = "damage",
    cost = 6 + 4 * level,
    effects = [
        Effect(type = "damage", value = 20 + 10 * level, duration = 1)
    ],
    target_type = "single",
    accuracy_bonus = 0.1,
    critical_bonus = 0
)

brandish = lambda level:Ability(
    name = "Brandish",
    description = "",
    type = "damage",
    cost = 5 + 3 * level,
    effects = [
        Effect(type = "damage", value = 60 + 10 * level, duration = 1)
    ],
    target_type = "single",
    accuracy_bonus = 0.2,
    critical_bonus = 0
)

armored_charge = lambda level:Ability(
    name = "Armored Charge",
    description = "",
    type = "damage",
    cost = 6 + 2 * level,
    effects = [
        Effect(type = "damage", value = 50 + 8 * level, duration = 1)
    ],
    target_type = "single",
    accuracy_bonus = 0.1,
    critical_bonus = 0
)

archer_shot = lambda level:Ability(
    name = "Archer Shot",
    description = "",
    type = "damage",
    cost = 5 + 3 * level,
    effects = [
        Effect(type = "damage", value = 35 + 10 * level, duration = 1)
    ],
    target_type = "single",
    accuracy_bonus = 0.1,
    critical_bonus = 0.3
)

point_blank = lambda level:Ability(
    name = "Point Blank",
    description = "",
    type = "damage",
    cost = 4 + 2 * level,
    effects = [
        Effect(type = "damage", value = 30 + 8 * level, duration = 1)
    ],
    target_type = "single",
    accuracy_bonus = 1,
    critical_bonus = 0.2
)

death_stroke = lambda level:Ability(
    name = "Death Stroke",
    description = "",
    type = "damage",
    cost = 6 + 4 * level,
    effects = [
        Effect(type = "damage", value = 40 + 15 * level, duration = 1)
    ],
    target_type = "single",
    accuracy_bonus = 0.1,
    critical_bonus = 0.4
)

chaos_blast = lambda level:Ability(
    name = "Chaos Blast",
    description = "",
    type = "damage",
    cost = 8 + 6 * level,
    effects = [
        Effect(type = "damage", value = 100 + 50 * level, duration = 1),
        Effect(
            type = "debuff",
            target_stat = "defense",
            value = -0.1 - 0.05 * level,
            duration = 2
        )
    ],
    target_type = "single",
    accuracy_bonus = 0.1,
    critical_bonus = 0.2
)

chaos_wave = lambda level:Ability(
    name = "Chaos Wave",
    description = "",
    type = "damage",
    cost = 10 + 8 * level,
    effects = [
        Effect(type = "damage", value = 80 + 40 * level, duration = 1),
        Effect(
            type = "hot",
            value = 15 + 10 * level,
            duration = 2
        )
    ],
    target_type = "all_enemies",
    accuracy_bonus = 0.1,
    critical_bonus = 0.2
)

chaos_storm = lambda level:Ability(
    name = "Chaos Storm",
    description = "",
    type = "damage",
    cost = 12 + 10 * level,
    effects = [
        Effect(type = "damage", value = 120 + 60 * level, duration = 1),
        Effect(
            type = "debuff",
            target_stat = "agility",
            value = -0.1 - 0.05 * level,
            duration = 2
        )
    ],
    target_type = "all_enemies",
    accuracy_bonus = 0.1,
    critical_bonus = 0.2
)

def get_non_learnable_ability(ability_name: str, ability_level: int) -> Ability:
    non_learnable_abilities = {
        "smile": smile,
        "king_sword": king_sword,
        "warrior_cry": warrior_cry,
        "brutal_slam": brutal_slam,
        "brandish": brandish,
        "armored_charge": armored_charge,
        "archer_shot": archer_shot,
        "point_blank": point_blank,
        "death_stroke": death_stroke,
        "chaos_blast": chaos_blast,
        "chaos_wave": chaos_wave,
        "chaos_storm": chaos_storm
    }
    return non_learnable_abilities[ability_name](ability_level)