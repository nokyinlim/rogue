from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from uuid import uuid4, UUID

# Equipment Slots
EQUIPMENT_SLOTS = ['head', 'chest', 'feet', 'mainhand', 'offhand', 'twohand', 'accessory']

class StatModifiers(BaseModel):
    health: int = 0
    physical_defense: int = 0
    magical_defense: int = 0
    mana_points: int = 0
    ability_points: int = 0
    attack_damage: int = 0
    spell_damage: int = 0
    hit_count: int = 1
    agility: int = 0
    accuracy: float = 0.0
    critical_hit_chance: float = 0.0
    action_speed: int = 0

class Equipment(BaseModel):
    name: str
    slot: str  # Must be one of EQUIPMENT_SLOTS
    stat_modifiers: StatModifiers

class Spell(BaseModel):
    name: str
    type: str  # e.g., 'damage', 'buff', 'debuff', 'dot'
    cost: int  # Mana points
    effect: Dict[str, Any]  # Defines what the spell does

class Ability(BaseModel):
    name: str
    type: str  # e.g., 'damage', 'buff', 'debuff', 'heal'
    cost: int  # Ability points
    effect: Dict[str, Any]

class Character(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    level: int = 1
    experience: int = 0
    stats: Dict[str, Any]  # Includes all mutable stats
    base_stats: Dict[str, int]  # Strength, Intelligence, Dexterity, Speed
    equipment: Dict[str, Optional[Equipment]] = {slot: None for slot in EQUIPMENT_SLOTS}
    spells: List[Spell] = []
    abilities: List[Ability] = []
    owner_id: UUID

class Enemy(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    level: int
    stats: Dict[str, Any]
    spells: List[Spell] = []
    abilities: List[Ability] = []

class GameState(BaseModel):
    game_id: UUID = Field(default_factory=uuid4)
    player_id: UUID
    characters: List[Character] = []
    enemies: List[Enemy] = []
    wave: int = 1
    turn_order: List[UUID] = []  # Ordered list of character/enemy IDs
    current_turn: int = 0
    status: str = "ongoing"  # could be 'ongoing', 'victory', 'defeat'