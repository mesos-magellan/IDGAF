import unittest

import pytest

from idgaf import State
from idgaf.examples.tsp.cities import cities_7
from idgaf.examples.tsp.bruteforce import bruteforce_tsp
from idgaf.examples.tsp import tsp_auto_example


class TestTSPExample(unittest.TestCase):
    def test_correctness(self):
        ga_fittest = tsp_auto_example(cities_7, minutes=0.02)
        bf_fittest = bruteforce_tsp(cities_7, announce_every=50)
        assert ga_fittest == bf_fittest


def test_state_abc():
    with pytest.raises(TypeError):
        class IncompleteState(State):
            pass
        b = IncompleteState()
