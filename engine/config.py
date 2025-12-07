"""
Commit Universe Engine - Configuration

Contains all constants, stages, and configuration for the simulation.
"""

from pathlib import Path

# Paths
UNIVERSE_ROOT = Path(__file__).parent.parent  # Parent of engine/ is the universe root
ENGINE_ROOT = Path(__file__).parent

# ============ TIME SCALING ============

TIME_SCALES = {
    "early_universe": 10_000_000,      # 10 million years per commit (first 1000 commits)
    "galaxy_formation": 1_000_000,      # 1 million years per commit
    "stellar_evolution": 100_000,       # 100k years per commit
    "planetary_development": 10_000,    # 10k years per commit
    "life_evolution": 1_000,            # 1k years per commit
    "civilization_emergence": 100,      # 100 years per commit
    "space_age": 10,                    # 10 years per commit
    "interstellar_age": 1,              # 1 year per commit
}

# ============ MILESTONES ============

MILESTONES = {
    "galaxy_formation": 50,
    "star_formation": 500,
    "planet_formation": 2000,
    "life_possible": 10000,
    "complex_life_possible": 25000,
    "intelligence_possible": 50000,
    "civilization_possible": 60000,
    "spacefaring_possible": 75000,
    "interstellar_possible": 150000,
}

# ============ ECOSYSTEM STAGES ============

FAUNA_STAGES = [
    "barren",               # 0 - No life possible
    "prebiotic",            # 1 - Organic chemistry, no life yet
    "primordial_soup",      # 2 - Complex molecules, proto-life
    "single_cell",          # 3 - First prokaryotes
    "multicellular_simple", # 4 - Bacterial mats, early multicellular
    "aquatic_primitive",    # 5 - Simple sea life, jellyfish
    "aquatic_complex",      # 6 - Fish, crustaceans, mollusks
    "amphibian",            # 7 - Life moves to land
    "reptilian",            # 8 - Reptiles dominate
    "megafauna",            # 9 - Dinosaur-equivalents
    "mammalian",            # 10 - Mammals rise
    "primate",              # 11 - Complex social animals
    "intelligent",          # 12 - Tool users, pre-civilization
    "civilized",            # 13 - Hands off to civilization system
]

FLORA_STAGES = [
    "none",                 # 0 - No plant life
    "microbial_mats",       # 1 - Bacterial films
    "algae",                # 2 - Simple aquatic plants
    "moss_lichen",          # 3 - First land plants
    "ferns",                # 4 - Primitive vascular plants
    "forests",              # 5 - Trees emerge
    "flowering",            # 6 - Angiosperms, complex ecosystems
    "mega_flora",           # 7 - Giant plant life
]

BIOMES = [
    "ocean_deep",
    "ocean_shallow",
    "coastal",
    "wetland",
    "tropical_forest",
    "temperate_forest",
    "boreal_forest",
    "grassland",
    "savanna",
    "desert_hot",
    "desert_cold",
    "tundra",
    "mountain",
    "volcanic",
    "ice_sheet",
    "underground",
    "floating",  # Gas giant life
]

BIOLOGY_TYPES = [
    "carbon",       # Earth-like
    "silicon",      # High-temp worlds
    "ammonia",      # Cold worlds
    "methane",      # Very cold worlds
    "sulfur",       # Volcanic worlds
    "crystalline",  # Exotic mineral life
    "energy",       # Post-physical
    "machine",      # Artificial life
]

# ============ CIVILIZATION AGES ============

CIV_AGES = [
    "prehistoric",      # 0 - Hunter-gatherers, fire, basic tools
    "tribal",           # 1 - Organized tribes, shamanism, oral tradition
    "bronze",           # 2 - Early metallurgy, first cities, writing
    "iron",             # 3 - Advanced metallurgy, empires, philosophy
    "classical",        # 4 - Golden age of culture, mathematics
    "medieval",         # 5 - Feudalism, organized religion dominates
    "renaissance",      # 6 - Scientific revolution, exploration
    "industrial",       # 7 - Machines, urbanization, nation-states
    "modern",           # 8 - Electricity, global communication
    "atomic",           # 9 - Nuclear power, computing, cold wars
    "information",      # 10 - Digital revolution, global networks
    "space",            # 11 - First spaceflight, orbital presence
    "interplanetary",   # 12 - Colony ships, solar system colonization
    "interstellar",     # 13 - FTL or generation ships, nearby stars
    "galactic",         # 14 - Galaxy-spanning presence
    "transcendent",     # 15 - Post-physical, ascended
]

