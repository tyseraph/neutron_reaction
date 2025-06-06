import sys
from pathlib import Path

# Ensure src directory is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from neutron_reaction import interactive_message
import pytest

from neutron_reaction.app import create_dash_app


def test_interactive_message():
    assert "Welcome" in interactive_message()


def test_create_dash_app():
    pytest.importorskip("dash")
    app = create_dash_app()
    assert hasattr(app, "layout")
