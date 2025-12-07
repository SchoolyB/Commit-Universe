"""
Markdown generator - Chronicles and historical records
"""

from typing import List, Optional
import random


def generate_chronicle_md(
    subject_name: str,
    subject_type: str = "civilization",
    emerged_at_commit: int = 0,
    initial_entry: Optional[str] = None
) -> str:
    """Generate a new chronicle.md file"""
    
    if subject_type == "civilization":
        return _generate_civilization_chronicle(subject_name, emerged_at_commit, initial_entry)
    elif subject_type == "planet":
        return _generate_planet_chronicle(subject_name, emerged_at_commit, initial_entry)
    elif subject_type == "star":
        return _generate_star_chronicle(subject_name, emerged_at_commit, initial_entry)
    else:
        return _generate_generic_chronicle(subject_name, subject_type, emerged_at_commit, initial_entry)


def _generate_civilization_chronicle(name: str, emerged_at_commit: int, initial_entry: Optional[str]) -> str:
    entry = initial_entry or _generate_emergence_text(name)
    
    return f'''# Chronicle of {name}

> *History is not the past. It is the present. We carry our history with us. We are our history.* — Ancient proverb

---

## The Beginning

### Emergence (Commit #{emerged_at_commit})

{entry}

---

## Timeline

| Commit | Event | Era |
|--------|-------|-----|
| {emerged_at_commit} | First signs of sapience | Emergence |

---

## Cultural Notes

*To be discovered...*

---

## Relations

*None yet established.*

---

*Chronicle maintained by the Universal Archives. Last updated: Commit #{emerged_at_commit}*
'''


def _generate_planet_chronicle(name: str, formed_at_commit: int, initial_entry: Optional[str]) -> str:
    entry = initial_entry or f"A new world takes shape in the cosmic dance of gravity and matter."
    
    return f'''# Geological Chronicle: {name}

---

## Formation (Commit #{formed_at_commit})

{entry}

---

## Geological Eras

| Commit | Era | Duration (My) | Notes |
|--------|-----|---------------|-------|
| {formed_at_commit} | Hadean | - | Initial formation |

---

## Notable Events

*Awaiting geological activity...*

---

*Chronicle maintained by the Universal Archives.*
'''


def _generate_star_chronicle(name: str, formed_at_commit: int, initial_entry: Optional[str]) -> str:
    entry = initial_entry or f"From the collapse of a molecular cloud, a new light ignites in the darkness."
    
    return f'''# Stellar Chronicle: {name}

---

## Ignition (Commit #{formed_at_commit})

{entry}

---

## Stellar Evolution

| Commit | Stage | Notes |
|--------|-------|-------|
| {formed_at_commit} | Protostar → Main Sequence | Nuclear fusion begins |

---

## System Events

*Awaiting stellar activity...*

---

*Chronicle maintained by the Universal Archives.*
'''


def _generate_generic_chronicle(name: str, subject_type: str, created_at_commit: int, initial_entry: Optional[str]) -> str:
    entry = initial_entry or f"A new {subject_type} emerges into existence."
    
    return f'''# Chronicle: {name}

Type: {subject_type.title()}

---

## Origin (Commit #{created_at_commit})

{entry}

---

## Events

| Commit | Event |
|--------|-------|
| {created_at_commit} | Creation |

---

*Chronicle maintained by the Universal Archives.*
'''


