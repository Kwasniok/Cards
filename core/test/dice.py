import unittest
from collections import defaultdict
from ..dice import Dice


class Test(unittest.TestCase):
    def test_general(self):
        F = 6
        outcomes = range(1, F + 1)
        d = Dice(name="d6", outcomes=outcomes)
        # roll / last outcome
        self.assertEqual(d.number_of_faces(), F)
        with self.assertRaises(RuntimeError):
            d.last_outcome()
        histogram = defaultdict(lambda: 0, {})
        for i in range(1000):
            last = d.roll()
            self.assertTrue(last in outcomes)
            self.assertEqual(d.last_outcome(), last)
            histogram[last] += 1
        # all outcomes used
        for outcome in outcomes:
            self.assertTrue(outcome in histogram.keys())
