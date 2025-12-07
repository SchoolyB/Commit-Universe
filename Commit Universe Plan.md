# Commit Universe

> A procedurally generated universe that evolves through git commits.

---

## The Concept

Commit Universe is a GitHub repository where **the repo itself is the universe**. The code doesn't run or execute anything meaningful—it simply holds data representing cosmic objects: galaxies, stars, planets, and civilizations.

**The magic is in the commits.**

Hundreds of automated commits happen daily, each representing an event in the universe: a star ignites, a planet forms, a civilization rises, another falls. Over time, the repo grows to massive scale—millions of lines of "code" (really data and history), tens of thousands of commits—telling the emergent story of an entire universe.

Think of it as a cosmic ant farm, played out through version control.

---

## Core Philosophy

| Element | What It Represents |
|---------|-------------------|
| The repository | The universe (frozen state at any moment) |
| Commits | Time passing (events happening) |
| Files & directories | Cosmic objects (galaxies, stars, planets, life) |
| Lines of code | History and accumulated state |
| Pull requests | Divine intervention (community participation) |
| Commit messages | The narrative (story of the universe) |

The repo doesn't DO anything. It just IS. The simulation engine that creates commits lives elsewhere (GitHub Actions or external cron). The Commit Universe repo is pure data—a living document of cosmic history.

---

## Goals

1. **Massive scale** — Grow to Linux-kernel-level LOC and commit counts
2. **Emergent storytelling** — Each commit adds to an unfolding narrative
3. **Community participation** — People can interact via PRs and issues
4. **Longevity** — Runs indefinitely, always evolving
5. **Discoverable** — Anyone can explore the universe by browsing the repo

---

## Commit Cadence

- **Target:** 200-500 commits per day
- **Frequency:** Every 3-7 minutes (randomized for organic feel)
- **Method:** GitHub Actions on a schedule, or external cron job

---

## Time Scale

Each commit represents a variable amount of cosmic time depending on what's happening:

| Era | Time per commit |
|-----|-----------------|
| Early universe (first 1000 commits) | ~10 million years |
| Galaxy formation | ~1 million years |
| Stellar evolution | ~100,000 years |
| Planetary development | ~10,000 years |
| Civilization emergence | ~100-1000 years |
| Space age civilizations | ~1-10 years |

Time compresses as interesting things happen. A lonely gas giant might not get a commit for weeks. A thriving civilization might get several per hour.

---

## Universe Structure

```
commit-universe/
│
├── README.md                         # Universe overview, stats, age
├── CONSTANTS.yaml                    # Fundamental physics constants
├── epoch.yaml                        # Current cosmic time, commit count
├── index.yaml                        # Master index of all objects
│
├── clusters/                         # Galaxy clusters
│   ├── cluster-0001/
│   │   ├── cluster.yaml              # Cluster metadata
│   │   │
│   │   ├── galaxies/
│   │   │   ├── galaxy-0001/
│   │   │   │   ├── galaxy.yaml       # Galaxy type, age, size
│   │   │   │   │
│   │   │   │   ├── sectors/
│   │   │   │   │   ├── sector-0001/
│   │   │   │   │   │   ├── sector.yaml
│   │   │   │   │   │   │
│   │   │   │   │   │   ├── systems/
│   │   │   │   │   │   │   ├── system-0001/
│   │   │   │   │   │   │   │   ├── star.yaml
│   │   │   │   │   │   │   │   ├── planets/
│   │   │   │   │   │   │   │   │   ├── planet-01/
│   │   │   │   │   │   │   │   │   │   ├── planet.yaml
│   │   │   │   │   │   │   │   │   │   ├── moons/
│   │   │   │   │   │   │   │   │   │   ├── atmosphere.yaml
│   │   │   │   │   │   │   │   │   │   ├── geology.yaml
│   │   │   │   │   │   │   │   │   │   ├── life.yaml          # If life exists
│   │   │   │   │   │   │   │   │   │   ├── civilization.yaml  # If sapient
│   │   │   │   │   │   │   │   │   │   └── chronicle.md       # History log
```

