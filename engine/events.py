"""
Commit Universe Engine - Event Generation

Handles the probabilistic generation of cosmic events based on universe state.
"""

import random
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum

from .config import (
    EVENT_WEIGHTS, MILESTONES, SPECTRAL_CLASSES, SPECTRAL_WEIGHTS,
    PLANET_TYPES, PLANET_WEIGHTS, GALAXY_TYPES, GALAXY_WEIGHTS,
    CIV_TRAITS, TECH_LEVELS
)
from .universe import UniverseState, Galaxy, Star, Planet, Life, Civilization


class EventType(Enum):
    # Cosmic
    GALAXY_FORM = "galaxy_form"
    NEBULA_FORM = "nebula_form"
    STAR_FORM = "star_form"
    STAR_EVOLVE = "star_evolve"
    SUPERNOVA = "supernova"
    BLACK_HOLE = "black_hole"
    
    # Planetary
    PLANET_FORM = "planet_form"
    MOON_FORM = "moon_form"
    ATMOSPHERE_FORM = "atmosphere_form"
    OCEAN_FORM = "ocean_form"
    ASTEROID_IMPACT = "asteroid_impact"
    
    # Life
    ABIOGENESIS = "abiogenesis"
    LIFE_EVOLVE = "life_evolve"
    MASS_EXTINCTION = "mass_extinction"
    INTELLIGENCE = "intelligence"
    
    # Civilization
    CIV_EMERGE = "civ_emerge"
    CIV_ADVANCE = "civ_advance"
    CIV_EXPAND = "civ_expand"
    CIV_DISCOVERY = "civ_discovery"
    FIRST_CONTACT = "first_contact"
    CIV_WAR = "civ_war"
    CIV_PEACE = "civ_peace"
    CIV_COLLAPSE = "civ_collapse"
    
    # Special
    ANOMALY = "anomaly"
    RUINS_DISCOVERED = "ruins_discovered"


@dataclass
class Event:
    """Represents a generated cosmic event"""
    event_type: EventType
    location: str
    description: str
    commit_message: str
    files_to_create: List[Tuple[str, str]]  # (path, content)
    files_to_modify: List[Tuple[str, str, str]]  # (path, section, content)
    magnitude: float = 1.0


