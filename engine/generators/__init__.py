"""
Commit Universe Engine - Code Generators

Each generator creates files in a specific language for different cosmic objects.
"""

from .go_gen import generate_constants_go
from .toml_gen import generate_cluster_toml, update_cluster_stats, get_cluster_galaxy_count
from .rust_gen import generate_galaxy_rs
from .c_gen import generate_star_c
from .python_gen import generate_planet_py
from .lua_gen import generate_moon_lua
from .json_gen import generate_atmosphere_json
from .js_gen import generate_life_js, generate_ecosystem_js, generate_creature_json, generate_flora_json
from .ts_gen import generate_civilization_ts
from .sql_gen import generate_registry_sql, append_registry_sql
from .markdown_gen import generate_chronicle_md, append_chronicle_md
from .esoteric_gen import generate_anomaly_bf, generate_ruins_cob

# New generators
from .name_gen import (
    LanguageFamily,
    get_random_language_family,
    generate_star_name,
    generate_planet_name,
    generate_moon_name,
    generate_galaxy_name,
    generate_civilization_name,
    generate_species_name,
    generate_religion_name,
    generate_culture_name,
    generate_leader_name,
    generate_city_name,
    generate_creature_name,
    generate_flora_name,
    generate_war_name,
    generate_treaty_name,
    generate_era_name,
    generate_name_set_for_civilization,
)

from .creature_gen import (
    BiologyType,
    CreatureCategory,
    CreatureRole,
    SizeClass,
    IntelligenceLevel,
    Creature,
    Flora,
    generate_creature,
    generate_apex_predator,
    generate_flora,
    generate_ecosystem_creatures,
    determine_biology_type,
)

__all__ = [
    # Existing generators
    "generate_constants_go",
    "generate_cluster_toml",
    "update_cluster_stats",
    "get_cluster_galaxy_count",
    "generate_galaxy_rs",
    "generate_star_c",
    "generate_planet_py",
    "generate_moon_lua",
    "generate_atmosphere_json",
    "generate_life_js",
    "generate_ecosystem_js",
    "generate_creature_json",
    "generate_flora_json",
    "generate_civilization_ts",
    "generate_registry_sql",
    "append_registry_sql",
    "generate_chronicle_md",
    "append_chronicle_md",
    "generate_anomaly_bf",
    "generate_ruins_cob",

    # Name generators
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

    # Creature generators
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
