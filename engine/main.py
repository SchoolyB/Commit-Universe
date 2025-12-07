#!/usr/bin/env python3
"""
Commit Universe Engine - Main Entry Point

This is the simulation engine that generates cosmic events and commits them
to the Commit Universe repository.

Usage:
    python -m engine.main [--events N] [--dry-run] [--seed SEED]
"""

import argparse
import json
import os
import random
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from .config import UNIVERSE_ROOT, TIME_SCALES
from .universe import UniverseReader, UniverseState, Epoch
from .events import EventGenerator, Event


class CommitUniverse:
    """Main engine class"""
    
    def __init__(self, universe_path: Path, dry_run: bool = False, seed: Optional[int] = None):
        self.universe_path = Path(universe_path)
        self.dry_run = dry_run
        self.seed = seed or int(datetime.now().timestamp())
        
        random.seed(self.seed)
        
    def run(self, num_events: int = 1) -> List[str]:
        """Run the simulation for N events"""
        
        print(f"🌌 Commit Universe Engine")
        print(f"   Universe: {self.universe_path}")
        print(f"   Events to generate: {num_events}")
        print(f"   Seed: {self.seed}")
        print(f"   Dry run: {self.dry_run}")
        print()
        
        # Load current state
        state = self._load_state()
        print(f"📊 Current Universe State:")
        print(f"   Commit: {state.epoch.commit_count}")
        print(f"   Cosmic Age: {state.epoch.cosmic_age_million_years:.2f} Myr")
        print(f"   Galaxies: {state.total_galaxies}")
        print(f"   Stars: {state.total_stars}")
        print(f"   Planets: {state.total_planets}")
        print(f"   Life-bearing worlds: {state.total_life}")
        print(f"   Civilizations: {state.total_civilizations}")
        print()
        
        # Generate events
        generator = EventGenerator(state, self.seed)
        events = generator.generate_events(num_events)
        
        if not events:
            print("⚠️  No events generated (universe may need more initial structure)")
            return []
        
        commit_messages = []
        
        for event in events:
            print(f"✨ Event: {event.event_type.value}")
            print(f"   Location: {event.location}")
            print(f"   Description: {event.description}")
            print(f"   Magnitude: {event.magnitude}")
            print()
            
            if not self.dry_run:
                self._apply_event(event, state)
                # Commit immediately after each event
                self._git_commit(event.commit_message)
                print(f"📝 Committed: {event.commit_message}")
                commit_messages.append(event.commit_message)
        
        # Update epoch once at the end
        if not self.dry_run and events:
            self._update_epoch(state, len(events))
            self._git_commit(f"tick: universe advances to commit {state.epoch.commit_count + len(events)}")

        return commit_messages
    
    def _load_state(self) -> UniverseState:
        """Load current universe state"""
        reader = UniverseReader(self.universe_path)
        state = reader.read_state()

        # Sync epoch commit_count with actual git commit count
        actual_commit_count = self._get_git_commit_count()
        if actual_commit_count != state.epoch.commit_count:
            print(f"⚠️  Syncing epoch: {state.epoch.commit_count} → {actual_commit_count}")
            state.epoch.commit_count = actual_commit_count

        return state

    def _get_git_commit_count(self) -> int:
        """Get the actual git commit count"""
        try:
            result = subprocess.run(
                ["git", "rev-list", "--count", "HEAD"],
                cwd=self.universe_path,
                check=True,
                capture_output=True,
                text=True
            )
            return int(result.stdout.strip())
        except (subprocess.CalledProcessError, ValueError):
            return 0
    
    def _apply_event(self, event: Event, state: UniverseState):
        """Apply an event's changes to the filesystem"""
        
        # Create new files
        for file_path, content in event.files_to_create:
            full_path = self.universe_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(full_path, 'w') as f:
                f.write(content)
            
            print(f"   📄 Created: {file_path}")
        
        # Modify existing files (simplified - would need more sophisticated handling)
        for file_path, field, new_value in event.files_to_modify:
            full_path = self.universe_path / file_path
            if full_path.exists():
                # This is simplified - real implementation would parse and modify properly
                print(f"   ✏️  Modified: {file_path} ({field}={new_value})")
    
    def _update_epoch(self, state: UniverseState, events_processed: int):
        """Update the epoch file"""
        epoch_path = self.universe_path / "epoch.json"
        
        # Calculate time passage based on current era
        time_scale = self._get_current_time_scale(state)
        time_passed = time_scale * events_processed
        
        new_epoch = {
            "commit_count": state.epoch.commit_count + events_processed,
            "cosmic_age_million_years": state.epoch.cosmic_age_million_years + time_passed,
            "current_era": self._determine_era(state),
            "last_updated": datetime.now().isoformat(),
            "seed": self.seed
        }
        
        with open(epoch_path, 'w') as f:
            json.dump(new_epoch, f, indent=2)
    
    def _get_current_time_scale(self, state: UniverseState) -> float:
        """Determine current time scale based on universe state"""
        commit = state.epoch.commit_count
        
        if commit < 1000:
            return TIME_SCALES["early_universe"] / 1_000_000  # Convert to Myr
        elif state.total_civilizations > 0:
            # Check if any spacefaring
            spacefaring = any(c.tech_level >= 4 for c in state.civilizations)
            if spacefaring:
                return TIME_SCALES["space_age"] / 1_000_000
            return TIME_SCALES["civilization_emergence"] / 1_000_000
        elif state.total_life > 0:
            return TIME_SCALES["planetary_development"] / 1_000_000
        elif state.total_planets > 0:
            return TIME_SCALES["stellar_evolution"] / 1_000_000
        elif state.total_stars > 0:
            return TIME_SCALES["galaxy_formation"] / 1_000_000
        else:
            return TIME_SCALES["early_universe"] / 1_000_000
    
    def _determine_era(self, state: UniverseState) -> str:
        """Determine the current cosmic era"""
        if state.total_civilizations > 0:
            if any(c.tech_level >= 5 for c in state.civilizations):
                return "interstellar_age"
            elif any(c.tech_level >= 4 for c in state.civilizations):
                return "space_age"
            return "civilization_age"
        elif state.total_life > 0:
            return "life_age"
        elif state.total_planets > 0:
            return "planetary_age"
        elif state.total_stars > 0:
            return "stellar_age"
        elif state.total_galaxies > 0:
            return "galactic_age"
        else:
            return "void"
    
    def _git_commit(self, message: str):
        """Create a git commit"""
        try:
            # Stage all changes
            subprocess.run(
                ["git", "add", "-A"],
                cwd=self.universe_path,
                check=True,
                capture_output=True
            )
            
            # Commit
            subprocess.run(
                ["git", "commit", "-m", message],
                cwd=self.universe_path,
                check=True,
                capture_output=True
            )
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Git error: {e.stderr.decode() if e.stderr else str(e)}")


