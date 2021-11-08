import unittest
from parameterized import parameterized
from tatsurd import TatSuRDG
import os
import io
import tatsu


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
        cls.path_to_grammar = os.path.join(cls.path, "calc_cut.ebnf")
        cls.path_to_usecases = os.path.join(cls.path)
        with io.open(cls.path_to_grammar, 'r', encoding="utf-8") as file:
            grammar = file.read()
            cls.parser = tatsu.compile(grammar)
            cls.rg = TatSuRDG(cls.parser, max_length_regex=5, max_counter=5, recursion_limit=1500)

    @parameterized.expand([
        "expression",
        "term",
        "+",
        "-",
        "*",
        "/",
        "factor",
        "(",
        ")",
        "number",
    ])
    def test_derivation_generator(self, use_case):
        for trial in range(1, 50):
            self.rg.init_rules()
            self.rg.random_derivation(use_case)