---

## Multi-Language Universe

The codebase is intentionally polyglot. Since nothing actually executes, we use **real programming languages** to store cosmic data—making the repo feel like genuine code while being purely declarative state.

### Language Assignments

| Cosmic Object | Language | Why |
|---------------|----------|-----|
| Universe constants | Go | Constants feel natural in Go |
| Galaxy clusters | TOML | Config-like, hierarchical |
| Galaxies | Rust | Structs, strong typing aesthetic |
| Stars | C | Low-level, foundational |
| Planets | Python | Readable, scientific feel |
| Moons | Lua | Small, lightweight |
| Atmospheres | JSON | Pure data |
| Life | JavaScript | Chaotic, unpredictable |
| Civilizations | TypeScript | More structured than life |
| Chronicles | Markdown | Narrative text |
| Indexes/Registries | SQL | Database-like catalogs |
| Anomalies | Brainfuck/Befunge | Weird things get weird languages |
| Ancient ruins | COBOL | Old things get old languages |

This creates a genuinely diverse codebase where language stats look organic and interesting.

---

## File Types & What They Store

### constants.go
```go
package universe

// Fundamental constants - set at the Big Bang, immutable forever
const (
    SpeedOfLight       = 299792458       // m/s
    GravitationalConst = 6.67430e-11     // m³/(kg·s²)
    PlanckConstant     = 6.62607015e-34  // J·Hz⁻¹
    BoltzmannConstant  = 1.380649e-23    // J/K
    
    UniverseSeed       = 84729           // RNG seed for this timeline
    BigBangCommit      = 1               // The first commit
    CosmicAge          = 0               // Updated each commit (millions of years)
)
```

### cluster.toml
```toml
[cluster]
id = "cluster-0001"
name = "Primordial Cluster Alpha"
formed_at_commit = 87
age_billion_years = 12.1

[cluster.position]
x = 0.0
y = 0.0
z = 0.0

[cluster.stats]
galaxy_count = 47
total_mass_solar = 1.2e15
diameter_mly = 12.4
```

### galaxy.rs
```rust
pub struct Galaxy {
    pub id: String,
    pub name: Option<String>,
    pub classification: GalaxyType,
    pub age_billion_years: f64,
    pub diameter_light_years: u64,
    pub star_count: u64,
    pub formed_at_commit: u64,
    pub discovered_by: Option<String>,
}

pub enum GalaxyType {
    Spiral,
    Elliptical,
    Irregular,
    Lenticular,
}

pub const GALAXY_0001: Galaxy = Galaxy {
    id: "galaxy-0001",
    name: None,
    classification: GalaxyType::Spiral,
    age_billion_years: 4.2,
    diameter_light_years: 87_000,
    star_count: 147_832,
    formed_at_commit: 847,
    discovered_by: None,
};
```

### star.c
```c
#ifndef STAR_SYSTEM_0001_H
#define STAR_SYSTEM_0001_H

typedef enum {
    SPECTRAL_O, SPECTRAL_B, SPECTRAL_A, SPECTRAL_F,
    SPECTRAL_G, SPECTRAL_K, SPECTRAL_M
} SpectralClass;

typedef enum {
    STAGE_PROTOSTAR,
    STAGE_MAIN_SEQUENCE,
    STAGE_RED_GIANT,
    STAGE_WHITE_DWARF,
    STAGE_NEUTRON_STAR,
    STAGE_BLACK_HOLE
} LifeStage;

struct Star {
    char id[32];
    char name[64];
    SpectralClass spectral_class;
    double mass_solar;
    double age_billion_years;
    LifeStage life_stage;
    int planet_count;
    double habitable_zone_inner_au;
    double habitable_zone_outer_au;
    unsigned long formed_at_commit;
};

static const struct Star SYSTEM_0001 = {
    .id = "system-0001",
    .name = "",
    .spectral_class = SPECTRAL_G,
    .mass_solar = 1.04,
    .age_billion_years = 3.1,
    .life_stage = STAGE_MAIN_SEQUENCE,
    .planet_count = 4,
    .habitable_zone_inner_au = 0.95,
    .habitable_zone_outer_au = 1.37,
    .formed_at_commit = 12847
};

#endif
```

