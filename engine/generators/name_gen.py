"""
Commit Universe - Procedural Name Generator

Generates pronounceable, interesting names for:
- Stars, planets, moons
- Civilizations and species
- Religions and cultures
- Creatures and flora
- Leaders and historical figures
- Cities and settlements

Uses linguistic syllable patterns with multiple "language families"
so each civilization has a consistent naming style.
"""

import random
from typing import List, Optional, Tuple
from enum import Enum


class LanguageFamily(Enum):
    """Different linguistic styles for different civilizations"""
    MELODIC = "melodic"          # Soft, flowing (elvish-like)
    HARSH = "harsh"              # Hard consonants, guttural
    ANCIENT = "ancient"          # Latin/Greek inspired
    FLOWING = "flowing"          # Polynesian/Japanese inspired
    CLICKING = "clicking"        # African click-language inspired
    CRYSTALLINE = "crystalline"  # Sharp, geometric sounds
    DEEP = "deep"                # Low, rumbling sounds
    WHISPERED = "whispered"      # Soft, breathy
    MECHANICAL = "mechanical"    # For machine civilizations
    COSMIC = "cosmic"            # Otherworldly, transcendent


# Phoneme sets for each language family
PHONEMES = {
    LanguageFamily.MELODIC: {
        "consonants": ["l", "r", "n", "m", "v", "th", "s", "f", "w", "y"],
        "vowels": ["a", "e", "i", "o", "u", "ae", "ia", "ea", "io"],
        "endings": ["iel", "wen", "ara", "ien", "oth", "iel", "ana", "ora"],
        "prefixes": ["El", "Ar", "Lor", "Mir", "Sil", "Cel", "Aer", "Val"],
    },
    LanguageFamily.HARSH: {
        "consonants": ["k", "g", "kr", "gr", "th", "z", "v", "dr", "tr", "kh", "gh"],
        "vowels": ["a", "o", "u", "aa", "uu", "ai"],
        "endings": ["rak", "goth", "zul", "khar", "gor", "mok", "drak", "thul"],
        "prefixes": ["Kra", "Gro", "Zar", "Mor", "Dra", "Gor", "Vok", "Thro"],
    },
    LanguageFamily.ANCIENT: {
        "consonants": ["t", "s", "n", "r", "l", "m", "p", "c", "d", "x"],
        "vowels": ["a", "e", "i", "o", "u", "ae", "ei", "au"],
        "endings": ["us", "um", "is", "ax", "on", "or", "ix", "es", "ius"],
        "prefixes": ["Ael", "Pro", "Max", "Sol", "Lux", "Rex", "Vex", "Nox"],
    },
    LanguageFamily.FLOWING: {
        "consonants": ["k", "t", "n", "m", "r", "h", "w", "y", "s"],
        "vowels": ["a", "i", "o", "u", "ai", "ao", "ou", "ei", "oa"],
        "endings": ["nui", "kai", "loa", "ani", "iki", "ono", "ara", "ura"],
        "prefixes": ["Ka", "Mo", "Ta", "Ni", "Ha", "Ri", "Ao", "Io"],
    },
    LanguageFamily.CLICKING: {
        "consonants": ["k", "t", "x", "q", "n", "m", "b", "d", "ng"],
        "vowels": ["a", "e", "i", "o", "u"],
        "endings": ["iki", "aba", "ongo", "eke", "ulu", "ana", "obo"],
        "prefixes": ["Nko", "Xho", "Qua", "Tik", "Mba", "Ngu", "Kwe"],
    },
    LanguageFamily.CRYSTALLINE: {
        "consonants": ["z", "x", "k", "t", "s", "kr", "st", "sk", "tz"],
        "vowels": ["i", "y", "e", "a", "ai", "ei"],
        "endings": ["zyx", "rix", "tek", "kis", "zar", "xis", "kri", "zel"],
        "prefixes": ["Zy", "Kri", "Xen", "Sty", "Tze", "Sky", "Zei", "Kry"],
    },
    LanguageFamily.DEEP: {
        "consonants": ["b", "d", "g", "m", "n", "r", "v", "th", "dh"],
        "vowels": ["o", "u", "a", "oo", "au", "ou"],
        "endings": ["oom", "und", "gor", "moth", "bur", "dun", "rom", "thum"],
        "prefixes": ["Bor", "Dum", "Gro", "Mur", "Rum", "Thun", "Vor", "Dro"],
    },
    LanguageFamily.WHISPERED: {
        "consonants": ["sh", "h", "s", "f", "th", "wh", "ph", "v"],
        "vowels": ["a", "e", "i", "u", "ae", "ai", "ei"],
        "endings": ["sha", "eth", "ith", "pha", "sai", "hei", "ven", "esh"],
        "prefixes": ["Sha", "Whi", "Fae", "Hei", "Pha", "Sai", "Vei", "Ash"],
    },
    LanguageFamily.MECHANICAL: {
        "consonants": ["x", "z", "k", "t", "n", "r", "b", "d"],
        "vowels": ["0", "1", "a", "e", "o"],
        "endings": ["-7", "-X", "ron", "tex", "nix", "bot", "dex", "max"],
        "prefixes": ["X-", "Z-", "K-", "Unit", "Core", "Node", "Mech", "Sys"],
    },
    LanguageFamily.COSMIC: {
        "consonants": ["th", "ph", "ch", "sh", "zh", "n", "m", "l", "r"],
        "vowels": ["a", "e", "i", "o", "u", "aa", "oo", "ae", "ou"],
        "endings": ["thos", "phor", "chal", "nous", "zhar", "lith", "neth", "ael"],
        "prefixes": ["Aeo", "Zha", "Pho", "Cha", "Nou", "Eth", "Vor", "Ael"],
    },
}


