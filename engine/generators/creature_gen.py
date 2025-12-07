"""
Commit Universe - Creature and Flora Generator

Generates procedural creatures and plants based on planetary conditions.
Considers:
- Gravity (affects size)
- Atmosphere (affects respiration)
- Star type (affects vision/coloration)
- Temperature (affects metabolism)
- Water availability (affects biology)
- Biology type (carbon, silicon, ammonia, etc.)
"""

import random
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum

from .name_gen import generate_creature_name, generate_flora_name, LanguageFamily


class BiologyType(Enum):
    """Base chemistry for life"""
    CARBON = "carbon"           # Earth-like
    SILICON = "silicon"         # High-temp worlds
    AMMONIA = "ammonia"         # Cold worlds
    METHANE = "methane"         # Very cold worlds
    SULFUR = "sulfur"           # Volcanic worlds
    CRYSTALLINE = "crystalline" # Exotic mineral life
    ENERGY = "energy"           # Post-physical/exotic
    MACHINE = "machine"         # Artificial life


class CreatureCategory(Enum):
    """Major creature categories"""
    MICROBE = "microbe"
    AQUATIC = "aquatic"
    AMPHIBIAN = "amphibian"
    TERRESTRIAL = "terrestrial"
    AERIAL = "aerial"
    SUBTERRANEAN = "subterranean"


class CreatureRole(Enum):
    """Ecological role"""
    PRODUCER = "producer"           # Autotroph (like plants but animal-ish)
    DECOMPOSER = "decomposer"
    FILTER_FEEDER = "filter_feeder"
    HERBIVORE = "herbivore"
    OMNIVORE = "omnivore"
    CARNIVORE = "carnivore"
    APEX_PREDATOR = "apex_predator"
    PARASITE = "parasite"
    SYMBIONT = "symbiont"


class SizeClass(Enum):
    """Size classification"""
    MICROSCOPIC = "microscopic"
    TINY = "tiny"               # Insect-sized
    SMALL = "small"             # Cat-sized
    MEDIUM = "medium"           # Dog/human-sized
    LARGE = "large"             # Horse/cow-sized
    HUGE = "huge"               # Elephant-sized
    GIGANTIC = "gigantic"       # Whale/dinosaur-sized
    COLOSSAL = "colossal"       # Kaiju-sized


class IntelligenceLevel(Enum):
    """Cognitive capability"""
    NONE = "none"               # Reactive only
    PRIMITIVE = "primitive"     # Basic instincts
    SIMPLE = "simple"           # Learning capability
    MODERATE = "moderate"       # Tool curiosity
    HIGH = "high"               # Problem solving
    SAPIENT = "sapient"         # Self-aware, culture
    TRANSCENDENT = "transcendent"


# Trait pools by category
LOCOMOTION_TRAITS = {
    CreatureCategory.AQUATIC: ["swimming", "jet_propulsion", "undulating", "crawling_seabed", "floating"],
    CreatureCategory.AMPHIBIAN: ["swimming", "hopping", "crawling", "walking"],
    CreatureCategory.TERRESTRIAL: ["walking", "running", "hopping", "slithering", "rolling", "burrowing"],
    CreatureCategory.AERIAL: ["flying", "gliding", "hovering", "soaring"],
    CreatureCategory.SUBTERRANEAN: ["burrowing", "crawling", "slithering"],
    CreatureCategory.MICROBE: ["flagella", "cilia", "amoeboid", "passive"],
}

BODY_PLANS = {
    CreatureCategory.AQUATIC: ["fish-like", "cephalopod", "crustacean", "jellyfish", "eel-like", "ray-like", "blob"],
    CreatureCategory.AMPHIBIAN: ["frog-like", "salamander-like", "mudskipper-like"],
    CreatureCategory.TERRESTRIAL: ["quadruped", "biped", "hexapod", "octopod", "serpentine", "centipede-like", "arachnid"],
    CreatureCategory.AERIAL: ["bird-like", "bat-like", "insectoid", "balloon", "ray-like"],
    CreatureCategory.SUBTERRANEAN: ["worm-like", "mole-like", "serpentine", "blob"],
    CreatureCategory.MICROBE: ["spherical", "rod", "spiral", "filament", "amoeboid"],
}

