"""
Commit Universe Engine - Event Generation

Handles the probabilistic generation of cosmic events based on universe state.
Now with ecosystem evolution, detailed civilizations, and naming.
"""

import random
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum

from .config import (
    EVENT_WEIGHTS, MILESTONES, SPECTRAL_CLASSES, SPECTRAL_WEIGHTS,
    PLANET_TYPES, PLANET_WEIGHTS, GALAXY_TYPES, GALAXY_WEIGHTS,
    CIV_TRAITS, CIV_AGES, GOVERNMENT_TYPES, RELIGION_TYPES,
    FAUNA_STAGES, FLORA_STAGES, TECH_CATEGORIES
)
from .universe import UniverseState, Galaxy, Star, Planet, Life, Civilization


class EventType(Enum):
    # Cosmic
    GALAXY_FORM = "galaxy_form"
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

    # Ecosystem / Life
    LIFE_SPARK = "life_spark"
    EVOLUTION_LEAP = "evolution_leap"
    SPECIES_EMERGE = "species_emerge"
    MASS_EXTINCTION = "mass_extinction"
    FLORA_BLOOM = "flora_bloom"
    INTELLIGENCE_SPARK = "intelligence_spark"

    # Civilization - Internal
    CIV_EMERGE = "civ_emerge"
    AGE_ADVANCE = "age_advance"
    RELIGION_EMERGE = "religion_emerge"
    RELIGION_SCHISM = "religion_schism"
    CULTURE_EMERGE = "culture_emerge"
    GOVERNMENT_CHANGE = "government_change"
    CIVIL_WAR = "civil_war"
    GOLDEN_AGE = "golden_age"
    DARK_AGE = "dark_age"
    GREAT_LEADER = "great_leader"
    PLAGUE = "plague"
    TECH_DISCOVERY = "tech_discovery"
    MIGRATION = "migration"

    # Civilization - External
    FIRST_CONTACT = "first_contact"
    ESTABLISH_TRADE = "establish_trade"
    ALLIANCE_FORM = "alliance_form"
    WAR_DECLARE = "war_declare"
    WAR_BATTLE = "war_battle"
    WAR_END = "war_end"
    CONQUEST = "conquest"
    CULTURAL_EXCHANGE = "cultural_exchange"
    CIV_EXPAND = "civ_expand"

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
        self._cluster_galaxy_counts = {}
        self._cluster_formed_at = {}

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
        possible_events = self._get_possible_events()

        if not possible_events:
            total_galaxies = self.state.total_galaxies + self._galaxies_created
            if self.commit < 1000 or total_galaxies == 0:
                return self._generate_galaxy_event()
            return None

        event_type = self._select_event_type(possible_events)

        generators = {
            # Cosmic
            EventType.GALAXY_FORM: self._generate_galaxy_event,
            EventType.STAR_FORM: self._generate_star_event,
            EventType.STAR_EVOLVE: self._generate_star_evolution_event,
            EventType.SUPERNOVA: self._generate_supernova_event,

            # Planetary
            EventType.PLANET_FORM: self._generate_planet_event,
            EventType.MOON_FORM: self._generate_moon_event,
            EventType.ATMOSPHERE_FORM: self._generate_atmosphere_event,

            # Ecosystem
            EventType.LIFE_SPARK: self._generate_life_spark_event,
            EventType.EVOLUTION_LEAP: self._generate_evolution_event,
            EventType.SPECIES_EMERGE: self._generate_species_event,
            EventType.MASS_EXTINCTION: self._generate_extinction_event,
            EventType.INTELLIGENCE_SPARK: self._generate_intelligence_event,

            # Civilization
            EventType.CIV_EMERGE: self._generate_civilization_event,
            EventType.AGE_ADVANCE: self._generate_age_advance_event,
            EventType.RELIGION_EMERGE: self._generate_religion_event,
            EventType.CULTURE_EMERGE: self._generate_culture_event,
            EventType.GOVERNMENT_CHANGE: self._generate_government_event,
            EventType.TECH_DISCOVERY: self._generate_tech_event,
            EventType.GREAT_LEADER: self._generate_leader_event,
            EventType.GOLDEN_AGE: self._generate_golden_age_event,
            EventType.DARK_AGE: self._generate_dark_age_event,
            EventType.CIV_EXPAND: self._generate_colony_event,

            # Inter-civ
            EventType.FIRST_CONTACT: self._generate_first_contact_event,
            EventType.WAR_DECLARE: self._generate_war_event,
            EventType.ALLIANCE_FORM: self._generate_alliance_event,

            # Special
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

        total_galaxies = self.state.total_galaxies + self._galaxies_created
        total_stars = self.state.total_stars + self._stars_created
        total_planets = self.state.total_planets + self._planets_created

        # Cosmic events
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

        # Ecosystem events
        habitable_planets = [p for p in self.state.planets if p.has_atmosphere]
        if commit >= MILESTONES.get("life_possible", 10000) and habitable_planets:
            possible.append(EventType.LIFE_SPARK)

        if self.state.total_life > 0:
            possible.append(EventType.EVOLUTION_LEAP)
            possible.append(EventType.SPECIES_EMERGE)
            if random.random() < 0.1:  # Rare
                possible.append(EventType.MASS_EXTINCTION)

        # Intelligence
        if commit >= MILESTONES.get("intelligence_possible", 50000):
            advanced_life = [l for l in self.state.life_worlds
                           if l.stage in ("primate", "intelligent", "mammalian")]
            if advanced_life:
                possible.append(EventType.INTELLIGENCE_SPARK)

        # Civilization events
        if commit >= MILESTONES.get("civilization_possible", 60000):
            intelligent_worlds = [l for l in self.state.life_worlds
                                 if l.stage == "intelligent"]
            if intelligent_worlds:
                possible.append(EventType.CIV_EMERGE)

        if self.state.total_civilizations > 0:
            possible.append(EventType.AGE_ADVANCE)
            possible.append(EventType.RELIGION_EMERGE)
            possible.append(EventType.CULTURE_EMERGE)
            possible.append(EventType.GOVERNMENT_CHANGE)
            possible.append(EventType.TECH_DISCOVERY)
            possible.append(EventType.GREAT_LEADER)
            possible.append(EventType.CIV_EXPAND)
            if random.random() < 0.1:
                possible.append(EventType.GOLDEN_AGE)
            if random.random() < 0.05:
                possible.append(EventType.DARK_AGE)

        if self.state.total_civilizations >= 2:
            possible.append(EventType.FIRST_CONTACT)
            possible.append(EventType.WAR_DECLARE)
            possible.append(EventType.ALLIANCE_FORM)

        # Rare events
        if total_stars > 10:
            possible.append(EventType.SUPERNOVA)

        if commit > 10000 and random.random() < 0.01:
            possible.append(EventType.ANOMALY)

        return possible

    def _select_event_type(self, possible: List[EventType]) -> EventType:
        """Select an event type based on weights"""
        weights = []
        for event_type in possible:
            weight = EVENT_WEIGHTS.get(event_type.value, 0.05)
            weights.append(weight)

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

    # ============ COSMIC EVENTS ============

    def _generate_galaxy_event(self) -> Event:
        """Generate a new galaxy"""
        from .generators import generate_galaxy_rs, generate_cluster_toml, generate_galaxy_name, get_random_language_family

        total_galaxies = self.state.total_galaxies + self._galaxies_created
        cluster_num = (total_galaxies // 100) + 1
        cluster_id = f"cluster-{cluster_num:04d}"
        galaxy_id = f"galaxy-{total_galaxies + 1:04d}"

        galaxy_type = random.choices(GALAXY_TYPES, GALAXY_WEIGHTS)[0]
        diameter = random.randint(20000, 150000)

        cluster_path = f"clusters/{cluster_id}"
        galaxy_path = f"{cluster_path}/galaxies/{galaxy_id}"

        galaxy_content = generate_galaxy_rs(
            galaxy_id=galaxy_id,
            galaxy_type=galaxy_type,
            diameter_light_years=diameter,
            formed_at_commit=self.commit
        )

        files_to_create = [(f"{galaxy_path}/galaxy.rs", galaxy_content)]

        self._galaxies_created += 1

        if cluster_id not in self._cluster_galaxy_counts:
            existing_count = sum(1 for g in self.state.galaxies if cluster_id in g.path)
            self._cluster_galaxy_counts[cluster_id] = existing_count
        self._cluster_galaxy_counts[cluster_id] += 1
        new_galaxy_count = self._cluster_galaxy_counts[cluster_id]

        is_new_cluster = cluster_id not in self.state.clusters and cluster_id not in self._clusters_created

        if is_new_cluster:
            formed_at = self.commit
            self._clusters_created.add(cluster_id)
            self._cluster_formed_at[cluster_id] = formed_at
        else:
            if cluster_id in self._cluster_formed_at:
                formed_at = self._cluster_formed_at[cluster_id]
            else:
                cluster_galaxies = [g for g in self.state.galaxies if cluster_id in g.path]
                formed_at = min((g.formed_at_commit for g in cluster_galaxies), default=1)
                self._cluster_formed_at[cluster_id] = formed_at

        cluster_content = generate_cluster_toml(
            cluster_id=cluster_id,
            formed_at_commit=formed_at,
            last_updated_commit=self.commit,
            galaxy_count=new_galaxy_count
        )
        files_to_create.append((f"{cluster_path}/cluster.toml", cluster_content))

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
        """Generate a new star with a name"""
        from .generators import generate_star_c, generate_star_name

        total_galaxies = self.state.total_galaxies + self._galaxies_created
        if total_galaxies == 0:
            return self._generate_galaxy_event()

        if self.state.galaxies:
            galaxy = random.choice(self.state.galaxies)
            galaxy_path = galaxy.path
        else:
            galaxy_num = random.randint(1, max(1, self._galaxies_created))
            cluster_num = (galaxy_num - 1) // 100 + 1
            galaxy_path = f"clusters/cluster-{cluster_num:04d}/galaxies/galaxy-{galaxy_num:04d}"

        star_id = f"system-{random.randint(1000, 9999):04d}"
        spectral_class = random.choices(SPECTRAL_CLASSES, SPECTRAL_WEIGHTS)[0]

        # Scientific designation for now (civs will name them later)
        star_name = generate_star_name(named_by_civ=False)

        mass_ranges = {"O": (16, 150), "B": (2.1, 16), "A": (1.4, 2.1),
                      "F": (1.04, 1.4), "G": (0.8, 1.04), "K": (0.45, 0.8), "M": (0.08, 0.45)}
        mass_range = mass_ranges.get(spectral_class, (0.8, 1.2))
        mass = random.uniform(*mass_range)

        sector_id = f"sector-{random.randint(1, 99):04d}"
        star_path = f"{galaxy_path}/sectors/{sector_id}/systems/{star_id}"

        star_content = generate_star_c(
            star_id=star_id,
            name=star_name,
            spectral_class=spectral_class,
            mass_solar=mass,
            life_stage="main_sequence",
            formed_at_commit=self.commit
        )

        self._stars_created += 1

        return Event(
            event_type=EventType.STAR_FORM,
            location=star_path,
            description=f"A class {spectral_class} star ignites ({star_name})",
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

        evolutions = {
            "protostar": "main_sequence",
            "main_sequence": "subgiant",
            "subgiant": "red_giant",
            "red_giant": "white_dwarf",
        }

        new_stage = evolutions.get(star.life_stage, star.life_stage)

        return Event(
            event_type=EventType.STAR_EVOLVE,
            location=star.path,
            description=f"Star evolves to {new_stage}",
            commit_message=f"evolve({star.path}): star transitions to {new_stage} phase",
            files_to_create=[],
            files_to_modify=[(f"{star.path}/star.c", "life_stage", new_stage)],
            magnitude=1.5
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
            description=f"SUPERNOVA!",
            commit_message=f"event({star.path}): SUPERNOVA - a star dies in cosmic fire",
            files_to_create=[],
            files_to_modify=[(f"{star.path}/star.c", "life_stage", "supernova_remnant")],
            magnitude=50.0
        )

    # ============ PLANETARY EVENTS ============

    def _generate_planet_event(self) -> Event:
        """Generate a new planet"""
        from .generators import generate_planet_py, generate_planet_name

        if not self.state.stars:
            return self._generate_star_event()

        star = random.choice(self.state.stars)

        planet_num = star.planet_count + 1
        planet_id = f"planet-{planet_num:02d}"
        planet_type = random.choices(PLANET_TYPES, PLANET_WEIGHTS)[0]

        # Scientific designation
        planet_name = generate_planet_name(star_name=star.id, named_by_civ=False)

        if planet_type == "terrestrial":
            mass = random.uniform(0.1, 3.0)
            radius = mass ** 0.27
            orbit = random.uniform(0.5, 2.5)
        elif planet_type == "gas_giant":
            mass = random.uniform(50, 500)
            radius = random.uniform(8, 15)
            orbit = random.uniform(3, 30)
        elif planet_type == "ice_giant":
            mass = random.uniform(10, 50)
            radius = random.uniform(3, 6)
            orbit = random.uniform(15, 50)
        else:
            mass = random.uniform(0.001, 0.1)
            radius = mass ** 0.3
            orbit = random.uniform(30, 100)

        planet_path = f"{star.path}/planets/{planet_id}"

        planet_content = generate_planet_py(
            planet_id=planet_id,
            name=planet_name,
            planet_type=planet_type,
            mass_earth=mass,
            radius_earth=radius,
            orbit_au=orbit,
            formed_at_commit=self.commit
        )

        self._planets_created += 1

        return Event(
            event_type=EventType.PLANET_FORM,
            location=planet_path,
            description=f"A {planet_type} planet forms ({planet_name})",
            commit_message=f"form({planet_path}): {planet_type} world accretes from stellar disk",
            files_to_create=[(f"{planet_path}/planet.py", planet_content)],
            files_to_modify=[],
            magnitude=1.5
        )

    def _generate_moon_event(self) -> Event:
        """Generate a moon"""
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

        compositions = [
            {"nitrogen": 0.78, "oxygen": 0.21, "argon": 0.01},
            {"carbon_dioxide": 0.96, "nitrogen": 0.03, "argon": 0.01},
            {"nitrogen": 0.90, "methane": 0.05, "hydrogen": 0.05},
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

    # ============ ECOSYSTEM EVENTS ============

    def _generate_life_spark_event(self) -> Event:
        """Life emerges on a suitable planet"""
        from .generators import generate_ecosystem_js, generate_chronicle_md, determine_biology_type

        candidates = [p for p in self.state.planets
                     if p.has_atmosphere and not p.has_life]

        if not candidates:
            return self._generate_atmosphere_event()

        planet = random.choice(candidates)

        # Determine biology type based on planet
        planet_data = {
            "avg_temp_kelvin": random.randint(200, 400),
            "atmosphere_composition": {"oxygen": 0.21, "nitrogen": 0.78},
            "gravity": 1.0,
            "has_water": True,
            "has_land": True,
        }
        biology = determine_biology_type(planet_data)

        ecosystem_content = generate_ecosystem_js(
            planet_id=planet.id,
            emerged_at_commit=self.commit,
            origin="abiogenesis",
            biology_type=biology.value,
            fauna_stage="primordial_soup",
            flora_stage="microbial_mats",
            fauna_diversity=1,
            flora_diversity=1,
            biomes=["ocean_shallow"],
            ecosystem_status="developing",
            biodiversity_index=0.01
        )

        chronicle_content = generate_chronicle_md(
            subject_name=f"Life on {planet.id}",
            subject_type="ecosystem",
            emerged_at_commit=self.commit,
            initial_entry="In warm pools rich with chemistry, the first self-replicating molecules appeared. Life had begun."
        )

        return Event(
            event_type=EventType.LIFE_SPARK,
            location=planet.path,
            description=f"LIFE EMERGES on {planet.id}!",
            commit_message=f"form({planet.path}): ABIOGENESIS - life sparks from primordial chemistry",
            files_to_create=[
                (f"{planet.path}/ecosystem.js", ecosystem_content),
                (f"{planet.path}/life_chronicle.md", chronicle_content)
            ],
            files_to_modify=[],
            magnitude=10.0
        )

    def _generate_evolution_event(self) -> Event:
        """Life evolves to next stage"""
        if not self.state.life_worlds:
            return self._generate_life_spark_event()

        life = random.choice(self.state.life_worlds)

        # Fauna evolution path
        fauna_path = {
            "primordial_soup": "single_cell",
            "single_cell": "multicellular_simple",
            "multicellular_simple": "aquatic_primitive",
            "aquatic_primitive": "aquatic_complex",
            "aquatic_complex": "amphibian",
            "amphibian": "reptilian",
            "reptilian": "megafauna",
            "megafauna": "mammalian",
            "mammalian": "primate",
            "primate": "intelligent",
        }

        current_stage = life.stage
        new_stage = fauna_path.get(current_stage, current_stage)

        return Event(
            event_type=EventType.EVOLUTION_LEAP,
            location=life.planet_path,
            description=f"Life evolves to {new_stage} stage",
            commit_message=f"evolve({life.planet_path}): life advances to {new_stage.replace('_', ' ')}",
            files_to_create=[],
            files_to_modify=[(f"{life.planet_path}/ecosystem.js", "fauna.stage", new_stage)],
            magnitude=3.0
        )

    def _generate_species_event(self) -> Event:
        """New notable species emerges"""
        from .generators import generate_creature, generate_creature_json, get_random_language_family

        if not self.state.life_worlds:
            return self._generate_life_spark_event()

        life = random.choice(self.state.life_worlds)

        planet_data = {
            "gravity": 1.0,
            "has_water": True,
            "has_land": True,
            "avg_temp_kelvin": 290,
            "atmosphere_composition": {"oxygen": 0.21},
            "star_spectral_class": "G"
        }

        creature = generate_creature(
            planet_data=planet_data,
            language_family=get_random_language_family(),
            discovered_at_commit=self.commit
        )

        creature_content = generate_creature_json(creature)
        creature_path = f"{life.planet_path}/creatures/{creature.id}.json"

        return Event(
            event_type=EventType.SPECIES_EMERGE,
            location=life.planet_path,
            description=f"New species: {creature.common_name}",
            commit_message=f"form({life.planet_path}): {creature.common_name} emerges - {creature.role.value}",
            files_to_create=[(creature_path, creature_content)],
            files_to_modify=[],
            magnitude=1.0
        )

    def _generate_extinction_event(self) -> Event:
        """Mass extinction event"""
        if not self.state.life_worlds:
            return self._generate_life_spark_event()

        life = random.choice(self.state.life_worlds)

        causes = ["asteroid_impact", "volcanic_winter", "gamma_ray_burst",
                  "climate_shift", "ocean_acidification", "pandemic"]
        cause = random.choice(causes)
        severity = random.uniform(0.3, 0.9)

        return Event(
            event_type=EventType.MASS_EXTINCTION,
            location=life.planet_path,
            description=f"MASS EXTINCTION ({cause}): {int(severity*100)}% species lost",
            commit_message=f"extinct({life.planet_path}): MASS EXTINCTION - {cause} devastates biosphere",
            files_to_create=[],
            files_to_modify=[],
            magnitude=15.0
        )

    def _generate_intelligence_event(self) -> Event:
        """Intelligence emerges"""
        candidates = [l for l in self.state.life_worlds
                     if l.stage in ("primate", "mammalian")]

        if not candidates:
            return self._generate_evolution_event()

        life = random.choice(candidates)

        return Event(
            event_type=EventType.INTELLIGENCE_SPARK,
            location=life.planet_path,
            description="INTELLIGENT LIFE EMERGES!",
            commit_message=f"form({life.planet_path}): INTELLIGENCE - a species begins to wonder",
            files_to_create=[],
            files_to_modify=[(f"{life.planet_path}/ecosystem.js", "fauna.stage", "intelligent")],
            magnitude=20.0
        )

    # ============ CIVILIZATION EVENTS ============

    def _generate_civilization_event(self) -> Event:
        """A new civilization emerges from intelligent life"""
        from .generators import (generate_civilization_ts, generate_chronicle_md,
                                generate_name_set_for_civilization, get_random_language_family)

        # Find intelligent life without civilization
        intelligent_worlds = [l for l in self.state.life_worlds if l.stage == "intelligent"]

        if not intelligent_worlds:
            return self._generate_intelligence_event()

        life = random.choice(intelligent_worlds)

        # Generate a complete name set for this civ
        language = get_random_language_family()
        names = generate_name_set_for_civilization(language)

        civ_id = f"civ-{self.commit:05d}"
        civ_path = f"{life.planet_path}/civilizations/{civ_id}"

        # Initial religion
        initial_religion = {
            "id": "rel-001",
            "name": names["primary_religion"],
            "type": random.choice(["animistic", "ancestor_worship", "polytheistic"]),
            "founded_at_commit": self.commit,
            "adherent_percentage": 90,
            "core_beliefs": ["The spirits guide us", "Honor the ancestors"],
            "status": "dominant"
        }

        # Initial culture
        initial_culture = {
            "id": "cul-001",
            "name": f"Core {names['species_name']}",
            "emerged_at_commit": self.commit,
            "values": random.sample(["honor", "knowledge", "tradition", "strength", "harmony"], 2),
            "art_forms": random.sample(["oral_tradition", "cave_painting", "ritual_dance", "music"], 2),
            "population_percentage": 100
        }

        civ_content = generate_civilization_ts(
            civ_id=civ_id,
            name=names["civilization_name"],
            species_name=names["species_name"],
            language_family=language.value,
            homeworld=names["homeworld_name"],
            home_star=names["home_star_name"],
            home_galaxy="",
            emerged_at_commit=self.commit,
            current_age="prehistoric",
            population=random.randint(5000, 50000),
            government="tribe",
            status="emerging",
            religions=[initial_religion],
            cultures=[initial_culture],
            traits=random.sample(CIV_TRAITS, 3)
        )

        chronicle_content = generate_chronicle_md(
            subject_name=names["civilization_name"],
            subject_type="civilization",
            emerged_at_commit=self.commit,
            initial_entry=f"On the world they would call {names['homeworld_name']}, the {names['species_name']} took their first steps toward civilization. They gazed at the stars and wondered."
        )

        return Event(
            event_type=EventType.CIV_EMERGE,
            location=civ_path,
            description=f"CIVILIZATION EMERGES: {names['civilization_name']}",
            commit_message=f"form({civ_path}): {names['civilization_name']} takes its first steps",
            files_to_create=[
                (f"{civ_path}/civilization.ts", civ_content),
                (f"{civ_path}/chronicle.md", chronicle_content)
            ],
            files_to_modify=[(f"{life.planet_path}/ecosystem.js", "fauna.stage", "civilized")],
            magnitude=25.0
        )

    def _generate_age_advance_event(self) -> Event:
        """Civilization advances to next age"""
        if not self.state.civilizations:
            return self._generate_civilization_event()

        # Find civs that can advance
        advanceable = [c for c in self.state.civilizations
                      if CIV_AGES.index(c.current_age) < len(CIV_AGES) - 1]

        if not advanceable:
            return self._generate_tech_event()

        civ = random.choice(advanceable)
        current_idx = CIV_AGES.index(civ.current_age)
        new_age = CIV_AGES[current_idx + 1]

        catalysts = {
            "tribal": "the first settlements form",
            "bronze": "metalworking is discovered",
            "iron": "iron transforms warfare and tools",
            "classical": "philosophy and democracy emerge",
            "medieval": "feudal systems consolidate power",
            "renaissance": "art and science flourish",
            "industrial": "machines change everything",
            "modern": "electricity connects the world",
            "atomic": "the atom is split",
            "information": "digital networks span the globe",
            "space": "they reach for the stars",
            "interplanetary": "colony ships depart",
            "interstellar": "the light barrier falls",
            "galactic": "the galaxy is their home",
            "transcendent": "they become something more",
        }

        return Event(
            event_type=EventType.AGE_ADVANCE,
            location=civ.path,
            description=f"{civ.name} enters the {new_age} age",
            commit_message=f"evolve({civ.path}): {civ.name} enters the {new_age} age - {catalysts.get(new_age, 'history turns')}",
            files_to_create=[],
            files_to_modify=[(f"{civ.path}/civilization.ts", "current_age", new_age)],
            magnitude=8.0
        )

    def _generate_religion_event(self) -> Event:
        """New religion emerges in a civilization"""
        from .generators import generate_religion_name, get_random_language_family

        if not self.state.civilizations:
            return self._generate_civilization_event()

        civ = random.choice(self.state.civilizations)

        religion_type = random.choice(RELIGION_TYPES)
        religion_name = generate_religion_name(get_random_language_family(), religion_type)

        return Event(
            event_type=EventType.RELIGION_EMERGE,
            location=civ.path,
            description=f"New faith emerges: {religion_name}",
            commit_message=f"form({civ.path}): {religion_name} spreads among the {civ.name}",
            files_to_create=[],
            files_to_modify=[],
            magnitude=3.0
        )

    def _generate_culture_event(self) -> Event:
        """New culture emerges"""
        from .generators import generate_culture_name, get_random_language_family

        if not self.state.civilizations:
            return self._generate_civilization_event()

        civ = random.choice(self.state.civilizations)
        culture_name = generate_culture_name(get_random_language_family())

        return Event(
            event_type=EventType.CULTURE_EMERGE,
            location=civ.path,
            description=f"New culture: {culture_name}",
            commit_message=f"form({civ.path}): {culture_name} culture emerges",
            files_to_create=[],
            files_to_modify=[],
            magnitude=2.0
        )

    def _generate_government_event(self) -> Event:
        """Government changes"""
        if not self.state.civilizations:
            return self._generate_civilization_event()

        civ = random.choice(self.state.civilizations)

        # Get valid governments for current age
        valid_govs = GOVERNMENT_TYPES.get(civ.current_age, ["tribe"])
        new_gov = random.choice(valid_govs)

        causes = ["revolution", "reform", "conquest", "succession_crisis", "popular_movement"]
        cause = random.choice(causes)

        return Event(
            event_type=EventType.GOVERNMENT_CHANGE,
            location=civ.path,
            description=f"{civ.name}: {cause} leads to {new_gov}",
            commit_message=f"event({civ.path}): {cause} transforms {civ.name} into {new_gov.replace('_', ' ')}",
            files_to_create=[],
            files_to_modify=[(f"{civ.path}/civilization.ts", "government", new_gov)],
            magnitude=4.0
        )

    def _generate_tech_event(self) -> Event:
        """Technology discovery"""
        if not self.state.civilizations:
            return self._generate_civilization_event()

        civ = random.choice(self.state.civilizations)

        # Pick a tech category and discovery
        category = random.choice(list(TECH_CATEGORIES.keys()))
        techs = TECH_CATEGORIES[category]
        tech = random.choice(techs)

        return Event(
            event_type=EventType.TECH_DISCOVERY,
            location=civ.path,
            description=f"{civ.name} discovers {tech}",
            commit_message=f"discover({civ.path}): {civ.name} unlocks {tech.replace('_', ' ')}",
            files_to_create=[],
            files_to_modify=[],
            magnitude=2.0
        )

    def _generate_leader_event(self) -> Event:
        """Great leader emerges"""
        from .generators import generate_leader_name, get_random_language_family

        if not self.state.civilizations:
            return self._generate_civilization_event()

        civ = random.choice(self.state.civilizations)

        titles = ["Emperor", "Prophet", "General", "Philosopher", "Inventor", "Queen", "King"]
        title = random.choice(titles)
        leader_name = generate_leader_name(get_random_language_family(), title)

        return Event(
            event_type=EventType.GREAT_LEADER,
            location=civ.path,
            description=f"Great leader: {leader_name}",
            commit_message=f"event({civ.path}): {leader_name} rises to shape history",
            files_to_create=[],
            files_to_modify=[],
            magnitude=3.0
        )

    def _generate_golden_age_event(self) -> Event:
        """Civilization enters golden age"""
        if not self.state.civilizations:
            return self._generate_civilization_event()

        civ = random.choice(self.state.civilizations)

        return Event(
            event_type=EventType.GOLDEN_AGE,
            location=civ.path,
            description=f"{civ.name} enters a GOLDEN AGE",
            commit_message=f"event({civ.path}): {civ.name} enters a golden age of prosperity",
            files_to_create=[],
            files_to_modify=[(f"{civ.path}/civilization.ts", "status", "golden_age")],
            magnitude=5.0
        )

    def _generate_dark_age_event(self) -> Event:
        """Civilization enters dark age"""
        if not self.state.civilizations:
            return self._generate_civilization_event()

        civ = random.choice(self.state.civilizations)

        causes = ["plague", "invasion", "civil_war", "climate_disaster", "economic_collapse"]
        cause = random.choice(causes)

        return Event(
            event_type=EventType.DARK_AGE,
            location=civ.path,
            description=f"{civ.name} enters a DARK AGE ({cause})",
            commit_message=f"crisis({civ.path}): {civ.name} falls into darkness - {cause}",
            files_to_create=[],
            files_to_modify=[(f"{civ.path}/civilization.ts", "status", "declining")],
            magnitude=6.0
        )

    def _generate_colony_event(self) -> Event:
        """Civilization establishes a colony"""
        from .generators import generate_planet_name, get_random_language_family

        spacefaring_ages = ["space", "interplanetary", "interstellar", "galactic"]
        spacefaring = [c for c in self.state.civilizations if c.current_age in spacefaring_ages]

        if not spacefaring:
            return self._generate_age_advance_event()

        civ = random.choice(spacefaring)
        colony_name = generate_planet_name(get_random_language_family(), named_by_civ=True)

        return Event(
            event_type=EventType.CIV_EXPAND,
            location=civ.path,
            description=f"{civ.name} founds colony: {colony_name}",
            commit_message=f"colony({civ.path}): {civ.name} establishes {colony_name}",
            files_to_create=[],
            files_to_modify=[],
            magnitude=4.0
        )

    # ============ INTER-CIV EVENTS ============

    def _generate_first_contact_event(self) -> Event:
        """Two civilizations meet"""
        if len(self.state.civilizations) < 2:
            return self._generate_civilization_event()

        civ_a, civ_b = random.sample(self.state.civilizations, 2)

        return Event(
            event_type=EventType.FIRST_CONTACT,
            location=civ_a.path,
            description=f"FIRST CONTACT: {civ_a.name} meets {civ_b.name}",
            commit_message=f"contact: {civ_a.name} and {civ_b.name} discover they are not alone",
            files_to_create=[],
            files_to_modify=[],
            magnitude=30.0
        )

    def _generate_war_event(self) -> Event:
        """War breaks out"""
        from .generators import generate_war_name, get_random_language_family

        if len(self.state.civilizations) < 2:
            return self._generate_civilization_event()

        civ_a, civ_b = random.sample(self.state.civilizations, 2)
        war_name = generate_war_name(get_random_language_family(), civ_b.name)

        causes = ["territorial_dispute", "resource_conflict", "ideological",
                  "religious", "succession", "honor"]
        cause = random.choice(causes)

        return Event(
            event_type=EventType.WAR_DECLARE,
            location=civ_a.path,
            description=f"WAR: {war_name}",
            commit_message=f"war({civ_a.path}): {war_name} begins - {cause}",
            files_to_create=[],
            files_to_modify=[],
            magnitude=10.0
        )

    def _generate_alliance_event(self) -> Event:
        """Alliance forms"""
        from .generators import generate_treaty_name, get_random_language_family

        if len(self.state.civilizations) < 2:
            return self._generate_civilization_event()

        civ_a, civ_b = random.sample(self.state.civilizations, 2)
        treaty_name = generate_treaty_name(get_random_language_family())

        return Event(
            event_type=EventType.ALLIANCE_FORM,
            location=civ_a.path,
            description=f"Alliance: {treaty_name}",
            commit_message=f"peace({civ_a.path}): {civ_a.name} and {civ_b.name} sign {treaty_name}",
            files_to_create=[],
            files_to_modify=[],
            magnitude=5.0
        )

    # ============ SPECIAL EVENTS ============

    def _generate_anomaly_event(self) -> Event:
        """Generate a cosmic anomaly"""
        from .generators import generate_anomaly_bf

        anomaly_types = ["spatial_rift", "time_dilation_zone", "dark_matter_concentration",
                        "quantum_fluctuation", "wormhole", "void_pocket"]

        anomaly_id = f"anomaly-{random.randint(1000, 9999)}"
        anomaly_type = random.choice(anomaly_types)

        location = "deep_space"
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
            description=f"ANOMALY: {anomaly_type}",
            commit_message=f"event({location}): ANOMALY - {anomaly_type.replace('_', ' ')} defies explanation",
            files_to_create=[(f"{location}/{anomaly_id}.bf", anomaly_content)],
            files_to_modify=[],
            magnitude=8.0
        )