# Star name patterns (some use language family, some universal)
STAR_DESCRIPTORS = [
    "Prime", "Major", "Minor", "Alpha", "Beta", "Gamma", "Delta",
    "Bright", "Dark", "Ancient", "Young", "Binary", "Triple"
]

STAR_SUFFIXES = [
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "A", "B", "C", "Alpha", "Beta", "Gamma"
]

# Planet name patterns
PLANET_DESCRIPTORS = [
    "New", "Old", "Greater", "Lesser", "Inner", "Outer", "Far", "Near"
]

# Creature trait words for names
CREATURE_TRAITS = [
    "swift", "great", "lesser", "giant", "dwarf", "horned", "fanged",
    "winged", "scaled", "armored", "spined", "crested", "spotted",
    "striped", "banded", "golden", "silver", "crimson", "azure",
    "midnight", "dawn", "dusk", "shadow", "flame", "frost", "thunder"
]

CREATURE_TYPES = [
    "beast", "crawler", "flyer", "swimmer", "stalker", "grazer",
    "hunter", "prowler", "drifter", "burrower", "climber", "leaper"
]


def get_random_language_family() -> LanguageFamily:
    """Get a random language family"""
    return random.choice(list(LanguageFamily))


def generate_syllable(family: LanguageFamily, pattern: str = "CV") -> str:
    """
    Generate a syllable based on pattern.
    C = consonant, V = vowel
    """
    phonemes = PHONEMES[family]
    result = ""

    for char in pattern:
        if char == "C":
            result += random.choice(phonemes["consonants"])
        elif char == "V":
            result += random.choice(phonemes["vowels"])

    return result


def generate_name_base(family: LanguageFamily, syllables: int = 2) -> str:
    """Generate a basic name with given number of syllables"""
    patterns = ["CV", "CVC", "VC", "CVV", "CVCV"]

    name_parts = []
    for i in range(syllables):
        pattern = random.choice(patterns)
        name_parts.append(generate_syllable(family, pattern))

    return "".join(name_parts)


