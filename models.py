from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from uuid import uuid4, UUID

# Equipment Slots
EQUIPMENT_SLOTS: List[str] = ['head', 'chest', 'feet', 'mainhand', 'offhand', 'twohand', 'accessory']

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

class Effect(BaseModel):
    """Defines a single effect that can be part of spells or abilities"""
    type: str  # 'damage', 'heal', 'buff', 'debuff', 'dot' (damage), 'hot' (heal)
    target_stat: Optional[str] = None  # For buffs/debuffs, which stat to modify
    value: float  # Amount of effect (damage, healing, stat change)
    duration: int = 1  # Number of turns effect lasts (1 for instant)
    is_percentage: bool = False  # If True, value is a percentage modifier

class Spell(BaseModel):
    name: str
    description: str = ""
    type: str  # Primary type for identification
    cost: int  # Mana points
    effects: List[Effect]  # Multiple effects possible
    target_type: str = "single"  # 'single', 'self', 'all_enemies', 'all_allies'
    cooldown: int = 0
    current_cooldown: int = 0

class Ability(BaseModel):
    name: str
    description: str = ""
    type: str
    cost: int  # Ability points
    effects: List[Effect]
    target_type: str = "single"
    accuracy_bonus: float = 0.0
    critical_bonus: float = 0.0
    cooldown: int = 0
    current_cooldown: int = 0

class StatusEffect(BaseModel):
    """Tracks active effects on entities. Example: Poison, Stun, etc."""
    name: str
    effect: Effect
    source_id: UUID
    remaining_turns: int

class Character(BaseModel):
    """Represents a player-controlled character.
    Includes all mutable stats, base stats, equipment, spells, abilities, 
    and status effects."""
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
    status_effects: List[StatusEffect] = []
    is_defending: bool = False # Significantly reduces incoming damage
    is_vulnerable: bool = False # Significantly increases incoming damage

class Enemy(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    level: int
    stats: Dict[str, Any]
    spells: List[Spell] = []
    abilities: List[Ability] = []
    status_effects: List[StatusEffect] = []
    is_defending: bool = False
    is_vulnerable: bool = False

class GameState(BaseModel):
    """Represents the current state of a game."""
    game_id: UUID = Field(default_factory=uuid4)
    """Represents the current ID of the GameState."""
    player_id: UUID
    """Player ID associated with the game."""
    characters: List[Character] = []
    """List of player-controlled characters."""
    enemies: List[Enemy] = []
    """List of enemies."""
    wave: int = 1
    """Current wave/level. Scales infinitely and difficulty based off the wave.'"""
    turn_order: List[UUID] = [] 
    """Order in which characters and enemies take"""
    current_turn: int = 0
    """Tracks the current character/enemy turn."""
    status: str = "ongoing"
    """Game status."""