def append_chronicle_md(
    existing_content: str,
    event_title: str,
    event_text: str,
    commit_number: int,
    era: Optional[str] = None
) -> str:
    """Append a new entry to an existing chronicle"""
    
    new_entry = f'''

### {event_title} (Commit #{commit_number})

{event_text}
'''
    
    # Find the Timeline table and add a row
    timeline_row = f"\n| {commit_number} | {event_title} | {era or 'Unknown'} |"
    
    # Insert the new entry before the Timeline section if it exists
    if "## Timeline" in existing_content:
        parts = existing_content.split("## Timeline")
        # Add entry before Timeline
        before_timeline = parts[0].rstrip() + new_entry + "\n\n---\n\n## Timeline"
        # Add row to timeline table
        timeline_and_after = parts[1]
        
        # Find the table and append row
        lines = timeline_and_after.split('\n')
        new_lines = []
        table_found = False
        for line in lines:
            new_lines.append(line)
            if line.startswith('|') and '|' in line[1:] and not table_found:
                if 'Commit' not in line and '---' not in line:
                    table_found = True
                    new_lines.append(timeline_row.strip())
        
        return before_timeline + '\n'.join(new_lines)
    
    # If no Timeline section, just append
    return existing_content.rstrip() + new_entry


def _generate_emergence_text(name: str) -> str:
    """Generate flavor text for civilization emergence"""
    templates = [
        f"In the twilight of prehistory, the first {name} looked up at the stars and wondered.",
        f"From the crucible of survival, the {name} emerged—tool-makers, dreamers, seekers of meaning.",
        f"When the {name} first spoke to one another of things beyond survival, civilization was born.",
        f"The {name} arose slowly, each generation building upon the last, until they could name themselves.",
        f"In sheltered valleys and by ancient waters, the {name} took their first steps toward the stars.",
    ]
    return random.choice(templates)


# Event text generators for various milestone events
def generate_event_text(event_type: str, **kwargs) -> str:
    """Generate flavor text for various event types"""
    
    generators = {
        "first_city": _gen_first_city_text,
        "writing": _gen_writing_text,
        "spaceflight": _gen_spaceflight_text,
        "first_contact": _gen_first_contact_text,
        "colony": _gen_colony_text,
        "war": _gen_war_text,
        "peace": _gen_peace_text,
        "extinction": _gen_extinction_text,
        "discovery": _gen_discovery_text,
    }
    
    generator = generators.get(event_type, lambda **kw: f"An event of type '{event_type}' occurred.")
    return generator(**kwargs)


def _gen_first_city_text(**kwargs) -> str:
    name = kwargs.get("civ_name", "The people")
    return f"{name} gathered in unprecedented numbers, and from their collective effort rose the first true city—a beacon of cooperation in a wilderness world."


def _gen_writing_text(**kwargs) -> str:
    name = kwargs.get("civ_name", "The people")
    return f"For the first time, {name} found a way to make their thoughts immortal. Writing emerged, and with it, true history began."


def _gen_spaceflight_text(**kwargs) -> str:
    name = kwargs.get("civ_name", "The people")
    return f"Breaking free of their world's gravity well, {name} achieved what their ancestors could only dream of. The cosmos awaited."


def _gen_first_contact_text(**kwargs) -> str:
    civ_a = kwargs.get("civ_a", "One civilization")
    civ_b = kwargs.get("civ_b", "another")
    return f"Across the void, two species met for the first time. {civ_a} and {civ_b} would never be the same."


def _gen_colony_text(**kwargs) -> str:
    name = kwargs.get("civ_name", "The people")
    location = kwargs.get("location", "a distant world")
    return f"{name} planted their flag on {location}. What was once alien soil would become a new home."


def _gen_war_text(**kwargs) -> str:
    return "The drums of war echoed across the stars. Civilizations that had reached for the infinite now reached for weapons."


def _gen_peace_text(**kwargs) -> str:
    return "After the long darkness, peace returned. The survivors vowed to remember, and to do better."


def _gen_extinction_text(**kwargs) -> str:
    name = kwargs.get("civ_name", "They")
    return f"{name} are gone now. Their cities crumble, their songs forgotten. Only these records remain to mark their passing."


def _gen_discovery_text(**kwargs) -> str:
    discovery = kwargs.get("discovery", "something remarkable")
    return f"A breakthrough that would reshape everything: the discovery of {discovery}."