def generate_name_with_prefix(family: LanguageFamily) -> str:
    """Generate a name with a language-appropriate prefix"""
    phonemes = PHONEMES[family]
    prefix = random.choice(phonemes["prefixes"])
    base = generate_name_base(family, random.randint(1, 2))
    return prefix + base.lower()


def generate_name_with_ending(family: LanguageFamily) -> str:
    """Generate a name with a language-appropriate ending"""
    phonemes = PHONEMES[family]
    base = generate_name_base(family, random.randint(1, 2))
    ending = random.choice(phonemes["endings"])
    return base.capitalize() + ending


def generate_full_name(family: LanguageFamily) -> str:
    """Generate a complete name using various methods"""
    method = random.choice([
        "prefix",
        "ending",
        "base_only",
        "prefix_ending"
    ])

    if method == "prefix":
        return generate_name_with_prefix(family)
    elif method == "ending":
        return generate_name_with_ending(family)
    elif method == "base_only":
        return generate_name_base(family, random.randint(2, 3)).capitalize()
    else:  # prefix_ending
        phonemes = PHONEMES[family]
        prefix = random.choice(phonemes["prefixes"])
        base = generate_syllable(family, "CV")
        ending = random.choice(phonemes["endings"])
        return prefix + base.lower() + ending


# ============ Specific Name Generators ============

def generate_star_name(family: Optional[LanguageFamily] = None,
                       named_by_civ: bool = False) -> str:
    """
    Generate a star name.
    If named_by_civ, uses language family for cultural name.
    Otherwise, uses scientific-style designation.
    """
    if named_by_civ and family:
        # Cultural name
        base = generate_full_name(family)
        if random.random() < 0.3:
            base += " " + random.choice(STAR_DESCRIPTORS)
        return base
    else:
        # Scientific designation (for unnamed stars)
        prefix = random.choice(["HD", "HIP", "GJ", "TYC", "2MASS"])
        number = random.randint(1000, 999999)
        suffix = random.choice(["", "A", "B", " Ab", " Bb"])
        return f"{prefix} {number}{suffix}"


def generate_planet_name(family: Optional[LanguageFamily] = None,
                         star_name: Optional[str] = None,
                         named_by_civ: bool = False) -> str:
    """
    Generate a planet name.
    Can be cultural (if named by civ) or designation-based.
    """
    if named_by_civ and family:
        # Cultural name
        base = generate_full_name(family)
        if random.random() < 0.2:
            base = random.choice(PLANET_DESCRIPTORS) + " " + base
        return base
    elif star_name:
        # Designation based on star
        suffix = random.choice(["b", "c", "d", "e", "f", "g"])
        return f"{star_name} {suffix}"
    else:
        # Generic designation
        prefix = random.choice(["Kepler", "TOI", "K2", "TRAPPIST"])
        number = random.randint(100, 9999)
        suffix = random.choice(["b", "c", "d", "e"])
        return f"{prefix}-{number}{suffix}"


def generate_moon_name(family: Optional[LanguageFamily] = None,
                       planet_name: Optional[str] = None,
                       named_by_civ: bool = False) -> str:
    """Generate a moon name"""
    if named_by_civ and family:
        return generate_full_name(family)
    elif planet_name:
        numeral = random.choice(["I", "II", "III", "IV", "V", "VI"])
        return f"{planet_name} {numeral}"
    else:
        return generate_name_base(get_random_language_family(), 2).capitalize()


def generate_galaxy_name(family: Optional[LanguageFamily] = None,
                         named_by_civ: bool = False) -> str:
    """Generate a galaxy name"""
    if named_by_civ and family:
        base = generate_full_name(family)
        return base + " Galaxy"
    else:
        # Scientific designation
        prefix = random.choice(["NGC", "IC", "UGC", "PGC", "Messier"])
        number = random.randint(1, 9999)
        return f"{prefix} {number}"