### planet.py
```python
"""Planet definition for system-0001, planet 03"""

from dataclasses import dataclass
from typing import Optional
from enum import Enum

class PlanetType(Enum):
    GAS_GIANT = "gas_giant"
    ICE_GIANT = "ice_giant"
    TERRESTRIAL = "terrestrial"
    DWARF = "dwarf"

@dataclass
class Planet:
    id: str
    name: Optional[str]
    planet_type: PlanetType
    mass_earth: float
    radius_earth: float
    orbit_au: float
    orbit_days: float
    moon_count: int
    has_atmosphere: bool
    has_water: bool
    has_life: bool
    has_intelligent_life: bool
    formed_at_commit: int

PLANET_03 = Planet(
    id="planet-03",
    name=None,
    planet_type=PlanetType.TERRESTRIAL,
    mass_earth=0.92,
    radius_earth=0.97,
    orbit_au=1.08,
    orbit_days=391,
    moon_count=1,
    has_atmosphere=True,
    has_water=True,
    has_life=True,
    has_intelligent_life=False,
    formed_at_commit=14293
)
```

### moon.lua
```lua
-- Moon definition: planet-03, moon-01

local Moon = {
    id = "moon-01",
    name = nil,
    parent_planet = "planet-03",
    
    mass_luna = 0.012,      -- relative to Earth's moon
    radius_km = 174,
    orbital_period_days = 6.2,
    tidally_locked = true,
    
    surface = {
        composition = "silicate",
        craters = 2847,
        largest_crater_km = 89
    },
    
    formed_at_commit = 14301,
    formed_by = "capture"   -- capture, accretion, impact
}

return Moon
```

### atmosphere.json
```json
{
    "planet_id": "planet-03",
    "pressure_atm": 0.89,
    "composition": {
        "nitrogen": 0.72,
        "oxygen": 0.21,
        "argon": 0.04,
        "carbon_dioxide": 0.02,
        "trace": 0.01
    },
    "layers": [
        {"name": "troposphere", "height_km": 12},
        {"name": "stratosphere", "height_km": 50},
        {"name": "mesosphere", "height_km": 85},
        {"name": "thermosphere", "height_km": 600}
    ],
    "average_temp_kelvin": 287,
    "greenhouse_effect": true,
    "ozone_layer": true,
    "formed_at_commit": 15729
}
```

### life.js
```javascript
/**
 * Life on planet-03
 * Status: Complex multicellular
 */

const life = {
    planet_id: "planet-03",
    emerged_at_commit: 847293,
    origin: "abiogenesis",  // abiogenesis, panspermia, seeded
    
    // Current state
    stage: "complex_multicellular",
    // Options: prebiotic, single_cell, multicellular, complex_multicellular, 
    //          intelligent, civilized, spacefaring, transcendent, extinct
    
    domains: 3,
    species_count: 8_429_117,
    
    milestones: [
        { commit: 847293, event: "first replicating molecules" },
        { commit: 851000, event: "prokaryotic cells emerge" },
        { commit: 892000, event: "photosynthesis develops" },
        { commit: 894000, event: "great oxygenation event" },
        { commit: 923000, event: "eukaryotic cells emerge" },
        { commit: 961000, event: "multicellular life" },
        { commit: 984200, event: "cambrian explosion equivalent" },
    ],
    
    dominant_form: {
        type: "vertebrate-analog",
        locomotion: "quadruped",
        respiration: "oxygen",
        avg_lifespan_years: 40
    },
    
    extinction_events: 2,
    current_biodiversity_index: 0.73
};

module.exports = life;
```