SENSORY_ADAPTATIONS = [
    "compound_eyes", "thermal_vision", "echolocation", "electroreception",
    "magnetic_sense", "chemical_sense", "pressure_sense", "tremorsense",
    "infrared_vision", "ultraviolet_vision", "radio_sense", "quantum_sense",
    "photosensitive_skin", "antenna", "whiskers", "lateral_line"
]

DEFENSIVE_ADAPTATIONS = [
    "armor_plates", "spines", "venom", "camouflage", "mimicry",
    "regeneration", "toxic_skin", "electric_shock", "ink_cloud",
    "decoy_limbs", "burrowing", "speed", "herd_behavior",
    "warning_coloration", "shell", "thick_hide", "size"
]

OFFENSIVE_ADAPTATIONS = [
    "claws", "fangs", "venom", "horns", "tusks",
    "crushing_jaws", "tentacles", "projectile_spit", "electric_shock",
    "ambush_hunting", "pack_hunting", "constriction", "sonic_attack",
    "acid_spray", "fire_breath", "ice_breath"
]

SPECIAL_TRAITS = [
    "bioluminescence", "chromatophores", "pheromone_communication",
    "hive_mind", "symbiotic_relationship", "metamorphosis",
    "extreme_longevity", "rapid_reproduction", "asexual_reproduction",
    "photosynthetic", "radiation_resistant", "pressure_resistant",
    "temperature_extremophile", "dormancy", "migration_instinct"
]

# Colors based on star type and environment
COLOR_PALETTES = {
    "red_star": ["deep_red", "maroon", "black", "gray", "infrared_patterns"],
    "orange_star": ["orange", "red", "brown", "amber", "rust"],
    "yellow_star": ["green", "brown", "blue", "yellow", "varied"],
    "blue_star": ["white", "silver", "pale_blue", "black", "ultraviolet_patterns"],
    "ocean": ["blue", "silver", "translucent", "bioluminescent", "dark"],
    "desert": ["tan", "brown", "sand", "ochre", "white"],
    "forest": ["green", "brown", "spotted", "striped", "camouflage"],
    "volcanic": ["black", "red", "orange", "gray", "obsidian"],
    "ice": ["white", "pale_blue", "translucent", "silver"],
}


@dataclass
class Creature:
    """A generated creature"""
    id: str
    common_name: str
    scientific_name: str
    category: CreatureCategory
    role: CreatureRole
    size_class: SizeClass
    intelligence: IntelligenceLevel

    # Physical
    body_plan: str
    locomotion: str
    limb_count: int
    has_tail: bool
    has_wings: bool
    coloration: List[str]

    # Traits
    sensory_adaptations: List[str]
    defensive_adaptations: List[str]
    offensive_adaptations: List[str]
    special_traits: List[str]

    # Biology
    biology_type: BiologyType
    respiration: str
    diet: str
    lifespan_years: float
    reproduction: str

    # Ecology
    habitat: str
    population_status: str
    discovered_at_commit: int

    # Optional
    description: str = ""


@dataclass
class Flora:
    """A generated plant/flora"""
    id: str
    common_name: str
    scientific_name: str

    # Physical
    growth_form: str  # tree, shrub, vine, grass, etc.
    height_meters: float
    coloration: List[str]

    # Biology
    biology_type: BiologyType
    photosynthesis_type: str
    reproduction: str
    lifespan_years: float

    # Ecology
    habitat: str
    coverage: str  # rare, common, dominant
    discovered_at_commit: int

    # Special
    special_traits: List[str]
    description: str = ""


def determine_biology_type(planet_data: dict) -> BiologyType:
    """Determine what kind of biochemistry based on planet conditions"""
    temp = planet_data.get("avg_temp_kelvin", 288)
    atmosphere = planet_data.get("atmosphere_composition", {})

    # Very hot worlds
    if temp > 400:
        if random.random() < 0.6:
            return BiologyType.SILICON
        else:
            return BiologyType.SULFUR

    # Very cold worlds
    if temp < 200:
        if atmosphere.get("ammonia", 0) > 0.1:
            return BiologyType.AMMONIA
        elif atmosphere.get("methane", 0) > 0.1:
            return BiologyType.METHANE
        else:
            return BiologyType.CARBON  # Cold carbon life

    # Earth-like range
    return BiologyType.CARBON