# Average commits per age (base, modified by events)
AGE_DURATION_COMMITS = {
    "prehistoric": 5000,
    "tribal": 3000,
    "bronze": 2000,
    "iron": 1500,
    "classical": 1000,
    "medieval": 1000,
    "renaissance": 500,
    "industrial": 300,
    "modern": 200,
    "atomic": 150,
    "information": 100,
    "space": 200,
    "interplanetary": 500,
    "interstellar": 1000,
    "galactic": 2000,
    "transcendent": float('inf'),  # End state
}

# ============ GOVERNMENT TYPES ============

GOVERNMENT_TYPES = {
    "prehistoric": ["band", "tribe"],
    "tribal": ["chiefdom", "tribal_council", "elder_rule"],
    "bronze": ["city_state", "early_kingdom", "theocracy", "pharaonic"],
    "iron": ["empire", "republic", "oligarchy", "military_state"],
    "classical": ["democracy", "bureaucratic_empire", "senatorial_republic"],
    "medieval": ["feudalism", "absolute_monarchy", "religious_state", "khanate"],
    "renaissance": ["constitutional_monarchy", "merchant_republic", "colonial_empire"],
    "industrial": ["nation_state", "constitutional_democracy", "communist_state", "fascist_state"],
    "modern": ["liberal_democracy", "authoritarian", "one_party_state", "federal_republic"],
    "atomic": ["superpower_bloc", "military_junta", "technocracy"],
    "information": ["corporate_state", "direct_democracy", "surveillance_state", "cyber_democracy"],
    "space": ["planetary_government", "orbital_corporate", "space_federation"],
    "interplanetary": ["system_federation", "colonial_administration", "corporate_hegemony"],
    "interstellar": ["stellar_empire", "confederation", "trade_league", "hive_consensus"],
    "galactic": ["galactic_council", "galactic_empire", "transcendent_collective"],
    "transcendent": ["post_physical", "unity_consciousness", "unknown"],
}

# ============ RELIGION TYPES ============

RELIGION_TYPES = [
    "animistic",        # Nature spirits
    "ancestor_worship", # Veneration of ancestors
    "polytheistic",     # Many gods
    "monotheistic",     # One god
    "dualistic",        # Two opposing forces
    "philosophical",    # Ethics-based, non-theistic
    "cosmic",           # Worship of cosmic forces
    "machine_cult",     # Technology worship
    "transcendent",     # Post-physical spirituality
]

# ============ TECHNOLOGY CATEGORIES ============

TECH_CATEGORIES = {
    "survival": [
        "fire", "stone_tools", "clothing", "shelter", "agriculture",
        "animal_husbandry", "medicine_basic", "food_preservation"
    ],
    "materials": [
        "bronze_working", "iron_working", "steel", "alloys",
        "plastics", "composites", "nanomaterials", "exotic_matter"
    ],
    "energy": [
        "muscle_power", "wind_power", "water_power", "steam",
        "electricity", "petroleum", "nuclear_fission", "nuclear_fusion",
        "antimatter", "zero_point", "stellar_harvesting"
    ],
    "information": [
        "writing", "printing", "telegraph", "radio", "television",
        "computers", "internet", "quantum_computing", "neural_interface"
    ],
    "transport": [
        "wheel", "sail", "steam_engine", "internal_combustion",
        "jet_propulsion", "rockets", "ion_drives", "ftl_drive", "wormhole_tech"
    ],
    "weapons": [
        "spears", "bows", "swords", "gunpowder", "firearms",
        "artillery", "nuclear_weapons", "directed_energy", "planet_crackers"
    ],
    "biology": [
        "selective_breeding", "germ_theory", "vaccines", "antibiotics",
        "genetics", "cloning", "gene_editing", "immortality_treatments", "uplift"
    ],
    "space": [
        "astronomy", "rocketry", "satellites", "space_stations",
        "moon_landing", "mars_colonization", "asteroid_mining",
        "terraforming", "dyson_structures"
    ],
}

# ============ CULTURE TRAITS ============

