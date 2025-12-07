"""
Commit Universe Engine - Universe State Management

Handles reading and tracking the current state of the universe.
"""

import json
import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
import re


@dataclass
class Epoch:
    """Current state of cosmic time"""
    commit_count: int = 0
    cosmic_age_million_years: float = 0
    current_era: str = "void"
    

@dataclass  
class Galaxy:
    id: str
    name: Optional[str] = None
    galaxy_type: str = "spiral"
    age_billion_years: float = 0
    diameter_light_years: int = 0
    star_count: int = 0
    formed_at_commit: int = 0
    path: str = ""


@dataclass
class Star:
    id: str
    name: Optional[str] = None
    spectral_class: str = "G"
    mass_solar: float = 1.0
    age_billion_years: float = 0
    life_stage: str = "main_sequence"
    planet_count: int = 0
    habitable_zone_inner_au: float = 0.9
    habitable_zone_outer_au: float = 1.4
    formed_at_commit: int = 0
    path: str = ""


@dataclass
class Planet:
    id: str
    name: Optional[str] = None
    planet_type: str = "terrestrial"
    mass_earth: float = 1.0
    radius_earth: float = 1.0
    orbit_au: float = 1.0
    orbit_days: float = 365
    moon_count: int = 0
    has_atmosphere: bool = False
    has_water: bool = False
    has_life: bool = False
    has_intelligent_life: bool = False
    formed_at_commit: int = 0
    path: str = ""


@dataclass
class Life:
    planet_path: str
    emerged_at_commit: int = 0
    stage: str = "single_cell"
    species_count: int = 1
    extinction_events: int = 0
    

@dataclass
class Civilization:
    id: str
    name: str
    species: str
    homeworld: str
    emerged_at_commit: int = 0
    tech_level: int = 0
    population: int = 0
    colonies: List[str] = field(default_factory=list)
    traits: List[str] = field(default_factory=list)
    status: str = "emerging"
    path: str = ""


@dataclass
class UniverseState:
    """Complete state of the universe"""
    epoch: Epoch = field(default_factory=Epoch)
    clusters: List[str] = field(default_factory=list)
    galaxies: List[Galaxy] = field(default_factory=list)
    stars: List[Star] = field(default_factory=list)
    planets: List[Planet] = field(default_factory=list)
    life_worlds: List[Life] = field(default_factory=list)
    civilizations: List[Civilization] = field(default_factory=list)
    
    # Quick counts
    total_galaxies: int = 0
    total_stars: int = 0
    total_planets: int = 0
    total_life: int = 0
    total_civilizations: int = 0