### civilization.ts
```typescript
interface Civilization {
    id: string;
    name: string;
    species: string;
    homeworld: string;
    emerged_at_commit: number;
    tech_level: TechLevel;
    population: number;
    colonies: string[];
    traits: CivTrait[];
    status: CivStatus;
}

enum TechLevel {
    Stone = 0,
    Agricultural = 1,
    Industrial = 2,
    Atomic = 3,
    Spacefaring = 4,
    Interstellar = 5,
    Galactic = 6,
    Transcendent = 7
}

type CivTrait = 
    | "curious" | "aggressive" | "peaceful" | "isolationist"
    | "expansionist" | "spiritual" | "logical" | "artistic"
    | "long-lived" | "short-lived" | "hive-mind" | "individualist";

type CivStatus = "emerging" | "active" | "dormant" | "declining" | "extinct" | "transcended";

const THE_KETHARI: Civilization = {
    id: "civ-00147",
    name: "The Kethari",
    species: "kethari",
    homeworld: "clusters/cluster-0001/galaxies/galaxy-0001/sectors/sector-0012/systems/system-0847/planets/planet-02",
    emerged_at_commit: 984729,
    tech_level: TechLevel.Spacefaring,
    population: 8_400_000_000,
    colonies: [
        "clusters/cluster-0001/galaxies/galaxy-0001/sectors/sector-0012/systems/system-0849/planets/planet-01"
    ],
    traits: ["curious", "peaceful", "long-lived"],
    status: "active"
};

export { Civilization, THE_KETHARI };
```

### registry.sql
```sql
-- Universal Star Registry
-- Auto-generated index of all stellar objects

CREATE TABLE stars (
    id VARCHAR(32) PRIMARY KEY,
    name VARCHAR(128),
    galaxy_id VARCHAR(32) NOT NULL,
    sector_id VARCHAR(32) NOT NULL,
    spectral_class CHAR(1),
    mass_solar DECIMAL(10,4),
    life_stage VARCHAR(32),
    planet_count INT DEFAULT 0,
    has_life BOOLEAN DEFAULT FALSE,
    has_civilization BOOLEAN DEFAULT FALSE,
    formed_at_commit BIGINT,
    FOREIGN KEY (galaxy_id) REFERENCES galaxies(id)
);

-- Current stellar population
INSERT INTO stars VALUES
('sys-0001', NULL, 'gal-0001', 'sec-0001', 'G', 1.04, 'main_sequence', 4, TRUE, FALSE, 12847),
('sys-0002', NULL, 'gal-0001', 'sec-0001', 'M', 0.31, 'main_sequence', 2, FALSE, FALSE, 12901),
('sys-0003', NULL, 'gal-0001', 'sec-0001', 'K', 0.78, 'main_sequence', 6, TRUE, TRUE, 13102),
('sys-0004', 'The Beacon', 'gal-0001', 'sec-0002', 'B', 8.21, 'main_sequence', 0, FALSE, FALSE, 11293);

-- Indexes for common queries
CREATE INDEX idx_stars_habitable ON stars(has_life);
CREATE INDEX idx_stars_civilized ON stars(has_civilization);
CREATE INDEX idx_stars_galaxy ON stars(galaxy_id);
```

### anomaly.bf (Brainfuck - for truly weird cosmic anomalies)
```brainfuck
ANOMALY: Spatial Rift XR-7291
Location: cluster-0001/galaxy-0001/sector-0099
Type: Stable wormhole
Destination: UNKNOWN

+++++++++[>++++++++>+++++++++++>+++>+<<<<-]
>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
Properties encoded in the fabric of spacetime itself
First detected: commit 284729
Status: ACTIVE - DO NOT APPROACH
```

