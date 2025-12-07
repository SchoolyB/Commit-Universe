# Civilization System Overhaul - Work Tracker

> Major patch to transform civilizations from simple counters into rich, detailed entities with history, culture, religion, and meaningful interactions.

---

## Overview

**Goal:** Make civilizations the richest, most detailed part of the simulation. Every civ should feel unique with its own history, culture, beliefs, and trajectory.

**Scope:**
- Name generation system
- Planetary ecosystems (flora, fauna, evolution, extinctions)
- Complete civilization system rewrite
- New event types (~40+ new events)
- Enhanced chronicle generation
- Inter-civilization interactions

---

## Phase 0: Planetary Ecosystems

### 0.1 Planet Life Status
Not all planets get life. Many remain barren forever. Those that do develop life follow evolutionary stages:

```
PLANETARY_LIFE_STAGES = [
    "barren",              # No life, never will be (too hot, too cold, no atmosphere)
    "prebiotic",           # Organic chemistry happening, no life yet
    "primordial_soup",     # Complex molecules, almost life
    "single_cell",         # First prokaryotes
    "multicellular_simple", # Bacterial mats, early multicellular
    "aquatic_primitive",   # Simple sea life, jellyfish-types
    "aquatic_complex",     # Fish, crustaceans, mollusks
    "amphibian",           # Life moves to land
    "reptilian",           # Reptiles dominate
    "megafauna",           # Dinosaur-equivalents, massive creatures
    "mammalian",           # Mammals rise (or equivalent)
    "primate",             # Complex social animals
    "intelligent",         # Tool users, pre-civilization
    "civilized"            # Hands off to civilization system
]
```

### 0.2 Flora Progression
```
FLORA_STAGES = [
    "none",
    "microbial_mats",      # Bacterial films
    "algae",               # Simple aquatic plants
    "moss_lichen",         # First land plants
    "ferns",               # Primitive vascular plants
    "forests",             # Trees emerge
    "flowering",           # Angiosperms, complex ecosystems
    "mega_flora"           # Giant plant life
]
```

### 0.3 Ecosystem Structure
```python
interface Ecosystem {
    planet_id: string;
    status: "barren" | "developing" | "thriving" | "dying" | "dead";

    # Fauna
    fauna_stage: FaunaStage;
    fauna_diversity: number;  # Species count estimate
    apex_predators: Creature[];
    notable_species: Creature[];

    # Flora
    flora_stage: FloraStage;
    flora_coverage: number;  # 0.0 - 1.0
    dominant_biomes: Biome[];

    # History
    emergence_commit: number;
    mass_extinctions: MassExtinction[];
    current_extinction_risk: number;
}
```

### 0.4 Creature Generation
- [ ] Create `engine/generators/creature_gen.py`
- [ ] Generate creature types based on planet conditions:
  - Gravity affects size
  - Atmosphere affects respiration
  - Star type affects vision
  - Water availability affects biology
- [ ] Creature properties:
  - Name (procedural)
  - Type (herbivore, carnivore, omnivore, filter-feeder, etc.)
  - Size class
  - Intelligence level
  - Notable traits
  - Population status

### 0.5 Biome Types
```
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
    "underground"
]
```

### 0.6 Ecosystem Events
- [ ] `LIFE_SPARK` - First life appears
- [ ] `EVOLUTION_LEAP` - Major evolutionary transition
- [ ] `SPECIES_EMERGE` - Notable species appears
- [ ] `APEX_CHANGE` - New apex predator
- [ ] `MASS_EXTINCTION` - Catastrophic die-off (asteroid, volcano, etc.)
- [ ] `RECOVERY` - Life bounces back post-extinction
- [ ] `FLORA_BLOOM` - Plant life explosion
- [ ] `OCEAN_TO_LAND` - Life colonizes land
- [ ] `MEGAFAUNA_ERA` - Giant creatures dominate
- [ ] `INTELLIGENCE_SPARK` - Pre-civ intelligence emerges

### 0.7 Alternative Biologies
Not all life is Earth-like:
- [ ] Carbon-based (Earth-like)
- [ ] Silicon-based (high temp worlds)
- [ ] Ammonia-based (cold worlds)
- [ ] Aquatic-only (no land life, water world civs)
- [ ] Hive organisms (collective intelligence)
- [ ] Crystalline (exotic)
- [ ] Energy beings (late-stage evolution)