class UniverseReader:
    """Reads the current state of the universe from the repo"""
    
    def __init__(self, universe_root: Path):
        self.root = Path(universe_root)
        
    def read_state(self) -> UniverseState:
        """Read the complete universe state"""
        state = UniverseState()
        
        # Read epoch
        state.epoch = self._read_epoch()
        
        # Scan for objects
        if (self.root / "clusters").exists():
            state.clusters = self._scan_clusters()
            state.galaxies = self._scan_galaxies()
            state.stars = self._scan_stars()
            state.planets = self._scan_planets()
            state.life_worlds = self._scan_life()
            state.civilizations = self._scan_civilizations()
        
        # Update counts
        state.total_galaxies = len(state.galaxies)
        state.total_stars = len(state.stars)
        state.total_planets = len(state.planets)
        state.total_life = len(state.life_worlds)
        state.total_civilizations = len(state.civilizations)
        
        return state
    
    def _read_epoch(self) -> Epoch:
        """Read epoch.json"""
        epoch_file = self.root / "epoch.json"
        if epoch_file.exists():
            with open(epoch_file) as f:
                data = json.load(f)
                return Epoch(
                    commit_count=data.get("commit_count", 0),
                    cosmic_age_million_years=data.get("cosmic_age_million_years", 0),
                    current_era=data.get("current_era", "void")
                )
        return Epoch()
    
    def _scan_clusters(self) -> List[str]:
        """Find all cluster directories"""
        clusters_dir = self.root / "clusters"
        if not clusters_dir.exists():
            return []
        return [d.name for d in clusters_dir.iterdir() if d.is_dir()]
    
    def _scan_galaxies(self) -> List[Galaxy]:
        """Find and parse all galaxy files"""
        galaxies = []
        clusters_dir = self.root / "clusters"
        if not clusters_dir.exists():
            return galaxies
            
        for cluster_dir in clusters_dir.iterdir():
            if not cluster_dir.is_dir():
                continue
            galaxies_dir = cluster_dir / "galaxies"
            if not galaxies_dir.exists():
                continue
                
            for galaxy_dir in galaxies_dir.iterdir():
                if not galaxy_dir.is_dir():
                    continue
                galaxy_file = galaxy_dir / "galaxy.rs"
                if galaxy_file.exists():
                    galaxy = self._parse_galaxy_rs(galaxy_file, str(galaxy_dir.relative_to(self.root)))
                    if galaxy:
                        galaxies.append(galaxy)
        return galaxies
    
    def _scan_stars(self) -> List[Star]:
        """Find and parse all star files"""
        stars = []
        clusters_dir = self.root / "clusters"
        if not clusters_dir.exists():
            return stars
        for star_file in clusters_dir.rglob("star.c"):
            star = self._parse_star_c(star_file, str(star_file.parent.relative_to(self.root)))
            if star:
                stars.append(star)
        return stars
    
    def _scan_planets(self) -> List[Planet]:
        """Find and parse all planet files"""
        planets = []
        clusters_dir = self.root / "clusters"
        if not clusters_dir.exists():
            return planets
        for planet_file in clusters_dir.rglob("planet.py"):
            planet = self._parse_planet_py(planet_file, str(planet_file.parent.relative_to(self.root)))
            if planet:
                planets.append(planet)
        return planets
    
    def _scan_life(self) -> List[Life]:
        """Find all planets with life"""
        life_worlds = []
        clusters_dir = self.root / "clusters"
        if not clusters_dir.exists():
            return life_worlds
        for life_file in clusters_dir.rglob("life.js"):
            life = self._parse_life_js(life_file, str(life_file.parent.relative_to(self.root)))
            if life:
                life_worlds.append(life)
        return life_worlds
    
    def _scan_civilizations(self) -> List[Civilization]:
        """Find and parse all civilization files"""
        civs = []
        clusters_dir = self.root / "clusters"
        if not clusters_dir.exists():
            return civs
        for civ_file in clusters_dir.rglob("civilization.ts"):
            civ = self._parse_civilization_ts(civ_file, str(civ_file.parent.relative_to(self.root)))
            if civ:
                civs.append(civ)
        return civs
    
    def _parse_galaxy_rs(self, filepath: Path, rel_path: str) -> Optional[Galaxy]:
        """Parse a galaxy.rs file"""
        try:
            content = filepath.read_text()
            # Extract values using regex (simplified parsing)
            galaxy = Galaxy(
                id=self._extract_rust_string(content, "id") or filepath.parent.name,
                name=self._extract_rust_option_string(content, "name"),
                galaxy_type=self._extract_rust_enum(content, "classification") or "spiral",
                formed_at_commit=self._extract_rust_int(content, "formed_at_commit") or 0,
                star_count=self._extract_rust_int(content, "star_count") or 0,
                path=rel_path
            )
            return galaxy
        except Exception:
            return None
    
    def _parse_star_c(self, filepath: Path, rel_path: str) -> Optional[Star]:
        """Parse a star.c file"""
        try:
            content = filepath.read_text()
            star = Star(
                id=self._extract_c_string(content, "id") or filepath.parent.name,
                name=self._extract_c_string(content, "name") or None,
                spectral_class=self._extract_c_enum(content, "spectral_class") or "G",
                mass_solar=self._extract_c_float(content, "mass_solar") or 1.0,
                life_stage=self._extract_c_enum(content, "life_stage") or "main_sequence",
                planet_count=self._extract_c_int(content, "planet_count") or 0,
                formed_at_commit=self._extract_c_int(content, "formed_at_commit") or 0,
                path=rel_path
            )
            return star
        except Exception:
            return None
    
    def _parse_planet_py(self, filepath: Path, rel_path: str) -> Optional[Planet]:
        """Parse a planet.py file"""
        try:
            content = filepath.read_text()
            planet = Planet(
                id=self._extract_py_string(content, "id") or filepath.parent.name,
                name=self._extract_py_string(content, "name"),
                planet_type=self._extract_py_enum(content, "planet_type") or "terrestrial",
                mass_earth=self._extract_py_float(content, "mass_earth") or 1.0,
                has_atmosphere=self._extract_py_bool(content, "has_atmosphere"),
                has_water=self._extract_py_bool(content, "has_water"),
                has_life=self._extract_py_bool(content, "has_life"),
                has_intelligent_life=self._extract_py_bool(content, "has_intelligent_life"),
                formed_at_commit=self._extract_py_int(content, "formed_at_commit") or 0,
                path=rel_path
            )
            return planet
        except Exception:
            return None
    
    def _parse_life_js(self, filepath: Path, rel_path: str) -> Optional[Life]:
        """Parse a life.js file"""
        try:
            content = filepath.read_text()
            life = Life(
                planet_path=rel_path,
                emerged_at_commit=self._extract_js_int(content, "emerged_at_commit") or 0,
                stage=self._extract_js_string(content, "stage") or "single_cell",
                species_count=self._extract_js_int(content, "species_count") or 1,
            )
            return life
        except Exception:
            return None
    
    def _parse_civilization_ts(self, filepath: Path, rel_path: str) -> Optional[Civilization]:
        """Parse a civilization.ts file"""
        try:
            content = filepath.read_text()
            civ = Civilization(
                id=self._extract_ts_string(content, "id") or "unknown",
                name=self._extract_ts_string(content, "name") or "Unknown",
                species=self._extract_ts_string(content, "species") or "unknown",
                homeworld=self._extract_ts_string(content, "homeworld") or "",
                emerged_at_commit=self._extract_ts_int(content, "emerged_at_commit") or 0,
                tech_level=self._extract_ts_int(content, "tech_level") or 0,
                population=self._extract_ts_int(content, "population") or 0,
                status=self._extract_ts_string(content, "status") or "emerging",
                path=rel_path
            )
            return civ
        except Exception:
            return None
    
    # Helper extraction methods
    def _extract_rust_string(self, content: str, field: str) -> Optional[str]:
        match = re.search(rf'{field}:\s*"([^"]*)"', content)
        return match.group(1) if match else None
    
    def _extract_rust_option_string(self, content: str, field: str) -> Optional[str]:
        match = re.search(rf'{field}:\s*Some\("([^"]*)"\)', content)
        return match.group(1) if match else None
    
    def _extract_rust_enum(self, content: str, field: str) -> Optional[str]:
        match = re.search(rf'{field}:\s*\w+::(\w+)', content)
        return match.group(1).lower() if match else None
    
    def _extract_rust_int(self, content: str, field: str) -> Optional[int]:
        match = re.search(rf'{field}:\s*([\d_]+)', content)
        return int(match.group(1).replace('_', '')) if match else None
    
    def _extract_c_string(self, content: str, field: str) -> Optional[str]:
        match = re.search(rf'\.{field}\s*=\s*"([^"]*)"', content)
        return match.group(1) if match else None
    
    def _extract_c_enum(self, content: str, field: str) -> Optional[str]:
        match = re.search(rf'\.{field}\s*=\s*\w+_(\w+)', content)
        return match.group(1).lower() if match else None
    
    def _extract_c_float(self, content: str, field: str) -> Optional[float]:
        match = re.search(rf'\.{field}\s*=\s*([\d.]+)', content)
        return float(match.group(1)) if match else None
    
    def _extract_c_int(self, content: str, field: str) -> Optional[int]:
        match = re.search(rf'\.{field}\s*=\s*(\d+)', content)
        return int(match.group(1)) if match else None
    
    def _extract_py_string(self, content: str, field: str) -> Optional[str]:
        match = re.search(rf'{field}="([^"]*)"', content)
        if not match:
            match = re.search(rf"{field}='([^']*)'", content)
        return match.group(1) if match else None
    
    def _extract_py_enum(self, content: str, field: str) -> Optional[str]:
        match = re.search(rf'{field}=\w+\.(\w+)', content)
        return match.group(1).lower() if match else None
    
    def _extract_py_float(self, content: str, field: str) -> Optional[float]:
        match = re.search(rf'{field}=([\d.]+)', content)
        return float(match.group(1)) if match else None
    
    def _extract_py_int(self, content: str, field: str) -> Optional[int]:
        match = re.search(rf'{field}=(\d+)', content)
        return int(match.group(1)) if match else None
    
    def _extract_py_bool(self, content: str, field: str) -> bool:
        match = re.search(rf'{field}=(True|False)', content)
        return match.group(1) == "True" if match else False
    
    def _extract_js_string(self, content: str, field: str) -> Optional[str]:
        match = re.search(rf'{field}:\s*["\']([^"\']*)["\']', content)
        return match.group(1) if match else None
    
    def _extract_js_int(self, content: str, field: str) -> Optional[int]:
        match = re.search(rf'{field}:\s*([\d_]+)', content)
        return int(match.group(1).replace('_', '')) if match else None
    
    def _extract_ts_string(self, content: str, field: str) -> Optional[str]:
        return self._extract_js_string(content, field)
    
    def _extract_ts_int(self, content: str, field: str) -> Optional[int]:
        return self._extract_js_int(content, field)