def generate_civilization_name(family: LanguageFamily) -> str:
    """Generate a civilization/empire name"""
    base = generate_full_name(family)

    suffix_type = random.choice(["people", "empire", "federation", "collective", "none"])

    if suffix_type == "people":
        suffixes = ["i", "an", "ese", "ite", "ar", "ori", "kin"]
        return "The " + base + random.choice(suffixes)
    elif suffix_type == "empire":
        titles = ["Empire", "Dominion", "Hegemony", "Sovereignty", "Realm"]
        return "The " + base + " " + random.choice(titles)
    elif suffix_type == "federation":
        titles = ["Federation", "Alliance", "Collective", "Union", "Accord"]
        return "The " + base + " " + random.choice(titles)
    elif suffix_type == "collective":
        return "The " + base + " Collective"
    else:
        return "The " + base


def generate_species_name(family: LanguageFamily) -> str:
    """Generate a species name"""
    base = generate_full_name(family)

    # Sometimes add a suffix
    if random.random() < 0.5:
        suffixes = ["i", "ans", "ites", "oids", "ari", "kin", "folk"]
        base = base + random.choice(suffixes)

    return base


def generate_religion_name(family: LanguageFamily,
                           religion_type: str = "monotheistic") -> str:
    """Generate a religion name"""
    base = generate_full_name(family)

    if religion_type == "monotheistic":
        patterns = [
            f"The Faith of {base}",
            f"The {base} Church",
            f"{base}ism",
            f"The Path of {base}",
            f"The {base} Truth",
        ]
    elif religion_type == "polytheistic":
        patterns = [
            f"The {base} Pantheon",
            f"The Old Gods of {base}",
            f"The {base} Traditions",
            f"The Many of {base}",
        ]
    elif religion_type == "philosophical":
        patterns = [
            f"The {base} Way",
            f"{base}ism",
            f"The {base} Philosophy",
            f"The Path of {base}",
        ]
    elif religion_type == "cosmic":
        patterns = [
            f"The Void Church of {base}",
            f"The {base} Mysteries",
            f"Children of {base}",
            f"The {base} Enlightenment",
        ]
    else:
        patterns = [
            f"The {base} Faith",
            f"The Way of {base}",
        ]

    return random.choice(patterns)


def generate_culture_name(family: LanguageFamily) -> str:
    """Generate a culture/ethnic group name"""
    base = generate_full_name(family)

    if random.random() < 0.3:
        descriptors = ["Northern", "Southern", "Eastern", "Western",
                       "Highland", "Lowland", "Coastal", "Desert", "Forest"]
        return random.choice(descriptors) + " " + base

    return base


def generate_leader_name(family: LanguageFamily,
                         title: Optional[str] = None) -> str:
    """Generate a leader/historical figure name"""
    first = generate_full_name(family)

    # Sometimes add a second name or epithet
    if random.random() < 0.4:
        second = generate_full_name(family)
        name = f"{first} {second}"
    else:
        name = first

    if title:
        name = f"{title} {name}"

    # Sometimes add an epithet
    if random.random() < 0.3:
        epithets = ["the Great", "the Wise", "the Conqueror", "the Builder",
                    "the Unifier", "the Prophet", "the Destroyer", "the Peaceful",
                    "the Bold", "the Just", "the Terrible", "the Magnificent"]
        name = name + " " + random.choice(epithets)

    return name


def generate_city_name(family: LanguageFamily) -> str:
    """Generate a city/settlement name"""
    base = generate_full_name(family)

    if random.random() < 0.2:
        suffixes = [" City", " Prime", " Major", " Central", " Port", " Haven"]
        base = base + random.choice(suffixes)

    return base


