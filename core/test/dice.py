import unittest
from collections import defaultdict
from ..dice import Dice


class Test(unittest.TestCase):
    def test_general(self):
        F = 6
        outcomes = range(1, F + 1)
        d = Dice(outcomes=outcomes)
        self.assertEqual(d.get_number_of_faces(), F)
        # roll / last outcome
        histogram = defaultdict(lambda: 0, {})
        for i in range(1000):
            last = d.roll()
            self.assertTrue(last in outcomes)
            self.assertEqual(d.get_last_outcome(), last)
            histogram[last] += 1
        # all outcomes used
        for outcome in outcomes:
            self.assertTrue(outcome in histogram.keys())