### ruins.cob (COBOL - for ancient artifacts)
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. ANCIENT-RUINS-0047.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 RUINS-RECORD.
          05 RUINS-ID            PIC X(16) VALUE "RUINS-0047".
          05 LOCATION            PIC X(128) VALUE
             "CLUSTER-0001/GALAXY-0001/SECTOR-0012/SYSTEM-0293/PLANET-02".
          05 BUILDER-CIV         PIC X(32) VALUE "THE FIRST ONES".
          05 AGE-COMMITS         PIC 9(12) VALUE 000000892741.
          05 DISCOVERED-COMMIT   PIC 9(12) VALUE 000000994837.
          05 TRANSLATION-STATUS  PIC X(16) VALUE "PARTIAL".
          05 DANGER-LEVEL        PIC 9     VALUE 7.
          05 ARTIFACTS-FOUND     PIC 9(6)  VALUE 000847.
          
       PROCEDURE DIVISION.
           DISPLAY "THE OLD ONES WERE HERE BEFORE TIME HAD MEANING".
           STOP RUN.
```

### chronicle.md (THIS IS WHERE LOC EXPLODES)
```markdown
# Chronicle of The Kethari

## Emergence (Commit #984729)
In the warm tidal pools of their homeworld, the Kethari first developed sapience...

## The Long Peace (Commits #984729 - #985102)
For three thousand years, the Kethari lived in scattered tribes...

## First Cities (Commit #985103)
The river delta settlements merged into the first true city...

## The Burning (Commit #986847)
A supervolcanic eruption nearly ended Kethari civilization...

## Spaceflight (Commit #991293)
The first Kethari vessel breached the atmosphere...

## First Colony (Commit #993847)
The neighboring world, once barren, received its first settlers...
```

Each civilization's chronicle grows indefinitely. Major events get entries. This is where most LOC accumulates.

---

## Event Types

Events are weighted by probability and prerequisites:

### Cosmic Events (always possible)
- Nebula forms
- Nebula collapses into protostar
- Star ignites (main sequence)
- Star ages/evolves
- Supernova
- Black hole forms
- Galaxy collision begins
- New sector mapped

### Planetary Events (requires stars)
- Protoplanetary disk forms
- Planet accretes
- Moon captured
- Atmosphere develops
- Oceans form
- Asteroid impact
- Magnetic field stabilizes

### Life Events (requires suitable planets)
- Abiogenesis (life begins)
- Multicellular life
- Cambrian-style explosion
- Mass extinction
- Intelligence emerges
- Civilization begins

### Civilization Events (requires civilizations)
- Discovery/invention
- War
- Peace treaty
- Cultural renaissance
- Dark age
- Spaceflight achieved
- Colony established
- First contact
- Alliance formed
- Civilization collapses
- Transcendence (leaves physical form)

---

## Commit Message Convention

```
<type>(<scope>): <description>

Types:
  bang     - Universe-level events (rare)
  form     - Something new created
  evolve   - Something changes state
  event    - Something happens
  extinct  - Something ends
  contact  - Civilizations interact
  colony   - Expansion events
  name     - Something gets named (usually via PR)
  lore     - Chronicle/history addition

Examples:
  bang: universe initialized with seed 84729
  form(cluster-0001/galaxy-0012): spiral galaxy coalesces from primordial hydrogen
  evolve(c1/g1/s12/sys-847): star enters red giant phase
  event(c1/g1/s12/sys-302/p3): asteroid impact triggers mass extinction
  form(c1/g1/s12/sys-302/p3): sapient species emerges from surviving mammals
  colony(c1/g1/s12): The Kethari establish outpost in neighboring system
  contact(c1/g1): First contact between The Kethari and The Vorn
  extinct(c1/g1/s08/sys-129/p2): The Silent Ones fade into history
  name(c1/g1/s12/sys-847): Star designated "Kethari Prime" by inhabitants