def determine_size_range(gravity: float, category: CreatureCategory) -> List[SizeClass]:
    """Determine possible size classes based on gravity"""
    # Higher gravity = smaller creatures
    if gravity > 2.0:
        return [SizeClass.MICROSCOPIC, SizeClass.TINY, SizeClass.SMALL]
    elif gravity > 1.5:
        return [SizeClass.TINY, SizeClass.SMALL, SizeClass.MEDIUM]
    elif gravity > 0.8:
        return [SizeClass.TINY, SizeClass.SMALL, SizeClass.MEDIUM, SizeClass.LARGE, SizeClass.HUGE]
    elif gravity > 0.3:
        return [SizeClass.SMALL, SizeClass.MEDIUM, SizeClass.LARGE, SizeClass.HUGE, SizeClass.GIGANTIC]
    else:  # Low gravity
        return [SizeClass.MEDIUM, SizeClass.LARGE, SizeClass.HUGE, SizeClass.GIGANTIC, SizeClass.COLOSSAL]


def determine_respiration(atmosphere: dict, biology: BiologyType) -> str:
    """Determine how the creature breathes"""
    if biology == BiologyType.MACHINE:
        return "none"
    elif biology == BiologyType.ENERGY:
        return "energy_absorption"

    # Check atmosphere
    if atmosphere.get("oxygen", 0) > 0.15:
        return "oxygen"
    elif atmosphere.get("carbon_dioxide", 0) > 0.5:
        return "carbon_dioxide"
    elif atmosphere.get("methane", 0) > 0.3:
        return "methane"
    elif atmosphere.get("ammonia", 0) > 0.2:
        return "ammonia"
    elif atmosphere.get("hydrogen", 0) > 0.3:
        return "hydrogen"
    elif atmosphere.get("sulfur_dioxide", 0) > 0.1:
        return "sulfur_compounds"
    else:
        return "anaerobic"


