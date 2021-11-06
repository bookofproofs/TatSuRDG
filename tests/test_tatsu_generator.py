import unittest
from parameterized import parameterized
from tatsurd import TatSuRandomDerivation
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
        cls.path_to_grammar = os.path.join(cls.path, "tatsu.ebnf")
        cls.path_to_usecases = os.path.join(cls.path)
        with io.open(cls.path_to_grammar, 'r', encoding="utf-8") as file:
            grammar = file.read()
            cls.parser = tatsu.compile(grammar)
            cls.rg = TatSuRandomDerivation(cls.parser, max_length_regex=50, max_counter=5, recursion_limit=1500)

    @parameterized.expand([
        "start",
        "grammar",
        "directive",
        "keywords",
        "keyword",
        "paramdef",
        "rule",
        "decorator",
        "params",
        "first_param",
        "kwparams",
        "pair",
        "expre",
        "choice",
        "sequence",
        "element",
        "rule_include",
        "named",
        "named_list",
        "named_single",
        "override",
        "override_list",
        "override_single",
        "override_single_deprecated",
        "term",
        "group",
        "gather",
        "positive_gather",
        "normal_gather",
        "join",
        "positive_join",
        "normal_join",
        "left_join",
        "right_join",
        "separator",
        "positive_closure",
        "closure",
        "empty_closure",
        "optional",
        "special",
        "lookahead",
        "negative_lookahead",
        "skip_to",
        "atom",
        "call",
        "void",
        "cut",
        "cut_deprecated",
        "known_name",
        "name",
        "constant",
        "token",
        "literal",
        "string",
        "raw_string",
        "STRING",
        "hex",
        "float",
        "int",
        "path",
        "word",
        "any",
        "pattern",
        "regexes",
        "regex",
        "boolean",
        "eof",

    ])
    def test_derivation_generator(self, use_case):
        for trial in range(1, 3):
            self.rg.init_rules()
            self.rg.random_derivation(use_case)