### 0.8 Life Files Structure
```
planet-XX/
├── planet.py           # Basic planet data
├── atmosphere.json     # Atmosphere composition
├── ecosystem.js        # Overall ecosystem state (JavaScript - chaotic life)
├── creatures/
│   ├── apex-001.json   # Notable creatures
│   └── apex-002.json
├── biomes.json         # Biome distribution
├── extinction_log.md   # History of mass extinctions
└── life_chronicle.md   # Evolution story
```

---

## Phase 1: Foundation Systems

### 1.1 Name Generator
- [ ] Create `engine/generators/name_gen.py`
- [ ] Implement linguistic syllable patterns (CV, CVC, VC structures)
- [ ] Create multiple "language families" for different civ cultures
- [ ] Name types needed:
  - [ ] Star names
  - [ ] Planet names
  - [ ] Civilization names
  - [ ] Species names
  - [ ] Religion names
  - [ ] Leader/historical figure names
  - [ ] City/settlement names
  - [ ] Cultural movement names
- [ ] Each civ gets assigned a language family for consistent naming

### 1.2 Update Existing Generators
- [ ] `python_gen.py` - planets accept optional names
- [ ] `c_gen.py` - stars accept optional names
- [ ] `rust_gen.py` - galaxies accept optional names
- [ ] `ts_gen.py` - complete rewrite for detailed civs
- [ ] `markdown_gen.py` - enhanced chronicle generation

---

## Phase 2: Civilization Data Model

### 2.1 Ages/Eras System
Replace simple tech_level (0-7) with granular ages:

```
AGES = [
    "prehistoric",      # 0 - Hunter-gatherers, fire, basic tools
    "tribal",           # 1 - Organized tribes, shamanism, oral tradition
    "bronze",           # 2 - Early metallurgy, first cities, writing
    "iron",             # 3 - Advanced metallurgy, empires, philosophy
    "classical",        # 4 - Golden age of culture, mathematics, democracy
    "medieval",         # 5 - Feudalism, organized religion dominates
    "renaissance",      # 6 - Scientific revolution begins, exploration
    "industrial",       # 7 - Machines, urbanization, nation-states
    "modern",           # 8 - Electricity, global communication
    "atomic",           # 9 - Nuclear power, early computing, cold wars
    "information",      # 10 - Digital revolution, global networks
    "space",            # 11 - First spaceflight, orbital presence
    "interplanetary",   # 12 - Colony ships, solar system colonization
    "interstellar",     # 13 - FTL or generation ships, nearby stars
    "galactic",         # 14 - Galaxy-spanning presence
    "transcendent"      # 15 - Post-physical, ascended, incomprehensible
]
```

- [ ] Define age progression requirements
- [ ] Define events possible at each age
- [ ] Define typical age duration (in commits)

### 2.2 Civilization Core Structure
```typescript
interface Civilization {
    // Identity
    id: string;
    name: string;
    species_name: string;
    language_family: string;  // For name generation

    // Location
    homeworld: string;
    home_star: string;
    home_galaxy: string;
    controlled_systems: string[];
    colonies: Colony[];

    // Timeline
    emerged_at_commit: number;
    current_age: Age;
    age_history: AgeTransition[];

    // Demographics
    population: number;
    population_growth_rate: number;
    subspecies: Subspecies[];  // Divergent populations

    // Society
    government: Government;
    governments_history: GovernmentChange[];
    religions: Religion[];
    cultures: Culture[];
    factions: Faction[];

    // Technology
    tech_discoveries: Discovery[];
    current_tech_focus: string;

    // External
    known_civs: CivRelation[];
    active_wars: War[];
    active_treaties: Treaty[];

    // Status
    status: CivStatus;
    golden_ages: number;
    dark_ages: number;
}
```

