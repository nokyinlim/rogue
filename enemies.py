from models import Enemy
from typing import Dict

import spells
import abilities

goblin = lambda level:Enemy(
    name="Goblin",
    level=level,
    stats={
        'health': 50 + level * 8,
        'max_health': 50 + level * 8,
        'physical_defense': 5 + level * 2,
        'magical_defense': 2 + level,
        'mana_points': 20 + level * 2,
        'max_mana_points': 20 + level * 2,
        'ability_points': 10 + level * 2,
        'max_ability_points': 10 + level * 2,
        'attack_damage': 20 + level * 4,
        'spell_damage': 5 + level,
        'hit_count': 1,
        'agility': 0.05 + level * 0.005,
        'accuracy': 0.85 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 8 + level * 0.6
    },
    base_stats={
        'strength': 5 + level * 5 / 6,
        'intelligence': 3 + level * 3 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 2 + level * 2 / 6
    },
    abilities=[abilities.heavy_attack(1)],
    power = 100 + level * 10
)

goblin_cleric = lambda level:Enemy(
    name = "Goblin Cleric",
    level = level,
    stats = {
        "health": 30 + level * 5,
        'max_health': 30 + level * 5,
        'physical_defense': 2 + level,
        'magical_defense': 5 + level * 2,
        'mana_points': 20 + level * 5,
        'ability_points': 20 + level * 5,
        'attack_damage': 10 + level * 2,
        'spell_damage': 20 + level * 4,
        'hit_count': 1,
        'agility': 0.02 + level * 0.002,
        'accuracy': 0.7 + level * 0.01,
        'critical_hit_chance': 0,
        'action_speed': 6 + level * 0.5
    },
    base_stats={
        'strength': 3 + level * 3 / 6,
        'intelligence': 5 + level * 5 / 6,
        'dexterity': 3 + level * 3 / 6,
        'speed': 3 + level * 3 / 6
    },
    spells=[spells.heal(1)],
    power = 100 + level * 10
)

goblin_warrior = lambda level:Enemy(
    name = "Goblin Warrior",
    level = level,
    stats = {
        "health": 70 + level * 10,
        'max_health': 70 + level * 10,
        'physical_defense': 10 + level * 3,
        'magical_defense': 2 + level,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 30 + level * 6,
        'spell_damage': 5 + level,
        'hit_count': 1,
        'agility': 0.05 + level * 0.005,
        'accuracy': 0.8 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 8 + level * 0.6
    },
    base_stats={
        'strength': 6 + level * 6 / 6,
        'intelligence': 2 + level * 2 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 2 + level * 2 / 6
    },
    abilities=[abilities.warrior_cry(1)],
    power = 120 + level * 12
)

goblin_mage = lambda level:Enemy(
    name = "Goblin Mage",
    level = level,
    stats = {
        "health": 30 + level * 5,
        'max_health': 30 + level * 5,
        'physical_defense': 2 + level,
        'magical_defense': 5 + level * 2,
        'mana_points': 20 + level * 5,
        'ability_points': 20 + level * 5,
        'attack_damage': 10 + level * 2,
        'spell_damage': 20 + level * 4,
        'hit_count': 1,
        'agility': 0.02 + level * 0.002,
        'accuracy': 0.7 + level * 0.01,
        'critical_hit_chance': 0,
        'action_speed': 6 + level * 0.5
    },
    base_stats={
        'strength': 3 + level * 3 / 6,
        'intelligence': 5 + level * 5 / 6,
        'dexterity': 3 + level * 3 / 6,
        'speed': 3 + level * 3 / 6
    },
    spells = [
        spells.fireball(1)
    ],
    power = 90 + level * 9
)

smiling_goblin = lambda level: Enemy(
    name = "Smiling Goblin",
    level = level,
    stats = {
        "health": 50 + level * 8,
        'max_health': 50 + level * 8,
        'physical_defense': 5 + level * 2,
        'magical_defense': 2 + level,
        'mana_points': 20 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 20 + level * 4,
        'spell_damage': 5 + level,
        'hit_count': 1,
        'agility': 0.05 + level * 0.005,
        'accuracy': 0.85 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 8 + level * 0.6
    },
    base_stats={
        'strength': 5 + level * 5 / 6,
        'intelligence': 3 + level * 3 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 2 + level * 2 / 6
    },
    abilities = [
        abilities.smile(1)
    ],
    power = 70 + level * 7
)