def generate_creature(
    planet_data: dict,
    category: Optional[CreatureCategory] = None,
    role: Optional[CreatureRole] = None,
    language_family: Optional[LanguageFamily] = None,
    creature_id: str = "",
    discovered_at_commit: int = 0
) -> Creature:
    """Generate a creature based on planetary conditions"""

    # Determine biology type
    biology = determine_biology_type(planet_data)

    # Pick category if not specified
    if category is None:
        has_water = planet_data.get("has_water", False)
        has_land = planet_data.get("has_land", True)

        available = []
        if has_water:
            available.extend([CreatureCategory.AQUATIC, CreatureCategory.AMPHIBIAN])
        if has_land:
            available.extend([CreatureCategory.TERRESTRIAL, CreatureCategory.AERIAL, CreatureCategory.SUBTERRANEAN])
        if not available:
            available = [CreatureCategory.MICROBE]

        category = random.choice(available)

    # Pick role if not specified
    if role is None:
        role = random.choice(list(CreatureRole))

    # Determine size based on gravity
    gravity = planet_data.get("gravity", 1.0)
    possible_sizes = determine_size_range(gravity, category)
    size = random.choice(possible_sizes)

    # Body plan
    body_plan = random.choice(BODY_PLANS.get(category, ["amorphous"]))
    locomotion = random.choice(LOCOMOTION_TRAITS.get(category, ["unknown"]))

    # Limbs
    if body_plan in ["serpentine", "worm-like", "blob", "jellyfish"]:
        limb_count = 0
    elif body_plan in ["biped", "bird-like"]:
        limb_count = 2
    elif body_plan in ["quadruped", "frog-like", "salamander-like"]:
        limb_count = 4
    elif body_plan in ["hexapod", "insectoid"]:
        limb_count = 6
    elif body_plan in ["octopod", "arachnid", "cephalopod"]:
        limb_count = 8
    elif body_plan in ["centipede-like"]:
        limb_count = random.choice([20, 40, 100])
    else:
        limb_count = random.choice([0, 2, 4, 6, 8])

    has_tail = random.random() < 0.6 and limb_count > 0
    has_wings = category == CreatureCategory.AERIAL or (random.random() < 0.1 and category == CreatureCategory.TERRESTRIAL)

    # Coloration based on star type and habitat
    star_type = planet_data.get("star_spectral_class", "G")
    if star_type in ["M", "K"]:
        palette_key = "red_star"
    elif star_type in ["F", "G"]:
        palette_key = "yellow_star"
    elif star_type in ["A", "B", "O"]:
        palette_key = "blue_star"
    else:
        palette_key = "yellow_star"

    base_colors = COLOR_PALETTES.get(palette_key, ["varied"])
    coloration = random.sample(base_colors, min(2, len(base_colors)))

    # Traits
    sensory = random.sample(SENSORY_ADAPTATIONS, random.randint(1, 3))
    defensive = random.sample(DEFENSIVE_ADAPTATIONS, random.randint(1, 3)) if role != CreatureRole.APEX_PREDATOR else random.sample(DEFENSIVE_ADAPTATIONS, random.randint(0, 1))
    offensive = random.sample(OFFENSIVE_ADAPTATIONS, random.randint(1, 3)) if role in [CreatureRole.CARNIVORE, CreatureRole.APEX_PREDATOR, CreatureRole.OMNIVORE] else []
    special = random.sample(SPECIAL_TRAITS, random.randint(0, 2))

    # Respiration
    atmosphere = planet_data.get("atmosphere_composition", {"oxygen": 0.21})
    respiration = determine_respiration(atmosphere, biology)

    # Diet based on role
    diet_map = {
        CreatureRole.PRODUCER: "autotroph",
        CreatureRole.DECOMPOSER: "detritivore",
        CreatureRole.FILTER_FEEDER: "filter_feeder",
        CreatureRole.HERBIVORE: "herbivore",
        CreatureRole.OMNIVORE: "omnivore",
        CreatureRole.CARNIVORE: "carnivore",
        CreatureRole.APEX_PREDATOR: "hypercarnivore",
        CreatureRole.PARASITE: "parasitic",
        CreatureRole.SYMBIONT: "symbiotic",
    }
    diet = diet_map.get(role, "omnivore")

    # Lifespan - size and metabolism matter
    base_lifespan = {
        SizeClass.MICROSCOPIC: 0.01,
        SizeClass.TINY: 1,
        SizeClass.SMALL: 5,
        SizeClass.MEDIUM: 20,
        SizeClass.LARGE: 40,
        SizeClass.HUGE: 80,
        SizeClass.GIGANTIC: 150,
        SizeClass.COLOSSAL: 300,
    }
    lifespan = base_lifespan.get(size, 20) * random.uniform(0.5, 2.0)

    # Reproduction
    if size in [SizeClass.MICROSCOPIC, SizeClass.TINY]:
        reproduction = random.choice(["binary_fission", "budding", "spores", "eggs_many"])
    else:
        reproduction = random.choice(["eggs_few", "eggs_many", "live_birth", "pouched", "larval_stage"])

    # Intelligence - apex predators and larger creatures tend to be smarter
    if role == CreatureRole.APEX_PREDATOR and size in [SizeClass.LARGE, SizeClass.HUGE]:
        intelligence = random.choice([IntelligenceLevel.MODERATE, IntelligenceLevel.HIGH, IntelligenceLevel.SIMPLE])
    elif size in [SizeClass.MICROSCOPIC, SizeClass.TINY]:
        intelligence = random.choice([IntelligenceLevel.NONE, IntelligenceLevel.PRIMITIVE])
    else:
        intelligence = random.choice([IntelligenceLevel.PRIMITIVE, IntelligenceLevel.SIMPLE, IntelligenceLevel.MODERATE])

    # Names
    common_name = generate_creature_name(language_family)
    scientific_name = generate_creature_name(scientific=True)

    # Habitat
    habitat_map = {
        CreatureCategory.AQUATIC: random.choice(["ocean_deep", "ocean_shallow", "coastal", "freshwater", "tidal"]),
        CreatureCategory.AMPHIBIAN: random.choice(["wetland", "coastal", "swamp", "riverbank"]),
        CreatureCategory.TERRESTRIAL: random.choice(["grassland", "forest", "desert", "mountain", "tundra"]),
        CreatureCategory.AERIAL: random.choice(["sky", "forest_canopy", "cliffs", "mountains"]),
        CreatureCategory.SUBTERRANEAN: random.choice(["caves", "burrows", "underground_rivers"]),
        CreatureCategory.MICROBE: random.choice(["everywhere", "water", "soil", "hosts"]),
    }
    habitat = habitat_map.get(category, "varied")

    population_status = random.choice(["abundant", "common", "uncommon", "rare", "endangered", "critically_endangered"])

    # Generate description
    description = _generate_creature_description(
        common_name, size, body_plan, locomotion, coloration, role, special
    )

    return Creature(
        id=creature_id or f"creature-{random.randint(1000, 9999)}",
        common_name=common_name,
        scientific_name=scientific_name,
        category=category,
        role=role,
        size_class=size,
        intelligence=intelligence,
        body_plan=body_plan,
        locomotion=locomotion,
        limb_count=limb_count,
        has_tail=has_tail,
        has_wings=has_wings,
        coloration=coloration,
        sensory_adaptations=sensory,
        defensive_adaptations=defensive,
        offensive_adaptations=offensive,
        special_traits=special,
        biology_type=biology,
        respiration=respiration,
        diet=diet,
        lifespan_years=lifespan,
        reproduction=reproduction,
        habitat=habitat,
        population_status=population_status,
        discovered_at_commit=discovered_at_commit,
        description=description,
    )