def generate_creature_name(family: Optional[LanguageFamily] = None,
                           scientific: bool = False) -> str:
    """Generate a creature/species name"""
    if scientific:
        # Pseudo-Latin scientific name
        family_to_use = LanguageFamily.ANCIENT
        genus = generate_name_base(family_to_use, 2).capitalize()
        species = generate_name_base(family_to_use, 2).lower()
        return f"{genus} {species}"
    elif family:
        # Cultural name
        trait = random.choice(CREATURE_TRAITS)
        creature_type = random.choice(CREATURE_TYPES)
        return f"{trait.capitalize()} {creature_type.capitalize()}"
    else:
        # Generic
        base = generate_name_base(get_random_language_family(), 2)
        return base.capitalize()


def generate_flora_name(family: Optional[LanguageFamily] = None,
                        scientific: bool = False) -> str:
    """Generate a plant/flora name"""
    if scientific:
        family_to_use = LanguageFamily.ANCIENT
        genus = generate_name_base(family_to_use, 2).capitalize()
        species = generate_name_base(family_to_use, 2).lower()
        return f"{genus} {species}"
    else:
        plant_types = ["fern", "moss", "tree", "vine", "flower", "shrub",
                       "grass", "kelp", "fungus", "bloom", "weed", "cactus"]
        descriptors = ["giant", "dwarf", "golden", "silver", "spiral", "crystal",
                       "blood", "moon", "sun", "star", "ghost", "iron", "silk"]
        return f"{random.choice(descriptors).capitalize()} {random.choice(plant_types)}"


def generate_war_name(family: LanguageFamily,
                      opponent_name: Optional[str] = None) -> str:
    """Generate a war/conflict name"""
    if opponent_name:
        patterns = [
            f"The {opponent_name} War",
            f"The War of {opponent_name} Aggression",
            f"The {opponent_name} Conflict",
        ]
    else:
        base = generate_full_name(family)
        patterns = [
            f"The {base} War",
            f"The War of {base}",
            f"The {base} Conflict",
            f"The Great War",
            f"The Final War",
            f"The War of Unification",
            f"The Border Wars",
        ]

    return random.choice(patterns)


def generate_treaty_name(family: LanguageFamily,
                         location: Optional[str] = None) -> str:
    """Generate a treaty/accord name"""
    if location:
        return f"The {location} Accords"
    else:
        base = generate_full_name(family)
        patterns = [
            f"The {base} Treaty",
            f"The {base} Accords",
            f"The {base} Pact",
            f"The Peace of {base}",
            f"The {base} Agreement",
        ]
        return random.choice(patterns)


def generate_era_name(family: LanguageFamily) -> str:
    """Generate a historical era name"""
    base = generate_full_name(family)
    patterns = [
        f"The {base} Era",
        f"The Age of {base}",
        f"The {base} Period",
        f"The {base} Dynasty",
        f"The {base} Epoch",
    ]
    return random.choice(patterns)


# ============ Batch Generation ============

def generate_name_set_for_civilization(family: LanguageFamily) -> dict:
    """Generate a complete set of names for a new civilization"""
    return {
        "civilization_name": generate_civilization_name(family),
        "species_name": generate_species_name(family),
        "homeworld_name": generate_planet_name(family, named_by_civ=True),
        "home_star_name": generate_star_name(family, named_by_civ=True),
        "capital_city": generate_city_name(family),
        "founding_leader": generate_leader_name(family),
        "primary_religion": generate_religion_name(family),
        "language_family": family.value,
    }


# For module imports
__all__ = [
    "LanguageFamily",
    "get_random_language_family",
    "generate_star_name",
    "generate_planet_name",
    "generate_moon_name",
    "generate_galaxy_name",
    "generate_civilization_name",
    "generate_species_name",
    "generate_religion_name",
    "generate_culture_name",
    "generate_leader_name",
    "generate_city_name",
    "generate_creature_name",
    "generate_flora_name",
    "generate_war_name",
    "generate_treaty_name",
    "generate_era_name",
    "generate_name_set_for_civilization",
]
