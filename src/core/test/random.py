import unittest
from collections import defaultdict
from ..random import random_pick, random_pop
from ..random import Randomized_List_View


class Test(unittest.TestCase):
    def test_random_pick(self):
        list = range(5)
        # track the frequncy of n random picks
        histogram = defaultdict(lambda: 0)
        n = 10000
        for i in range(n):
            histogram[random_pick(list)] += 1
        # check frequency of each element picked
        for element, frequency in histogram.items():
            if frequency < 0.8 * float(n) / float(len(list)):
                self.fail("Frequency distribution not even enough.")

        def test_random_pop(self):
            list = range(5)
            # track the frequncy of n random pops (on a copy of list)
            histogram = defaultdict(lambda: 0)
            n = 10000
            for i in range(n):
                list_copy = list[:]
                histogram[random_pop(list_copy)] += 1
                self.assertTrue(len(list_copy) == len(list) - 1)
            # check frequency of each element popped
            for element, frequency in histogram.items():
                if frequency < 0.8 * float(n) / float(len(list)):
                    self.fail("Frequency distribution not even enough.")

        def test_randomized(self):
            list = range(5)
            # track frequency of each element at each index
            histograms = [defaultdict(lambda: 0) for element in list]
            n = 10000
            for i in range(n):
                rand_list = Randomized_List_View(list)
                # same content
                self.assertTrue(len(list) == len(rand_list))
                for element in list:
                    self.assertTrue(element in rand_list)
                for j in range(len(rand_list)):
                    histograms[j][rand_list[j]] += 1
            # check frequency of each element for each index
            for j in range(len(list)):
                for element, frequency in histograms[j].items():
                    if frequency < 0.8 * float(n) / float(len(list)):
                        self.fail("Frequency distribution not even enough.")
