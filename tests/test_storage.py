import pytest_
from models.electrolyzer import Elektrolyzer

def elektrolyzer():
    """Fixture für Test-Elektrolyzer"""
    return Elektrolyzer("Test", id=1, efficiency=0.75, cost_per_kw=100)