goblin_king = lambda level: Enemy(
    name = "Goblin King",
    level = level,
    stats = {
        "health": 100 + level * 15,
        'max_health': 100 + level * 15,
        'physical_defense': 15 + level * 4,
        'magical_defense': 5 + level * 2,
        'mana_points': 30 + level * 5,
        'ability_points': 20 + level * 5,
        'attack_damage': 40 + level * 8,
        'spell_damage': 10 + level * 2,
        'hit_count': 1,
        'agility': 0.1 + level * 0.01,
        'accuracy': 0.9 + level * 0.01,
        'critical_hit_chance': 0.05 + level * 0.005,
        'action_speed': 10 + level * 0.8
    },
    base_stats={
        'strength': 8 + level * 8 / 6,
        'intelligence': 4 + level * 4 / 6,
        'dexterity': 6 + level * 6 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities = [
        abilities.king_sword(1)
    ],
    power = 200 + level * 20
)



orc = lambda level: Enemy(
    name="Orc",
    level=level,
    stats={
        'health': 120 + level * 12,
        'max_health': 120 + level * 12,
        'physical_defense': 20 + level * 4,
        'magical_defense': 5 + level * 2,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 50 + level * 10,
        'spell_damage': 5 + level,
        'hit_count': 1,
        'agility': 0.03 + level * 0.003,
        'accuracy': 0.75 + level * 0.01,
        'critical_hit_chance': 0.03 + level * 0.003,
        'action_speed': 7 + level * 0.5
    },
    base_stats={
        'strength': 10 + level * 10 / 6,
        'intelligence': 2 + level * 2 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities=[abilities.brutal_slam(1)],
    power=150 + level * 15
)

orc_shaman = lambda level: Enemy(
    name="Orc Shaman",
    level=level,
    stats={
        'health': 80 + level * 10,
        'max_health': 80 + level * 10,
        'physical_defense': 10 + level * 3,
        'magical_defense': 10 + level * 4,
        'mana_points': 30 + level * 5,
        'ability_points': 20 + level * 5,
        'attack_damage': 20 + level * 4,
        'spell_damage': 30 + level * 6,
        'hit_count': 1,
        'agility': 0.02 + level * 0.002,
        'accuracy': 0.7 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 6 + level * 0.5
    },
    base_stats={
        'strength': 5 + level * 5 / 6,
        'intelligence': 6 + level * 6 / 6,
        'dexterity': 3 + level * 3 / 6,
        'speed': 3 + level * 3 / 6
    },
    spells=[spells.heal(2 + level // 3)],
    power=140 + level * 14
)

orc_soldier = lambda level: Enemy(
    name="Orc Soldier",
    level=level,
    stats={
        'health': 150 + level * 15,
        'max_health': 150 + level * 15,
        'physical_defense': 25 + level * 5,
        'magical_defense': 5 + level * 2,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 60 + level * 12,
        'spell_damage': 5 + level,
        'hit_count': 1,
        'agility': 0.03 + level * 0.003,
        'accuracy': 0.75 + level * 0.01,
        'critical_hit_chance': 0.03 + level * 0.003,
        'action_speed': 7 + level * 0.5
    },
    base_stats={
        'strength': 12 + level * 12 / 6,
        'intelligence': 2 + level * 2 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities=[abilities.brutal_slam(3)],
    power=180 + level * 18
)

orc_warlock = lambda level: Enemy(
    name="Orc Warlock",
    level=level,
    stats={
        'health': 100 + level * 12,
        'max_health': 100 + level * 12,
        'physical_defense': 10 + level * 3,
        'magical_defense': 15 + level * 4,
        'mana_points': 30 + level * 5,
        'ability_points': 20 + level * 5,
        'attack_damage': 30 + level * 6,
        'spell_damage': 40 + level * 8,
        'hit_count': 1,
        'agility': 0.02 + level * 0.002,
        'accuracy': 0.7 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 6 + level * 0.5
    },
    base_stats={
        'strength': 6 + level * 6 / 6,
        'intelligence': 8 + level * 8 / 6,
        'dexterity': 3 + level * 3 / 6,
        'speed': 3 + level * 3 / 6
    },
    spells=[spells.fireball(3)],
    power=160 + level * 16
)

orc_chieftain = lambda level: Enemy(
    name="Orc Chieftain",
    level=level,
    stats={
        'health': 200 + level * 20,
        'max_health': 200 + level * 20,
        'physical_defense': 30 + level * 6,
        'magical_defense': 10 + level * 4,
        'mana_points': 20 + level * 5,
        'ability_points': 20 + level * 5,
        'attack_damage': 70 + level * 14,
        'spell_damage': 10 + level * 2,
        'hit_count': 1,
        'agility': 0.04 + level * 0.004,
        'accuracy': 0.8 + level * 0.01,
        'critical_hit_chance': 0.04 + level * 0.004,
        'action_speed': 8 + level * 0.6
    },
    base_stats={
        'strength': 14 + level * 14 / 6,
        'intelligence': 4 + level * 4 / 6,
        'dexterity': 6 + level * 6 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities=[abilities.brutal_slam(5)],
    power=220 + level * 22
)

orc_witch_doctor = lambda level: Enemy(
    name="Orc Witch Doctor",
    level=level,
    stats={
        'health': 150 + level * 15,
        'max_health': 150 + level * 15,
        'physical_defense': 20 + level * 4,
        'magical_defense': 20 + level * 6,
        'mana_points': 40 + level * 5,
        'ability_points': 30 + level * 5,
        'attack_damage': 40 + level * 8,
        'spell_damage': 50 + level * 10,
        'hit_count': 1,
        'agility': 0.03 + level * 0.003,
        'accuracy': 0.75 + level * 0.01,
        'critical_hit_chance': 0.03 + level * 0.003,
        'action_speed': 7 + level * 0.5
    },
    base_stats={
        'strength': 10 + level * 10 / 6,
        'intelligence': 12 + level * 12 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 3 + level * 3 / 6
    },
    spells=[spells.fireball(4)],
    power=200 + level * 20
)

orc_berserker = lambda level: Enemy(
    name="Orc Berserker",
    level=level,
    stats={
        'health': 180 + level * 18,
        'max_health': 180 + level * 18,
        'physical_defense': 25 + level * 5,
        'magical_defense': 10 + level * 3,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 80 + level * 16,
        'spell_damage': 5 + level,
        'hit_count': 1,
        'agility': 0.04 + level * 0.004,
        'accuracy': 0.8 + level * 0.01,
        'critical_hit_chance': 0.04 + level * 0.004,
        'action_speed': 8 + level * 0.6
    },
    base_stats={
        'strength': 16 + level * 16 / 6,
        'intelligence': 2 + level * 2 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities=[abilities.brutal_slam(6)],
    power=200 + level * 20
)

orc_princess = lambda level: Enemy(
    name="Orc Princess",
    level=level,
    stats={
        'health': 120 + level * 12,
        'max_health': 120 + level * 12,
        'physical_defense': 20 + level * 4,
        'magical_defense': 5 + level * 2,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 50 + level * 10,
        'spell_damage': 5 + level,
        'hit_count': 1,
        'agility': 0.03 + level * 0.003,
        'accuracy': 0.75 + level * 0.01,
        'critical_hit_chance': 0.03 + level * 0.003,
        'action_speed': 7 + level * 0.5
    },
    base_stats={
        'strength': 10 + level * 10 / 6,
        'intelligence': 2 + level * 2 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities=[abilities.brutal_slam(5)],
    power=150 + level * 15
)

# some more basic enemies here, like bandit, troll, etc. Intended for larger groups of them

bandit = lambda level:Enemy(
    name = "Bandit",
    level = level,
    stats = {
        "health": 40 + level * 10,
        'max_health': 40 + level * 10,
        'physical_defense': 5 + level * 2,
        'magical_defense': 2 + level,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 10 + level * 2,
        'spell_damage': 5 + level,
        'hit_count': 1,
        'agility': 0.05 + level * 0.005,
        'accuracy': 0.8 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 8 + level * 0.6
    },
    base_stats={
        'strength': 6 + level * 6 / 6,
        'intelligence': 2 + level * 2 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 3 + level * 3 / 6
    },
    power=40 + level * 4
)

troll = lambda level:Enemy(
    name = "Troll",
    level = level,
    stats = {
        "health": 100 + level * 15,
        'max_health': 100 + level * 15,
        'physical_defense': 15 + level * 4,
        'magical_defense': 5 + level * 2,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 40 + level * 8,
        'spell_damage': 5 + level,
        'hit_count': 1,
        'agility': 0.05 + level * 0.005,
        'accuracy': 0.8 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 8 + level * 0.6
    },
    base_stats={
        'strength': 8 + level * 8 / 6,
        'intelligence': 2 + level * 2 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 3 + level * 3 / 6
    },
    power=120 + level * 12
)

ruffian = lambda level:Enemy(
    name = "Ruffian",
    level = level,
    stats = {
        "health": 50 + level * 8,
        'max_health': 50 + level * 8,
        'physical_defense': 5 + level * 2,
        'magical_defense': 2 + level,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 20 + level * 4,
        'spell_damage': 5 + level,
        'hit_count': 1,
        'agility': 0.05 + level * 0.005,
        'accuracy': 0.8 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 8 + level * 0.6
    },
    base_stats={
        'strength': 5 + level * 5 / 6,
        'intelligence': 2 + level * 2 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 3 + level * 3 / 6
    },
    power=60 + level * 6
)

# Skeletons must have lower HP because of their undead, meaning they take reduced damage from most sources

skeleton = lambda level:Enemy(
    name = "Skeleton",
    level = level,
    stats = {
        "health": 100 + level * 15,
        'max_health': 100 + level * 15,
        'physical_defense': 10 + level * 3,
        'magical_defense': 10 + level * 4,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 30 + level * 6,
        'spell_damage': 30 + level * 6,
        'hit_count': 2,
        'agility': 0.02 + level * 0.002,
        'accuracy': 0.7 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 6 + level * 0.5
    },
    base_stats={
        'strength': 6 + level * 6 / 6,
        'intelligence': 4 + level * 4 / 6,
        'dexterity': 3 + level * 3 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities = [abilities.brandish(1)],
    power = 400 + level * 40,
    is_undead = True
)

skeleton_warrior = lambda level:Enemy(
    name = "Skeleton Warrior",
    level = level,
    stats = {
        "health": 150 + level * 20,
        'max_health': 150 + level * 20,
        'physical_defense': 15 + level * 4,
        'magical_defense': 15 + level * 6,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 40 + level * 8,
        'spell_damage': 30 + level * 6,
        'hit_count': 2,
        'agility': 0.03 + level * 0.003,
        'accuracy': 0.75 + level * 0.01,
        'critical_hit_chance': 0.03 + level * 0.003,
        'action_speed': 7 + level * 0.5
    },
    base_stats={
        'strength': 8 + level * 8 / 6,
        'intelligence': 4 + level * 4 / 6,
        'dexterity': 6 + level * 6 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities = [abilities.brandish(2)],
    power = 500 + level * 50,
    is_undead = True
)

skeleton_knight = lambda level:Enemy(
    name = "Skeleton Knight",
    level = level,
    stats = {
        "health": 200 + level * 25,
        'max_health': 200 + level * 25,
        'physical_defense': 20 + level * 5,
        'magical_defense': 20 + level * 6,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 50 + level * 10,
        'spell_damage': 40 + level * 8,
        'hit_count': 1,
        'agility': 0.04 + level * 0.004,
        'accuracy': 0.8 + level * 0.01,
        'critical_hit_chance': 0.04 + level * 0.004,
        'action_speed': 8 + level * 0.6
    },
    base_stats={
        'strength': 10 + level * 10 / 6,
        'intelligence': 6 + level * 6 / 6,
        'dexterity': 8 + level * 8 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities = [abilities.armored_charge(1)],
    power = 600 + level * 60,
    is_undead = True
)

skeleton_mage = lambda level:Enemy(
    name = "Skeleton Mage",
    level = level,
    stats = {
        "health": 100 + level * 15,
        'max_health': 100 + level * 15,
        'physical_defense': 10 + level * 3,
        'magical_defense': 10 + level * 4,
        'mana_points': 30 + level * 5,
        'ability_points': 20 + level * 5,
        'attack_damage': 30 + level * 6,
        'spell_damage': 40 + level * 8,
        'hit_count': 1,
        'agility': 0.02 + level * 0.002,
        'accuracy': 0.7 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 6 + level * 0.5
    },
    base_stats={
        'strength': 6 + level * 6 / 6,
        'intelligence': 8 + level * 8 / 6,
        'dexterity': 4 + level * 4 / 6,
        'speed': 3 + level * 3 / 6
    },
    spells = [
        spells.fireball(1)
    ],
    power = 400 + level * 40,
    is_undead = True
)

skeleton_archer = lambda level:Enemy(
    name = "Skeleton Archer",
    level = level,
    stats = {
        "health": 80 + level * 12,
        'max_health': 80 + level * 12,
        'physical_defense': 5 + level * 2,
        'magical_defense': 5 + level * 2,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 20 + level * 4,
        'spell_damage': 20 + level * 4,
        'hit_count': 1,
        'agility': 0.03 + level * 0.003,
        'accuracy': 0.75 + level * 0.01,
        'critical_hit_chance': 0.03 + level * 0.003,
        'action_speed': 7 + level * 0.5
    },
    base_stats={
        'strength': 4 + level * 4 / 6,
        'intelligence': 4 + level * 4 / 6,
        'dexterity': 6 + level * 6 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities = [
        abilities.archer_shot(1),
        abilities.point_blank(1)
    ],
    power = 380 + level * 30,
    is_undead = True
)

skeleton_swordsman = lambda level:Enemy(
    name = "Skeleton Swordsman",
    level = level,
    stats = {
        "health": 120 + level * 18,
        'max_health': 120 + level * 18,
        'physical_defense': 10 + level * 3,
        'magical_defense': 10 + level * 4,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 30 + level * 6,
        'spell_damage': 30 + level * 6,
        'hit_count': 2,
        'agility': 0.02 + level * 0.002,
        'accuracy': 0.7 + level * 0.01,
        'critical_hit_chance': 0.02 + level * 0.002,
        'action_speed': 6 + level * 0.5
    },
    base_stats={
        'strength': 6 + level * 6 / 6,
        'intelligence': 4 + level * 4 / 6,
        'dexterity': 6 + level * 6 / 6,
        'speed': 3 + level * 3 / 6
    },
    power = 450 + level * 30,
    is_undead = True,
    abilities = [abilities.brandish(2)]
)

elite_skeleton = lambda level:Enemy(
    name = "Elite Skeleton",
    level = level,
    stats = {
        "health": 150 + level * 20,
        'max_health': 150 + level * 20,
        'physical_defense': 15 + level * 4,
        'magical_defense': 15 + level * 6,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 40 + level * 8,
        'spell_damage': 40 + level * 8,
        'hit_count': 2,
        'agility': 0.03 + level * 0.003,
        'accuracy': 0.75 + level * 0.01,
        'critical_hit_chance': 0.03 + level * 0.003,
        'action_speed': 7 + level * 0.5
    },
    base_stats={
        'strength': 8 + level * 8 / 6,
        'intelligence': 6 + level * 6 / 6,
        'dexterity': 8 + level * 8 / 6,
        'speed': 3 + level * 3 / 6
    },
    power = 800 + level * 75,
    is_undead = True,
    abilities=[abilities.brandish(3)]
)

skeleton_commander = lambda level:Enemy(
    name = "Skeleton Commander",
    level = level,
    stats = {
        "health": 350 + level * 30,
        'max_health': 350 + level * 30,
        'physical_defense': 30 + level * 6,
        'magical_defense': 30 + level * 6,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 60 + level * 12,
        'spell_damage': 60 + level * 12,
        'hit_count': 2,
        'agility': 0.05 + level * 0.005,
        'accuracy': 0.85 + level * 0.01,
        'critical_hit_chance': 0.05 + level * 0.005,
        'action_speed': 10 + level * 0.8
    },
    base_stats={
        'strength': 10 + level * 10 / 6,
        'intelligence': 8 + level * 8 / 6,
        'dexterity': 10 + level * 10 / 6,
        'speed': 3 + level * 3 / 6
    },
    power = 1000 + level * 100,
    is_undead = True,
    abilities=[abilities.brandish(4), abilities.death_stroke(1)]
)

skeleton_lord = lambda level:Enemy(
    name = "Skeleton Lord",
    level = level,
    stats = {
        "health": 300 + level * 30,
        'max_health': 300 + level * 30,
        'physical_defense': 30 + level * 6,
        'magical_defense': 30 + level * 6,
        'mana_points': 10 + level * 2,
        'ability_points': 10 + level * 2,
        'attack_damage': 60 + level * 12,
        'spell_damage': 60 + level * 12,
        'hit_count': 2,
        'agility': 0.05 + level * 0.005,
        'accuracy': 0.85 + level * 0.01,
        'critical_hit_chance': 0.05 + level * 0.005,
        'action_speed': 10 + level * 0.8
    },
    base_stats={
        'strength': 12 + level * 12 / 6,
        'intelligence': 10 + level * 10 / 6,
        'dexterity': 12 + level * 12 / 6,
        'speed': 3 + level * 3 / 6
    },
    power = 1200 + level * 120,
    is_undead = True,
    abilities=[abilities.brandish(5), abilities.death_stroke(2)]
)

necromancer = lambda level: Enemy(
    name = "Necromancer",
    level = level,
    stats = {
        "health": 500 + level * 100,
        'max_health': 500 + level * 100,
        'physical_defense': 50 + level * 10,
        'magical_defense': 50 + level * 10,
        'mana_points': 100 + level * 20,
        'ability_points': 100 + level * 20,
        'attack_damage': 100 + level * 20,
        'spell_damage': 100 + level * 20,
        'hit_count': 2,
        'agility': 0.1 + level * 0.01,
        'accuracy': 0.9 + level * 0.01,
        'critical_hit_chance': 0.1 + level * 0.01,
        'action_speed': 10 + level * 0.8
    },
    base_stats={
        'strength': 20 + level * 20 / 6,
        'intelligence': 20 + level * 20 / 6,
        'dexterity': 20 + level * 20 / 6,
        'speed': 3 + level * 3 / 6
    },
    spells=[
        spells.fireball(1),
        spells.ice_bolt(1),
        spells.lightning_bolt(1)
    ],
    power=2000 + level * 50
)

god_of_chaos = lambda level: Enemy(
    name = "Set, the God of Chaos",
    level = level,
    stats = {
        "health": 1000 + level * 200,
        'max_health': 1000 + level * 200,
        'physical_defense': 100 + level * 20,
        'magical_defense': 100 + level * 20,
        'mana_points': 200 + level * 40,
        'ability_points': 200 + level * 40,
        'attack_damage': 100 + level * 40,
        'spell_damage': 100 + level * 40,
        'hit_count': 1,
        'agility': 0.2 + level * 0.02,
        'accuracy': 0.95 + level * 0.01,
        'critical_hit_chance': 0.2 + level * 0.02,
        'action_speed': 12 + level * 1
    },
    base_stats={
        'strength': 30 + level * 30 / 6,
        'intelligence': 30 + level * 30 / 6,
        'dexterity': 30 + level * 30 / 6,
        'speed': 3 + level * 3 / 6
    },
    abilities=[
        abilities.chaos_blast(1),
        abilities.chaos_wave(1),
        abilities.chaos_storm(1)
    ],
    spells=[
        spells.fireball(1),
        spells.ice_bolt(1),
        spells.lightning_bolt(1)
    ],
    power = 2500 + level * 200
)



ENEMIES: Dict[str, Enemy] = {
    "goblin": goblin,
    "goblin_cleric": goblin_cleric,
    "goblin_warrior": goblin_warrior,
    "goblin_mage": goblin_mage,
    "smiling_goblin": smiling_goblin,
    "goblin_king": goblin_king,
    "orc": orc,
    "orc_shaman": orc_shaman,
    "orc_soldier": orc_soldier,
    "orc_warlock": orc_warlock,
    "orc_chieftain": orc_chieftain,
    "orc_witch_doctor": orc_witch_doctor,
    "orc_berserker": orc_berserker,
    "orc_princess": orc_princess,
    "bandit": bandit,
    "troll": troll,
    "ruffian": ruffian,
    "skeleton": skeleton,
    "skeleton_warrior": skeleton_warrior,
    "skeleton_knight": skeleton_knight,
    "skeleton_mage": skeleton_mage,
    "skeleton_archer": skeleton_archer,
    "skeleton_swordsman": skeleton_swordsman,
    "elite_skeleton": elite_skeleton,
    "skeleton_commander": skeleton_commander,
    "skeleton_lord": skeleton_lord,
    "necromancer": necromancer,
}



def initialize_enemy(enemy_id: str, level: int) -> Enemy:
    pass

def generate_wave_enemies(wave: int) -> list[Enemy]:
    """
    Generate a list of enemies for a given wave number.
    Wave power scaling formula: base_power * (1.2 ^ wave)
    """
    import random
    
    # Base power for wave 1
    base_wave_power = 100
    # Calculate total power budget for this wave
    wave_power = int(base_wave_power * (1.08 ** wave))
    
    # All available enemy types grouped by their relative power
    enemy_tiers = {
        'goblin': [bandit, ruffian, goblin, goblin_cleric, goblin_warrior, goblin_mage, smiling_goblin],  # >0 power
        'orc': [goblin_king, orc, orc_shaman, orc_warlock, orc_chieftain, orc_berserker, orc_princess, troll],  # >140 power
        'skeleton': [skeleton, skeleton_warrior, skeleton_knight, skeleton_mage, skeleton_archer, skeleton_swordsman],  # >350 power
        'elite': [elite_skeleton, skeleton_commander, skeleton_lord, necromancer],  # >800 power
    }
    
    selected_enemies = []
    remaining_power = wave_power
    
    # Keep adding enemies until they can't fit any more within the power budget
    while remaining_power > 50:
        
        if remaining_power >= 1000:
            tier = 'elite'
        elif remaining_power >= 350:
            tier = 'skeleton'
        elif remaining_power >= 140:
            tier = 'orc'
        else:
            tier = 'goblin'
            
        enemy_type = random.choice(enemy_tiers[tier])
        # Enemy level scales with wave. Currently allows to scale infinitely but maybe cap it at some point?
        enemy_level = max(wave // 2, 1)
        enemy = enemy_type(enemy_level)
        
        if enemy.power <= remaining_power:
            selected_enemies.append(enemy)
            remaining_power -= enemy.power
        else:
            # Try a weaker tier if can't fit the current enemy
            continue

    match wave:
        case 1:
            selected_enemies = [goblin(1)]
        case 2:
            selected_enemies = [goblin(1), goblin_cleric(1)]
        case 3:
            selected_enemies = [goblin(1), goblin_mage(1), goblin_warrior(1)]
        case 4:
            selected_enemies = [goblin(1), goblin_cleric(1), goblin_warrior(1), goblin_mage(1)]
        case 5:
            selected_enemies = [bandit(1) for _ in range(10)]
        case 10:
            selected_enemies = [goblin_king(1)]
        case 20:
            selected_enemies = [necromancer]
        
            
    return selected_enemies