### 2.3 Religion System
- [ ] Define `Religion` interface
```typescript
interface Religion {
    id: string;
    name: string;
    founder: string | null;  // null = organic emergence
    founded_at_commit: number;
    type: "polytheistic" | "monotheistic" | "philosophical" | "animistic" | "ancestor_worship" | "cosmic" | "machine_cult";
    core_beliefs: string[];
    adherent_percentage: number;
    holy_sites: string[];  // Planet/location paths
    schisms: Religion[];  // Child religions from splits
    status: "emerging" | "dominant" | "declining" | "underground" | "extinct";
}
```
- [ ] Religion emergence events
- [ ] Schism/reformation events
- [ ] Holy war events
- [ ] Religion spread mechanics

### 2.4 Culture System
- [ ] Define `Culture` interface
```typescript
interface Culture {
    id: string;
    name: string;
    parent_culture: string | null;
    emerged_at_commit: number;
    traits: CultureTrait[];
    art_forms: string[];
    values: string[];  // "honor", "knowledge", "expansion", etc.
    taboos: string[];
    current_movement: string | null;  // "golden age of poetry", "rationalist revolution"
}
```
- [ ] Culture drift over time
- [ ] Cultural exchange between civs
- [ ] Art/philosophical movements
- [ ] Cultural victories/dominance

### 2.5 Government System
- [ ] Define government types by age
```
prehistoric: band, tribe
tribal: chiefdom, tribal_council
bronze: city_state, early_kingdom, theocracy
iron: empire, republic, oligarchy
classical: democracy, bureaucratic_empire
medieval: feudalism, absolute_monarchy, religious_state
renaissance: constitutional_monarchy, merchant_republic
industrial: nation_state, colonial_empire, early_democracy
modern: democracy, authoritarian, communist_state
atomic: superpower_bloc, united_nations_type
information: corporate_state, direct_democracy, surveillance_state
space: planetary_government, orbital_corporate
interplanetary: system_federation, colonial_administration
interstellar: stellar_empire, confederation, hive_consensus
galactic: galactic_council, transcendent_collective
```
- [ ] Revolution/government change events
- [ ] Civil war events
- [ ] Reform events

### 2.6 Technology Tree
- [ ] Define tech categories:
  - Survival (fire, agriculture, medicine)
  - Materials (bronze, iron, steel, composites, exotic matter)
  - Energy (muscle, wind, steam, electric, nuclear, fusion, zero-point)
  - Information (writing, printing, telegraph, radio, internet, quantum)
  - Transport (wheel, sail, engine, rocket, FTL)
  - Weapons (spear, bow, gunpowder, nuclear, planet-killer)
  - Biology (breeding, medicine, genetics, uplift, immortality)
- [ ] Tech discovery events
- [ ] Tech sharing between civs
- [ ] Tech lost during dark ages

---

## Phase 3: Event System Expansion

### 3.1 Internal Civ Events
- [ ] `AGE_ADVANCE` - Civ enters new age
- [ ] `RELIGION_EMERGE` - New religion founded
- [ ] `RELIGION_SCHISM` - Religion splits
- [ ] `RELIGION_SPREAD` - Religion crosses borders
- [ ] `HOLY_WAR` - Religious conflict
- [ ] `CULTURE_EMERGE` - New culture develops
- [ ] `CULTURAL_MOVEMENT` - Renaissance, enlightenment, etc.
- [ ] `GOVERNMENT_CHANGE` - Revolution, reform, coup
- [ ] `CIVIL_WAR` - Internal conflict
- [ ] `GOLDEN_AGE` - Period of prosperity
- [ ] `DARK_AGE` - Collapse, regression
- [ ] `GREAT_LEADER` - Influential figure emerges
- [ ] `PLAGUE` - Disease devastates population
- [ ] `TECH_DISCOVERY` - New technology unlocked
- [ ] `TECH_LOST` - Knowledge lost (dark age, war)
- [ ] `MIGRATION` - Population movement
- [ ] `DIASPORA` - Forced population scatter
- [ ] `UNIFICATION` - Factions unite
- [ ] `FACTION_SPLIT` - Civ fragments