```

---

## Community Participation (PRs)

### Naming Rights
Anyone can PR to name an unnamed object:
- Stars, planets, moons
- Galaxies and sectors
- Civilizations can be given epithets

Rules:
- Must not be already named
- Must not be offensive
- Must not be real-world trademarked
- Creative/original names encouraged

### Lore Contributions
Add to a civilization's chronicle or a planet's history:
- Must fit established facts
- Must maintain tone
- Reviewed before merge

### Seed Events
Propose specific events:
- "I want a supernova in sector 12"
- "Two civilizations should meet"
- Subject to maintainer discretion

### Discovery
Add detail to existing objects:
- Describe a planet's unique features
- Detail a star system's quirks
- Expand on a civilization's culture

---

## Technical Implementation

### The Simulation Engine (separate repo)
- **Language:** Python
- **Location:** GitHub Actions workflow OR separate `commit-universe-engine` repo
- **Function:** Load state → Roll events → Write files → Commit → Push

### State Management
- Universe state is the repo itself
- Engine reads YAML files to know what exists
- Engine writes new/modified files
- Commit = state transition

### Randomness
- Seeded RNG for reproducibility? Or true random?
- TBD: Could offer "alternate timelines" with different seeds

### Scheduling
```yaml
# GitHub Action runs every 5 minutes
on:
  schedule:
    - cron: '*/5 * * * *'
```

Each run generates 1-3 commits (randomized) for organic feel.

---

## GitHub Actions: Costs & Limits

**Good news: This project is free to run.**

### Pricing

| Repository Type | Minutes | Cost |
|-----------------|---------|------|
| **Public repo** | **Unlimited** | **Free** ✓ |
| Private (Free tier) | 2,000/month | $0.008/min after |
| Private (Pro) | 3,000/month | $0.008/min after |

Since Commit Universe will be a **public repository**, GitHub Actions minutes are completely free with no cap. This is the way.

### Limits to Be Aware Of

| Limit | Value | Impact |
|-------|-------|--------|
| Minimum schedule interval | 5 minutes | Can't run more frequently than `*/5 * * * *` |
| Job execution time | 6 hours max | No issue—our jobs take seconds |
| Concurrent jobs | 20 (free) | No issue—we run 1 at a time |
| API requests | 1,000/hour/repo | Be mindful if scaling up |
| Workflow run time | 35 days max | N/A for scheduled jobs |

### Our Target Setup

```yaml
on:
  schedule:
    - cron: '*/5 * * * *'  # Every 5 minutes
```

**Expected output:**
- ~288 workflow runs per day
- 1-3 commits per run (randomized)
- **~300-800 commits per day**
- **$0 cost** (public repo)

Each job runs for just a few seconds (load state → generate event → commit → push), nowhere near any limits.

### Cost Summary

| Item | Cost |
|------|------|
| GitHub Actions minutes | $0 (public repo) |
| Repository storage | $0 (free tier: 1GB, then ~$0.008/GB/day) |
| Git LFS | Not needed |
| **Total** | **Free** (until repo exceeds ~1GB) |

By the time storage becomes a concern, the project will either be dead or successful enough to justify costs.

---

## Milestones

| Commits | Event |
|---------|-------|
| 1 | Big Bang - universe initialized |
| 100 | First galaxies form |
| 1,000 | First stars ignite |
| 10,000 | First planets form |
| 50,000 | First life emerges |
| 100,000 | First civilization |
| 250,000 | First spacefaring civilization |
| 500,000 | First interstellar contact |
| 1,000,000 | ??? |

---

## The Big Bang (Commit #1)

The initial commit creates:

```
commit-universe/
├── README.md
├── CONSTANTS.yaml
├── epoch.yaml
└── void/
    └── .gitkeep
```

With message:
```
bang: in the beginning, there was nothing. then there was something.
```

The `void/` directory represents pre-galactic space. First structures will emerge from it.

---

## Open Questions

1. **Determinism** — Should the universe be reproducible from a seed, or truly random?
2. **Speed controls** — Should there be a way to "fast forward" or pause?
3. **Alternate timelines** — Fork the repo at any point for parallel universes?
4. **Visualization** — Future web UI to explore the universe graphically?
5. **Interaction depth** — How much can PRs really affect the simulation?

---

## Next Steps

1. [x] Document the concept (this file)
2. [ ] Create the Commit Universe repo with Big Bang commit
3. [ ] Build the simulation engine (Python)
4. [ ] Set up GitHub Actions for automated commits
5. [ ] Write contribution guidelines
6. [ ] Let it run and grow
7. [ ] Build community

---

*The universe doesn't care if anyone is watching. It just keeps going.*