class EventGenerator:
    """Generates cosmic events based on universe state"""
    
    def __init__(self, state: UniverseState, seed: Optional[int] = None):
        self.state = state
        self.commit = state.epoch.commit_count
        if seed:
            random.seed(seed)
        
        # Track objects created during this run
        self._galaxies_created = 0
        self._stars_created = 0
        self._planets_created = 0
        self._clusters_created = set()
    
    def generate_events(self, count: int = 1) -> List[Event]:
        """Generate one or more events"""
        events = []
        for _ in range(count):
            event = self._generate_single_event()
            if event:
                events.append(event)
        return events
    
    def _generate_single_event(self) -> Optional[Event]:
        """Generate a single event based on current state and probabilities"""
        
        # Determine what types of events are possible
        possible_events = self._get_possible_events()
        
        if not possible_events:
            # Fallback: always allow galaxy formation early on
            total_galaxies = self.state.total_galaxies + self._galaxies_created
            if self.commit < 1000 or total_galaxies == 0:
                return self._generate_galaxy_event()
            return None
        
        # Weight and select an event type
        event_type = self._select_event_type(possible_events)
        
        # Generate the specific event
        generators = {
            EventType.GALAXY_FORM: self._generate_galaxy_event,
            EventType.STAR_FORM: self._generate_star_event,
            EventType.STAR_EVOLVE: self._generate_star_evolution_event,
            EventType.PLANET_FORM: self._generate_planet_event,
            EventType.MOON_FORM: self._generate_moon_event,
            EventType.ATMOSPHERE_FORM: self._generate_atmosphere_event,
            EventType.ABIOGENESIS: self._generate_abiogenesis_event,
            EventType.LIFE_EVOLVE: self._generate_life_evolution_event,
            EventType.INTELLIGENCE: self._generate_intelligence_event,
            EventType.CIV_EMERGE: self._generate_civilization_event,
            EventType.CIV_ADVANCE: self._generate_civ_advance_event,
            EventType.CIV_EXPAND: self._generate_colony_event,
            EventType.FIRST_CONTACT: self._generate_first_contact_event,
            EventType.SUPERNOVA: self._generate_supernova_event,
            EventType.ANOMALY: self._generate_anomaly_event,
        }
        
        generator = generators.get(event_type)
        if generator:
            return generator()
        
        return None
    
    def _get_possible_events(self) -> List[EventType]:
        """Determine which events are possible based on current state"""
        possible = []
        commit = self.commit
        
        # Track totals including this run
        total_galaxies = self.state.total_galaxies + self._galaxies_created
        total_stars = self.state.total_stars + self._stars_created
        total_planets = self.state.total_planets + self._planets_created
        
        # Cosmic events (always possible after certain points)
        if commit >= MILESTONES.get("galaxy_formation", 50):
            possible.append(EventType.GALAXY_FORM)
        
        if commit >= MILESTONES.get("star_formation", 500) and total_galaxies > 0:
            possible.append(EventType.STAR_FORM)
        
        if total_stars > 0:
            possible.append(EventType.STAR_EVOLVE)
        
        # Planetary events
        if commit >= MILESTONES.get("planet_formation", 2000) and total_stars > 0:
            possible.append(EventType.PLANET_FORM)
        
        if total_planets > 0:
            possible.append(EventType.MOON_FORM)
            possible.append(EventType.ATMOSPHERE_FORM)
        
        # Life events
        habitable_planets = [p for p in self.state.planets if p.has_atmosphere and p.has_water]
        if commit >= MILESTONES.get("life_possible", 10000) and habitable_planets:
            possible.append(EventType.ABIOGENESIS)
        
        if self.state.total_life > 0:
            possible.append(EventType.LIFE_EVOLVE)
        
        # Check for planets with intelligent-ready life
        if commit >= MILESTONES.get("intelligence_possible", 50000):
            advanced_life = [l for l in self.state.life_worlds 
                           if l.stage in ("complex_multicellular", "intelligent")]
            if advanced_life:
                possible.append(EventType.INTELLIGENCE)
        
        # Civilization events
        if self.state.total_civilizations > 0:
            possible.append(EventType.CIV_ADVANCE)
            possible.append(EventType.CIV_EXPAND)
        
        if self.state.total_civilizations >= 2:
            possible.append(EventType.FIRST_CONTACT)
        
        # Rare events
        if total_stars > 10:
            possible.append(EventType.SUPERNOVA)
        
        if commit > 10000 and random.random() < 0.01:
            possible.append(EventType.ANOMALY)
        
        return possible
    
    def _select_event_type(self, possible: List[EventType]) -> EventType:
        """Select an event type based on weights"""
        # Get weights for possible events
        weights = []
        for event_type in possible:
            weight_key = event_type.value
            weight = EVENT_WEIGHTS.get(weight_key, 0.05)
            weights.append(weight)
        
        # Normalize and select
        total = sum(weights)
        if total == 0:
            return random.choice(possible)
        
        r = random.random() * total
        cumulative = 0
        for event_type, weight in zip(possible, weights):
            cumulative += weight
            if r <= cumulative:
                return event_type
        
        return possible[-1]
    
    # Event generators
    def _generate_galaxy_event(self) -> Event:
        """Generate a new galaxy"""
        from .generators import generate_galaxy_rs, generate_cluster_toml
        
        # Track total galaxies (existing + created this run)
        total_galaxies = self.state.total_galaxies + self._galaxies_created
        total_clusters = len(self.state.clusters) + len(self._clusters_created)
        
        # Determine cluster (create if needed, or add to existing)
        cluster_num = (total_galaxies // 100) + 1  # ~100 galaxies per cluster
        cluster_id = f"cluster-{cluster_num:04d}"
        
        galaxy_id = f"galaxy-{total_galaxies + 1:04d}"
        
        # Random galaxy properties
        galaxy_type = random.choices(GALAXY_TYPES, GALAXY_WEIGHTS)[0]
        diameter = random.randint(20000, 150000)
        
        # Generate files
        cluster_path = f"clusters/{cluster_id}"
        galaxy_path = f"{cluster_path}/galaxies/{galaxy_id}"
        
        galaxy_content = generate_galaxy_rs(
            galaxy_id=galaxy_id,
            galaxy_type=galaxy_type,
            diameter_light_years=diameter,
            formed_at_commit=self.commit
        )
        
        files_to_create = [
            (f"{galaxy_path}/galaxy.rs", galaxy_content),
        ]
        
        # Create cluster if new
        is_new_cluster = cluster_id not in self.state.clusters and cluster_id not in self._clusters_created
        if is_new_cluster:
            cluster_content = generate_cluster_toml(
                cluster_id=cluster_id,
                formed_at_commit=self.commit
            )
            files_to_create.append((f"{cluster_path}/cluster.toml", cluster_content))
            self._clusters_created.add(cluster_id)
        
        # Track this creation
        self._galaxies_created += 1
        
        return Event(
            event_type=EventType.GALAXY_FORM,
            location=galaxy_path,
            description=f"A {galaxy_type} galaxy coalesces from primordial matter",
            commit_message=f"form({galaxy_path}): {galaxy_type} galaxy emerges from the cosmic dark",
            files_to_create=files_to_create,
            files_to_modify=[],
            magnitude=5.0
        )
    
    def _generate_star_event(self) -> Event:
        """Generate a new star"""
        from .generators import generate_star_c
        
        # Need at least one galaxy
        total_galaxies = self.state.total_galaxies + self._galaxies_created
        if total_galaxies == 0:
            return self._generate_galaxy_event()
        
        # Pick a random galaxy (from existing or use last created path)
        if self.state.galaxies:
            galaxy = random.choice(self.state.galaxies)
            galaxy_path = galaxy.path
        else:
            # Use a generated galaxy path
            galaxy_num = random.randint(1, max(1, self._galaxies_created))
            cluster_num = (galaxy_num - 1) // 100 + 1
            galaxy_path = f"clusters/cluster-{cluster_num:04d}/galaxies/galaxy-{galaxy_num:04d}"
        
        # Generate star properties
        star_id = f"system-{random.randint(1000, 9999):04d}"
        spectral_class = random.choices(SPECTRAL_CLASSES, SPECTRAL_WEIGHTS)[0]
        
        # Mass based on spectral class
        mass_ranges = {"O": (16, 150), "B": (2.1, 16), "A": (1.4, 2.1), 
                      "F": (1.04, 1.4), "G": (0.8, 1.04), "K": (0.45, 0.8), "M": (0.08, 0.45)}
        mass_range = mass_ranges.get(spectral_class, (0.8, 1.2))
        mass = random.uniform(*mass_range)
        
        sector_id = f"sector-{random.randint(1, 99):04d}"
        star_path = f"{galaxy_path}/sectors/{sector_id}/systems/{star_id}"
        
        star_content = generate_star_c(
            star_id=star_id,
            spectral_class=spectral_class,
            mass_solar=mass,
            life_stage="main_sequence",
            formed_at_commit=self.commit
        )
        
        # Track creation
        self._stars_created += 1
        
        return Event(
            event_type=EventType.STAR_FORM,
            location=star_path,
            description=f"A class {spectral_class} star ignites",
            commit_message=f"form({star_path}): class {spectral_class} star begins nuclear fusion",
            files_to_create=[(f"{star_path}/star.c", star_content)],
            files_to_modify=[],
            magnitude=2.0
        )
    
    def _generate_star_evolution_event(self) -> Event:
        """Evolve an existing star"""
        if not self.state.stars:
            return self._generate_star_event()
        
        star = random.choice(self.state.stars)
        
        # Determine evolution
        evolutions = {
            "protostar": "main_sequence",
            "main_sequence": "subgiant",
            "subgiant": "red_giant",
            "red_giant": "white_dwarf",  # simplified
        }
        
        new_stage = evolutions.get(star.life_stage, star.life_stage)
        
        return Event(
            event_type=EventType.STAR_EVOLVE,
            location=star.path,
            description=f"Star {star.id} evolves to {new_stage}",
            commit_message=f"evolve({star.path}): star transitions to {new_stage} phase",
            files_to_create=[],
            files_to_modify=[(f"{star.path}/star.c", "life_stage", new_stage)],
            magnitude=1.5
        )
    
    def _generate_planet_event(self) -> Event:
        """Generate a new planet"""
        from .generators import generate_planet_py
        
        if not self.state.stars:
            return self._generate_star_event()
        
        star = random.choice(self.state.stars)
        
        planet_num = star.planet_count + 1
        planet_id = f"planet-{planet_num:02d}"
        planet_type = random.choices(PLANET_TYPES, PLANET_WEIGHTS)[0]
        
        # Generate properties based on type
        if planet_type == "terrestrial":
            mass = random.uniform(0.1, 3.0)
            radius = mass ** 0.27  # rough approximation
            orbit = random.uniform(0.5, 2.5)
        elif planet_type == "gas_giant":
            mass = random.uniform(50, 500)
            radius = random.uniform(8, 15)
            orbit = random.uniform(3, 30)
        elif planet_type == "ice_giant":
            mass = random.uniform(10, 50)
            radius = random.uniform(3, 6)
            orbit = random.uniform(15, 50)
        else:  # dwarf
            mass = random.uniform(0.001, 0.1)
            radius = mass ** 0.3
            orbit = random.uniform(30, 100)
        
        planet_path = f"{star.path}/planets/{planet_id}"
        
        planet_content = generate_planet_py(
            planet_id=planet_id,
            planet_type=planet_type,
            mass_earth=mass,
            radius_earth=radius,
            orbit_au=orbit,
            formed_at_commit=self.commit
        )
        
        return Event(
            event_type=EventType.PLANET_FORM,
            location=planet_path,
            description=f"A {planet_type} planet forms around {star.id}",
            commit_message=f"form({planet_path}): {planet_type} world accretes from stellar disk",
            files_to_create=[(f"{planet_path}/planet.py", planet_content)],
            files_to_modify=[],
            magnitude=1.5
        )
    
    def _generate_moon_event(self) -> Event:
        """Generate a moon for an existing planet"""
        from .generators import generate_moon_lua
        
        if not self.state.planets:
            return self._generate_planet_event()
        
        planet = random.choice(self.state.planets)
        moon_num = planet.moon_count + 1
        moon_id = f"moon-{moon_num:02d}"
        
        moon_path = f"{planet.path}/moons/{moon_id}"
        
        moon_content = generate_moon_lua(
            moon_id=moon_id,
            parent_planet=planet.id,
            mass_luna=random.uniform(0.001, 2.0),
            radius_km=random.uniform(100, 3000),
            formed_at_commit=self.commit
        )
        
        return Event(
            event_type=EventType.MOON_FORM,
            location=moon_path,
            description=f"A moon is captured by {planet.id}",
            commit_message=f"form({moon_path}): satellite captured into orbit",
            files_to_create=[(f"{moon_path}/moon.lua", moon_content)],
            files_to_modify=[],
            magnitude=0.5
        )
    
    def _generate_atmosphere_event(self) -> Event:
        """Add atmosphere to a planet"""
        from .generators import generate_atmosphere_json
        
        planets_without_atmo = [p for p in self.state.planets 
                                if not p.has_atmosphere and p.planet_type == "terrestrial"]
        
        if not planets_without_atmo:
            return self._generate_planet_event()
        
        planet = random.choice(planets_without_atmo)
        
        # Generate random atmosphere
        compositions = [
            {"nitrogen": 0.78, "oxygen": 0.21, "argon": 0.01},
            {"carbon_dioxide": 0.96, "nitrogen": 0.03, "argon": 0.01},
            {"nitrogen": 0.90, "methane": 0.05, "hydrogen": 0.05},
            {"hydrogen": 0.80, "helium": 0.19, "methane": 0.01},
        ]
        
        atmo_content = generate_atmosphere_json(
            planet_id=planet.id,
            pressure_atm=random.uniform(0.1, 5.0),
            composition=random.choice(compositions),
            formed_at_commit=self.commit
        )
        
        return Event(
            event_type=EventType.ATMOSPHERE_FORM,
            location=planet.path,
            description=f"Atmosphere develops on {planet.id}",
            commit_message=f"form({planet.path}): atmosphere coalesces from outgassing",
            files_to_create=[(f"{planet.path}/atmosphere.json", atmo_content)],
            files_to_modify=[],
            magnitude=1.0
        )
    
    def _generate_abiogenesis_event(self) -> Event:
        """Life emerges on a suitable planet"""
        from .generators import generate_life_js, generate_chronicle_md
        
        # Find habitable planets without life
        candidates = [p for p in self.state.planets 
                     if p.has_atmosphere and p.has_water and not p.has_life]
        
        if not candidates:
            return self._generate_atmosphere_event()
        
        planet = random.choice(candidates)
        
        life_content = generate_life_js(
            planet_id=planet.id,
            emerged_at_commit=self.commit,
            origin="abiogenesis",
            stage="single_cell",
            species_count=1
        )
        
        chronicle_content = generate_chronicle_md(
            subject_name=f"Life on {planet.id}",
            subject_type="planet",
            emerged_at_commit=self.commit,
            initial_entry="In warm pools rich with chemistry, the first self-replicating molecules appeared. Life had begun."
        )
        
        return Event(
            event_type=EventType.ABIOGENESIS,
            location=planet.path,
            description=f"Life emerges on {planet.id}!",
            commit_message=f"form({planet.path}): ABIOGENESIS - life emerges from primordial chemistry",
            files_to_create=[
                (f"{planet.path}/life.js", life_content),
                (f"{planet.path}/chronicle.md", chronicle_content)
            ],
            files_to_modify=[],
            magnitude=10.0
        )
    
    def _generate_life_evolution_event(self) -> Event:
        """Evolve existing life"""
        if not self.state.life_worlds:
            return self._generate_abiogenesis_event()
        
        life = random.choice(self.state.life_worlds)
        
        evolution_path = {
            "single_cell": "complex_single_cell",
            "complex_single_cell": "multicellular",
            "multicellular": "complex_multicellular",
            "complex_multicellular": "complex_multicellular",  # stays here until intelligence
        }
        
        new_stage = evolution_path.get(life.stage, life.stage)
        new_species = int(life.species_count * random.uniform(1.5, 3.0))
        
        return Event(
            event_type=EventType.LIFE_EVOLVE,
            location=life.planet_path,
            description=f"Life evolves to {new_stage} stage",
            commit_message=f"evolve({life.planet_path}): life advances to {new_stage}",
            files_to_create=[],
            files_to_modify=[(f"{life.planet_path}/life.js", "stage", new_stage)],
            magnitude=3.0
        )
    
    def _generate_intelligence_event(self) -> Event:
        """Intelligence emerges"""
        candidates = [l for l in self.state.life_worlds 
                     if l.stage == "complex_multicellular"]
        
        if not candidates:
            return self._generate_life_evolution_event()
        
        life = random.choice(candidates)
        
        return Event(
            event_type=EventType.INTELLIGENCE,
            location=life.planet_path,
            description="Intelligent life emerges!",
            commit_message=f"form({life.planet_path}): INTELLIGENCE EMERGES - a species begins to wonder",
            files_to_create=[],
            files_to_modify=[(f"{life.planet_path}/life.js", "stage", "intelligent")],
            magnitude=15.0
        )
    
    def _generate_civilization_event(self) -> Event:
        """A civilization emerges"""
        from .generators import generate_civilization_ts, generate_chronicle_md
        
        # Find intelligent life without civilization
        # This is simplified - in reality we'd track this better
        return Event(
            event_type=EventType.CIV_EMERGE,
            location="",
            description="A new civilization emerges",
            commit_message="form: a new civilization takes its first steps",
            files_to_create=[],
            files_to_modify=[],
            magnitude=20.0
        )
    
    def _generate_civ_advance_event(self) -> Event:
        """Civilization advances tech level"""
        if not self.state.civilizations:
            return self._generate_civilization_event()
        
        civ = random.choice([c for c in self.state.civilizations if c.tech_level < 7])
        if not civ:
            return self._generate_colony_event()
        
        new_level = min(civ.tech_level + 1, 7)
        level_name = TECH_LEVELS.get(new_level, "unknown")
        
        return Event(
            event_type=EventType.CIV_ADVANCE,
            location=civ.path,
            description=f"{civ.name} advances to {level_name} age",
            commit_message=f"evolve({civ.path}): {civ.name} enters the {level_name} age",
            files_to_create=[],
            files_to_modify=[(f"{civ.path}/civilization.ts", "tech_level", str(new_level))],
            magnitude=5.0
        )
    
    def _generate_colony_event(self) -> Event:
        """Civilization establishes a colony"""
        spacefaring = [c for c in self.state.civilizations if c.tech_level >= 4]
        
        if not spacefaring:
            return self._generate_civ_advance_event()
        
        civ = random.choice(spacefaring)
        
        return Event(
            event_type=EventType.CIV_EXPAND,
            location=civ.path,
            description=f"{civ.name} establishes a new colony",
            commit_message=f"colony({civ.path}): {civ.name} plants flag on distant world",
            files_to_create=[],
            files_to_modify=[],
            magnitude=4.0
        )
    
    def _generate_first_contact_event(self) -> Event:
        """Two civilizations meet"""
        if len(self.state.civilizations) < 2:
            return self._generate_civilization_event()
        
        civ_a, civ_b = random.sample(self.state.civilizations, 2)
        
        return Event(
            event_type=EventType.FIRST_CONTACT,
            location=civ_a.path,
            description=f"First contact between {civ_a.name} and {civ_b.name}",
            commit_message=f"contact: {civ_a.name} meets {civ_b.name} - history changes forever",
            files_to_create=[],
            files_to_modify=[],
            magnitude=25.0
        )
    
    def _generate_supernova_event(self) -> Event:
        """A star goes supernova"""
        massive_stars = [s for s in self.state.stars 
                        if s.spectral_class in ('O', 'B') or s.life_stage == "red_giant"]
        
        if not massive_stars:
            return self._generate_star_evolution_event()
        
        star = random.choice(massive_stars)
        
        return Event(
            event_type=EventType.SUPERNOVA,
            location=star.path,
            description=f"SUPERNOVA in {star.id}!",
            commit_message=f"event({star.path}): SUPERNOVA - a star dies in cosmic fire",
            files_to_create=[],
            files_to_modify=[(f"{star.path}/star.c", "life_stage", "supernova_remnant")],
            magnitude=50.0
        )
    
    def _generate_anomaly_event(self) -> Event:
        """Generate a cosmic anomaly"""
        from .generators import generate_anomaly_bf
        
        anomaly_types = [
            "spatial_rift", "time_dilation_zone", "dark_matter_concentration",
            "quantum_fluctuation", "wormhole", "void_pocket", "energy_vortex"
        ]
        
        anomaly_id = f"anomaly-{random.randint(1000, 9999)}"
        anomaly_type = random.choice(anomaly_types)
        
        location = "deep space"
        if self.state.galaxies:
            galaxy = random.choice(self.state.galaxies)
            location = f"{galaxy.path}/anomalies"
        
        anomaly_content = generate_anomaly_bf(
            anomaly_id=anomaly_id,
            anomaly_type=anomaly_type,
            location=location,
            danger_level=random.randint(3, 9),
            discovered_at_commit=self.commit
        )
        
        return Event(
            event_type=EventType.ANOMALY,
            location=location,
            description=f"Anomaly detected: {anomaly_type}",
            commit_message=f"event({location}): ANOMALY DETECTED - {anomaly_type} defies explanation",
            files_to_create=[(f"{location}/{anomaly_id}.bf", anomaly_content)],
            files_to_modify=[],
            magnitude=8.0
        )