def _generate_creature_description(
    name: str, size: SizeClass, body_plan: str,
    locomotion: str, coloration: List[str],
    role: CreatureRole, special: List[str]
) -> str:
    """Generate a prose description of the creature"""
    size_words = {
        SizeClass.MICROSCOPIC: "microscopic",
        SizeClass.TINY: "tiny",
        SizeClass.SMALL: "small",
        SizeClass.MEDIUM: "medium-sized",
        SizeClass.LARGE: "large",
        SizeClass.HUGE: "massive",
        SizeClass.GIGANTIC: "gigantic",
        SizeClass.COLOSSAL: "colossal",
    }

    color_str = " and ".join(coloration) if coloration else "mottled"
    size_str = size_words.get(size, "medium-sized")

    desc = f"The {name} is a {size_str}, {color_str} creature with a {body_plan} body plan. "
    desc += f"It moves by {locomotion.replace('_', ' ')}. "

    if role == CreatureRole.APEX_PREDATOR:
        desc += "As an apex predator, it sits at the top of its ecosystem's food chain. "
    elif role == CreatureRole.HERBIVORE:
        desc += "It feeds primarily on plant matter. "
    elif role == CreatureRole.CARNIVORE:
        desc += "It hunts other creatures for sustenance. "

    if special:
        special_str = ", ".join([s.replace("_", " ") for s in special])
        desc += f"Notable traits include {special_str}."

    return desc


def generate_apex_predator(
    planet_data: dict,
    language_family: Optional[LanguageFamily] = None,
    creature_id: str = "",
    discovered_at_commit: int = 0
) -> Creature:
    """Generate an apex predator for a planet"""
    return generate_creature(
        planet_data=planet_data,
        role=CreatureRole.APEX_PREDATOR,
        language_family=language_family,
        creature_id=creature_id,
        discovered_at_commit=discovered_at_commit
    )


