import json
from pathlib import Path


def load_isotopes(json_path: str = 'web/isotopes.json') -> list[str]:
    """Load the isotope list from an external JSON file."""
    path = Path(json_path)
    with path.open() as f:
        return json.load(f)


def main():
    """Simple CLI that prints available isotopes."""
    for isotope in load_isotopes():
        print(isotope)


if __name__ == '__main__':
    main()
