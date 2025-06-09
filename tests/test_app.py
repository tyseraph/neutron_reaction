import sys
from pathlib import Path

# Ensure src directory is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from neutron_reaction import interactive_message


def test_interactive_message():
    assert "Welcome" in interactive_message()