CULTURE_TRAITS = [
    # Values
    "honor_bound", "knowledge_seeking", "tradition_focused", "progress_oriented",
    "individualistic", "collectivist", "martial", "peaceful",
    "spiritual", "materialistic", "hierarchical", "egalitarian",

    # Artistic
    "musical", "architectural", "literary", "visual_arts",
    "performative", "sculptural", "culinary", "textile",

    # Social
    "hospitable", "xenophobic", "mercantile", "isolationist",
    "expansionist", "diplomatic", "secretive", "open",
]

# ============ CIVILIZATION TRAITS ============

CIV_TRAITS = [
    "curious", "aggressive", "peaceful", "isolationist",
    "expansionist", "spiritual", "logical", "artistic",
    "long_lived", "short_lived", "hive_mind", "individualist",
    "adaptive", "stubborn", "cooperative", "competitive",
    "honor_bound", "pragmatic", "romantic", "stoic",
    "nomadic", "sedentary", "aquatic", "subterranean",
]

# ============ STAR & PLANET TYPES ============

SPECTRAL_CLASSES = ["O", "B", "A", "F", "G", "K", "M"]
SPECTRAL_WEIGHTS = [0.01, 0.02, 0.05, 0.08, 0.12, 0.20, 0.52]

PLANET_TYPES = ["terrestrial", "gas_giant", "ice_giant", "dwarf", "ocean_world", "desert_world", "ice_world"]
PLANET_WEIGHTS = [0.30, 0.20, 0.15, 0.15, 0.08, 0.07, 0.05]

GALAXY_TYPES = ["spiral", "elliptical", "irregular", "lenticular"]
GALAXY_WEIGHTS = [0.60, 0.20, 0.15, 0.05]

# ============ EVENT WEIGHTS ============

EVENT_WEIGHTS = {
    # Cosmic events
    "galaxy_form": 0.05,
    "star_form": 0.12,
    "star_evolve": 0.08,
    "supernova": 0.02,
    "black_hole_form": 0.01,

    # Planetary events
    "planet_form": 0.10,
    "moon_form": 0.05,
    "atmosphere_form": 0.06,
    "ocean_form": 0.04,
    "asteroid_impact": 0.03,

    # Ecosystem events
    "life_spark": 0.005,
    "evolution_leap": 0.08,
    "species_emerge": 0.06,
    "mass_extinction": 0.02,
    "flora_bloom": 0.05,

    # Civilization internal events
    "civ_emerge": 0.003,
    "age_advance": 0.10,
    "religion_emerge": 0.04,
    "religion_schism": 0.02,
    "culture_emerge": 0.03,
    "government_change": 0.03,
    "civil_war": 0.02,
    "golden_age": 0.02,
    "dark_age": 0.01,
    "great_leader": 0.03,
    "plague": 0.01,
    "tech_discovery": 0.08,
    "migration": 0.03,

    # Civilization external events
    "first_contact": 0.005,
    "establish_trade": 0.04,
    "alliance_form": 0.03,
    "war_declare": 0.02,
    "war_battle": 0.04,
    "war_end": 0.03,
    "conquest": 0.01,
    "cultural_exchange": 0.04,

    # Special events
    "anomaly": 0.005,
    "ruins_discovered": 0.01,
}

# ============ COMMIT MESSAGE TYPES ============

COMMIT_TYPES = {
    "bang": "bang",         # Universe-level events
    "form": "form",         # Something created
    "evolve": "evolve",     # Something changes/advances
    "event": "event",       # Something happens
    "extinct": "extinct",   # Something ends
    "contact": "contact",   # Civilizations interact
    "colony": "colony",     # Expansion events
    "name": "name",         # Something gets named
    "lore": "lore",         # Chronicle/history addition
    "war": "war",           # Conflict events
    "peace": "peace",       # Peace/treaty events
    "discover": "discover", # Discovery events
    "crisis": "crisis",     # Crisis events
}

# ============ LEGACY COMPATIBILITY ============

# Old tech levels mapping to new ages
TECH_LEVELS = {
    0: "prehistoric",
    1: "tribal",
    2: "bronze",
    3: "iron",
    4: "classical",
    5: "medieval",
    6: "renaissance",
    7: "industrial",
    8: "modern",
    9: "atomic",
    10: "information",
    11: "space",
    12: "interplanetary",
    13: "interstellar",
    14: "galactic",
    15: "transcendent",
}