def create_big_bang(universe_path: Path) -> str:
    """Create the initial Big Bang commit"""
    from .generators import generate_constants_go
    
    universe_path.mkdir(parents=True, exist_ok=True)
    
    seed = int(datetime.now().timestamp())
    
    # Create initial files
    readme = f'''# 🌌 Commit Universe

> A procedurally generated universe, evolving through git commits.

## The Beginning

This universe was born at commit #1, the Big Bang.

**Seed:** {seed}
**Created:** {datetime.now().isoformat()}

## How It Works

This repository IS the universe. Every commit represents cosmic time passing.
Stars form, planets coalesce, life emerges, civilizations rise and fall.

**The code doesn't run. It just exists.**

Browse the directories to explore galaxies, star systems, and worlds.
Each file type tells a different part of the story.

## Stats

- **Commit:** 1
- **Cosmic Age:** 0 Myr
- **Galaxies:** 0
- **Stars:** 0
- **Planets:** 0
- **Life-bearing worlds:** 0
- **Civilizations:** 0

*Stats updated each commit by the simulation engine.*

---

*The universe doesn't care if anyone is watching. It just keeps going.*
'''
    
    epoch = {
        "commit_count": 1,
        "cosmic_age_million_years": 0,
        "current_era": "void",
        "created_at": datetime.now().isoformat(),
        "seed": seed
    }
    
    constants = generate_constants_go(seed, 0)
    
    # Write files
    (universe_path / "README.md").write_text(readme)
    (universe_path / "epoch.json").write_text(json.dumps(epoch, indent=2))
    (universe_path / "constants.go").write_text(constants)
    
    # Create void directory
    (universe_path / "void").mkdir(exist_ok=True)
    (universe_path / "void" / ".gitkeep").write_text("# The void - before structure\n")
    
    # Initialize git
    subprocess.run(["git", "init"], cwd=universe_path, check=True, capture_output=True)
    subprocess.run(["git", "add", "-A"], cwd=universe_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "bang: in the beginning, there was nothing. then there was something."],
        cwd=universe_path,
        check=True,
        capture_output=True
    )
    
    return f"🌌 Big Bang complete! Universe created at {universe_path}"


def main():
    parser = argparse.ArgumentParser(
        description="Commit Universe Engine - Simulate cosmic evolution through git commits"
    )
    
    parser.add_argument(
        "--universe", "-u",
        type=Path,
        default=UNIVERSE_ROOT,
        help="Path to the universe repository"
    )
    
    parser.add_argument(
        "--events", "-e",
        type=int,
        default=1,
        help="Number of events to generate (default: 1)"
    )
    
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Generate events without committing"
    )
    
    parser.add_argument(
        "--seed", "-s",
        type=int,
        default=None,
        help="Random seed for reproducibility"
    )
    
    parser.add_argument(
        "--big-bang",
        action="store_true",
        help="Create a new universe with the Big Bang"
    )
    
    args = parser.parse_args()
    
    if args.big_bang:
        result = create_big_bang(args.universe)
        print(result)
        return 0
    
    if not args.universe.exists():
        print(f"❌ Universe not found at {args.universe}")
        print("   Use --big-bang to create a new universe")
        return 1
    
    engine = CommitUniverse(
        universe_path=args.universe,
        dry_run=args.dry_run,
        seed=args.seed
    )
    
    commits = engine.run(num_events=args.events)
    
    print()
    print(f"✅ Generated {len(commits)} cosmic events")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
