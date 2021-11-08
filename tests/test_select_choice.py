from tatsurd import TatSuRDG
import os
import io
import tatsu
import unittest
import scipy.stats as stats


class TatSuRDTests(unittest.TestCase):
    path = ""
    path_to_grammar = ""
    path_to_usecases = ""
    parser = None
    rd = None

    @classmethod
    def setUpClass(cls):
        cls.path = os.path.normpath(os.path.abspath(__file__))
        if os.path.isfile(cls.path):
            cls.path = os.path.dirname(cls.path)
        cls.path_to_grammar = os.path.join(cls.path, "calc.ebnf")
        cls.path_to_usecases = os.path.join(cls.path)
        with io.open(cls.path_to_grammar, 'r', encoding="utf-8") as file:
            grammar = file.read()
            cls.parser = tatsu.compile(grammar)
            cls.rg = TatSuRDG(cls.parser, max_length_regex=10, max_counter=5, recursion_limit=1500)

    def test_select_choice_n(self):
        counters = dict()
        numb = 10
        for j in range(0, numb):
            counters[j] = 0
        total = 1000000
        for i in range(1, total):
            res = self.rg.select_index_randomly(numb)
            if res is not None:
                counters[res] += 1
        expected = []
        observed = []
        for j in range(0, numb):
            expected.append(total * (j + 1) / (numb * (numb + 1) / 2))
            observed.append(counters[j])

        # normalize the data such that the observed and expected frequencies have the same sum
        again = True
        while again:
            try:
                for j in range(0, numb):
                    observed[j] = observed[j] * sum(expected) / sum(observed)
                result = stats.chisquare(f_obs=observed, f_exp=expected)
                again = False
            except ValueError:
                pass

        print("expected: " + str(expected) + ", sum = " + str(sum(expected)))
        print("observed: " + str(observed) + ", sum = " + str(sum(observed)))
        result = stats.chisquare(f_obs=observed, f_exp=expected)
        print(result)
        # fail if chi square pvalue is smaller than 5%
        self.assertGreater(result[1], 0.05)
