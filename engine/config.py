"""
Commit Universe Engine - Configuration
"""

from pathlib import Path

# Paths
UNIVERSE_ROOT = Path(__file__).parent.parent  # Parent of engine/ is the universe root
ENGINE_ROOT = Path(__file__).parent

# Time scaling (commits to cosmic time)
TIME_SCALES = {
    "early_universe": 10_000_000,      # 10 million years per commit (first 1000 commits)
    "galaxy_formation": 1_000_000,      # 1 million years per commit
    "stellar_evolution": 100_000,       # 100k years per commit
    "planetary_development": 10_000,    # 10k years per commit
    "civilization_emergence": 1_000,    # 1k years per commit
    "space_age": 10,                    # 10 years per commit
}

# Event probabilities (base chances, modified by universe state)
EVENT_WEIGHTS = {
    # Cosmic events
    "nebula_form": 0.15,
    "nebula_collapse": 0.10,
    "star_ignite": 0.12,
    "star_evolve": 0.08,
    "supernova": 0.02,
    "black_hole_form": 0.01,
    "galaxy_form": 0.05,
    
    # Planetary events
    "planet_form": 0.10,
    "moon_capture": 0.05,
    "atmosphere_develop": 0.06,
    "ocean_form": 0.04,
    "asteroid_impact": 0.03,
    
    # Life events
    "abiogenesis": 0.005,
    "life_evolve": 0.08,
    "mass_extinction": 0.02,
    "intelligence_emerge": 0.002,
    
    # Civilization events
    "civ_advance": 0.10,
    "civ_discovery": 0.08,
    "civ_expand": 0.05,
    "civ_war": 0.03,
    "civ_peace": 0.04,
    "civ_collapse": 0.01,
    "first_contact": 0.005,
}

# Milestones - minimum commits before certain events can happen
MILESTONES = {
    "galaxy_formation": 50,
    "star_formation": 500,
    "planet_formation": 2000,
    "life_possible": 10000,
    "intelligence_possible": 50000,
    "spacefaring_possible": 75000,
    "interstellar_possible": 150000,
}

# Commit message templates
COMMIT_TYPES = {
    "bang": "bang",
    "form": "form",
    "evolve": "evolve", 
    "event": "event",
    "extinct": "extinct",
    "contact": "contact",
    "colony": "colony",
    "name": "name",
    "lore": "lore",
}

# Star classifications
SPECTRAL_CLASSES = ["O", "B", "A", "F", "G", "K", "M"]
SPECTRAL_WEIGHTS = [0.01, 0.02, 0.05, 0.08, 0.12, 0.20, 0.52]  # M stars most common

# Planet types
PLANET_TYPES = ["terrestrial", "gas_giant", "ice_giant", "dwarf"]
PLANET_WEIGHTS = [0.35, 0.25, 0.20, 0.20]

# Galaxy types
GALAXY_TYPES = ["spiral", "elliptical", "irregular", "lenticular"]
GALAXY_WEIGHTS = [0.60, 0.20, 0.15, 0.05]

# Civilization traits
CIV_TRAITS = [
    "curious", "aggressive", "peaceful", "isolationist",
    "expansionist", "spiritual", "logical", "artistic",
    "long-lived", "short-lived", "hive-mind", "individualist",
    "adaptive", "stubborn", "cooperative", "competitive"
]

# Tech levels
TECH_LEVELS = {
    0: "stone",
    1: "agricultural",
    2: "industrial",
    3: "atomic",
    4: "spacefaring",
    5: "interstellar",
    6: "galactic",
    7: "transcendent"
}
