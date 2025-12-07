"""
Commit Universe Engine - Code Generators

Each generator creates files in a specific language for different cosmic objects.
"""

from .go_gen import generate_constants_go
from .toml_gen import generate_cluster_toml
from .rust_gen import generate_galaxy_rs
from .c_gen import generate_star_c
from .python_gen import generate_planet_py
from .lua_gen import generate_moon_lua
from .json_gen import generate_atmosphere_json
from .js_gen import generate_life_js
from .ts_gen import generate_civilization_ts
from .sql_gen import generate_registry_sql, append_registry_sql
from .markdown_gen import generate_chronicle_md, append_chronicle_md
from .esoteric_gen import generate_anomaly_bf, generate_ruins_cob

__all__ = [
    "generate_constants_go",
    "generate_cluster_toml",
    "generate_galaxy_rs",
    "generate_star_c",
    "generate_planet_py",
    "generate_moon_lua",
    "generate_atmosphere_json",
    "generate_life_js",
    "generate_civilization_ts",
    "generate_registry_sql",
    "append_registry_sql",
    "generate_chronicle_md",
    "append_chronicle_md",
    "generate_anomaly_bf",
    "generate_ruins_cob",
]
