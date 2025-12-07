"""
Commit Universe Engine

A simulation engine that generates cosmic events and commits them
to the Commit Universe repository.
"""

from .config import UNIVERSE_ROOT, TIME_SCALES, EVENT_WEIGHTS, MILESTONES
from .universe import UniverseReader, UniverseState, Epoch, Galaxy, Star, Planet, Life, Civilization
from .events import EventGenerator, Event, EventType
from .main import CommitUniverse, create_big_bang

__version__ = "0.1.0"

__all__ = [
    # Config
    "UNIVERSE_ROOT",
    "TIME_SCALES",
    "EVENT_WEIGHTS",
    "MILESTONES",

    # Universe state
    "UniverseReader",
    "UniverseState",
    "Epoch",
    "Galaxy",
    "Star",
    "Planet",
    "Life",
    "Civilization",

    # Events
    "EventGenerator",
    "Event",
    "EventType",

    # Main
    "CommitUniverse",
    "create_big_bang",
]