def generate_flora(
    planet_data: dict,
    language_family: Optional[LanguageFamily] = None,
    flora_id: str = "",
    discovered_at_commit: int = 0
) -> Flora:
    """Generate a plant/flora based on planetary conditions"""

    biology = determine_biology_type(planet_data)

    # Growth forms
    growth_forms = ["tree", "shrub", "vine", "grass", "fern", "moss", "fungus",
                    "algae", "kelp", "succulent", "flowering_plant", "crystal_growth"]

    if biology == BiologyType.CRYSTALLINE:
        growth_form = random.choice(["crystal_growth", "mineral_formation", "lattice_structure"])
    elif biology in [BiologyType.SILICON, BiologyType.SULFUR]:
        growth_form = random.choice(["silicon_tree", "mineral_bush", "crystal_grass", "sulfur_bloom"])
    else:
        growth_form = random.choice(growth_forms)

    # Height based on gravity
    gravity = planet_data.get("gravity", 1.0)
    if gravity > 1.5:
        height = random.uniform(0.1, 5)
    elif gravity > 0.8:
        height = random.uniform(0.5, 50)
    else:  # Low gravity = tall plants
        height = random.uniform(1, 200)

    # Coloration
    star_type = planet_data.get("star_spectral_class", "G")
    if star_type in ["M", "K"]:
        # Red star = black/red plants (absorb all light)
        coloration = random.sample(["black", "dark_red", "deep_purple", "maroon"], 2)
    elif star_type in ["F", "G"]:
        coloration = random.sample(["green", "blue-green", "yellow-green", "olive"], 2)
    elif star_type in ["A", "B", "O"]:
        coloration = random.sample(["pale_green", "white", "silver", "blue"], 2)
    else:
        coloration = ["green", "brown"]

    # Photosynthesis type
    atmosphere = planet_data.get("atmosphere_composition", {})
    if atmosphere.get("carbon_dioxide", 0) > 0.5:
        photosynthesis = "enhanced_carbon_fixation"
    elif biology == BiologyType.SILICON:
        photosynthesis = "silicon_based"
    elif biology == BiologyType.CRYSTALLINE:
        photosynthesis = "piezoelectric"
    else:
        photosynthesis = random.choice(["oxygenic", "anoxygenic", "chemosynthesis"])

    # Reproduction
    reproduction = random.choice(["spores", "seeds", "runners", "budding", "fragmentation", "flowering"])

    # Lifespan
    if growth_form in ["tree", "kelp"]:
        lifespan = random.uniform(100, 5000)
    elif growth_form in ["shrub", "fern"]:
        lifespan = random.uniform(10, 100)
    else:
        lifespan = random.uniform(1, 20)

    # Habitat
    habitat = random.choice(["forest", "grassland", "wetland", "desert", "tundra",
                             "coastal", "mountain", "volcanic", "aquatic"])

    coverage = random.choice(["rare", "uncommon", "common", "abundant", "dominant"])

    # Special traits
    flora_traits = [
        "bioluminescent", "carnivorous", "mobile_roots", "explosive_seeds",
        "symbiotic_with_fauna", "medicinal", "toxic", "psychoactive",
        "nitrogen_fixing", "drought_resistant", "fire_adapted", "parasitic"
    ]
    special = random.sample(flora_traits, random.randint(0, 2))

    # Names
    common_name = generate_flora_name(language_family)
    scientific_name = generate_flora_name(scientific=True)

    # Description
    color_str = " and ".join(coloration)
    description = f"The {common_name} is a {growth_form} that grows up to {height:.1f} meters tall. "
    description += f"Its {color_str} coloration helps it absorb light from its star. "
    if special:
        description += f"It is known for being {', '.join(special).replace('_', ' ')}."

    return Flora(
        id=flora_id or f"flora-{random.randint(1000, 9999)}",
        common_name=common_name,
        scientific_name=scientific_name,
        growth_form=growth_form,
        height_meters=height,
        coloration=coloration,
        biology_type=biology,
        photosynthesis_type=photosynthesis,
        reproduction=reproduction,
        lifespan_years=lifespan,
        habitat=habitat,
        coverage=coverage,
        discovered_at_commit=discovered_at_commit,
        special_traits=special,
        description=description,
    )


def generate_ecosystem_creatures(
    planet_data: dict,
    fauna_stage: str,
    language_family: Optional[LanguageFamily] = None,
    discovered_at_commit: int = 0
) -> List[Creature]:
    """Generate a set of creatures appropriate for the planet's evolutionary stage"""

    creatures = []

    # How many creatures based on stage
    stage_counts = {
        "single_cell": 1,
        "multicellular_simple": 2,
        "aquatic_primitive": 3,
        "aquatic_complex": 5,
        "amphibian": 6,
        "reptilian": 8,
        "megafauna": 10,
        "mammalian": 12,
        "primate": 15,
        "intelligent": 15,
    }

    count = stage_counts.get(fauna_stage, 5)

    # Generate appropriate creatures
    for i in range(count):
        creature = generate_creature(
            planet_data=planet_data,
            language_family=language_family,
            creature_id=f"creature-{i+1:04d}",
            discovered_at_commit=discovered_at_commit
        )
        creatures.append(creature)

    return creatures


# Export
__all__ = [
    "BiologyType",
    "CreatureCategory",
    "CreatureRole",
    "SizeClass",
    "IntelligenceLevel",
    "Creature",
    "Flora",
    "generate_creature",
    "generate_apex_predator",
    "generate_flora",
    "generate_ecosystem_creatures",
    "determine_biology_type",
]