### 3.2 Inter-Civ Events
- [ ] `FIRST_CONTACT` - Two civs meet (already exists, enhance)
- [ ] `ESTABLISH_TRADE` - Trade route opens
- [ ] `TRADE_WAR` - Economic conflict
- [ ] `DIPLOMATIC_MARRIAGE` - Alliance through union
- [ ] `ALLIANCE_FORM` - Military/political alliance
- [ ] `ALLIANCE_BREAK` - Alliance dissolves
- [ ] `WAR_DECLARE` - Open warfare begins
- [ ] `WAR_BATTLE` - Battle occurs
- [ ] `WAR_END` - Peace treaty or surrender
- [ ] `CONQUEST` - One civ absorbs another
- [ ] `VASSAL` - Tributary relationship
- [ ] `CULTURAL_EXCHANGE` - Civs share culture
- [ ] `RELIGIOUS_CONVERSION` - Civ adopts foreign religion
- [ ] `TECH_TRADE` - Technology exchanged
- [ ] `JOINT_COLONY` - Civs colonize together
- [ ] `GALACTIC_COUNCIL` - Multi-civ organization forms

### 3.3 Event Weighting by Age
- [ ] Define which events can happen at which ages
- [ ] Define probability weights per age
- [ ] Earlier ages: more internal focus
- [ ] Later ages: more external/inter-civ focus

---

## Phase 4: Chronicle Enhancement

### 4.1 Rich Chronicle Entries
- [ ] Age transition narratives
- [ ] Religion founding stories
- [ ] War chronicles with battles
- [ ] Great leader biographies
- [ ] Cultural movement descriptions
- [ ] First contact stories
- [ ] Colony founding narratives

### 4.2 Chronicle Structure
```markdown
# Chronicle of [Civ Name]

## The Beginning (Commit #X)
[Emergence story]

## The Age of [Age Name] (Commits #X - #Y)
### [Year/Period]
[Events of this period]

### The [Religion] Faith
[Religion emergence story]

### The Great [Leader Name]
[Biography]

## Relations
### First Contact with [Other Civ]
[Story]

### The [War Name] (Commits #X - #Y)
[War narrative]
```

---

## Phase 5: File Structure Updates

### 5.1 New Files Per Civ
```
civilization-XXXX/
├── civilization.ts      # Main civ data
├── chronicle.md         # Full history
├── religions/
│   ├── religion-01.json
│   └── religion-02.json
├── cultures/
│   └── culture-01.json
├── leaders/
│   └── leader-01.json
├── wars/
│   └── war-01.json
└── treaties/
    └── treaty-01.json
```

### 5.2 Update Universe Reader
- [ ] Parse new civ structure
- [ ] Track religions, cultures, leaders
- [ ] Track inter-civ relations

---

## Phase 6: Integration & Testing

### 6.1 Update events.py
- [ ] Integrate all new event types
- [ ] Update event probability system
- [ ] Add age-based event filtering
- [ ] Add inter-civ event logic

### 6.2 Update main.py
- [ ] Handle new file types
- [ ] Update epoch tracking for civ-heavy eras

### 6.3 Local Testing
- [ ] Run simulation for 1000+ commits
- [ ] Verify age progression
- [ ] Verify religion/culture emergence
- [ ] Verify inter-civ events
- [ ] Check chronicle readability
- [ ] Performance testing

---

## Implementation Order

1. **Name Generator** - Foundation for everything else
2. **Creature Generator** - Procedural fauna/flora
3. **Ecosystem System** - Planet life stages, biomes
4. **Ecosystem Events** - Evolution, extinctions, etc.
5. **Age System** - Replace tech_level with 16 ages
6. **Enhanced CivData** - New TypeScript structure
7. **Religion System** - Beliefs and conflicts
8. **Culture System** - Identity and drift
9. **Government System** - Politics and revolution
10. **Tech Tree** - Detailed progression
11. **Internal Civ Events** - All the new civ events
12. **Inter-Civ Events** - Relations and wars
13. **Chronicle Enhancement** - Rich storytelling
14. **Integration** - Wire it all together
15. **Testing** - Local simulation runs

---

## Notes

- Keep backward compatibility where possible
- Civs should feel ALIVE, not just data
- Chronicles should be readable as actual stories
- Names should be pronounceable and memorable
- Each civ should feel genuinely unique

---

## Progress

**Status:** NOT STARTED

**Current Phase:** Planning Complete

**Next Step:** Begin Phase 1.1 - Name Generator
