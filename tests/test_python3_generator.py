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
        cls.path_to_grammar = os.path.join(cls.path, "python3.ebnf")
        cls.path_to_usecases = os.path.join(cls.path)
        with io.open(cls.path_to_grammar, 'r', encoding="utf-8") as file:
            grammar = file.read()
            cls.parser = tatsu.compile(grammar)
            cls.rg = TatSuRandomDerivation(cls.parser, max_length_regex=5, max_counter=5, recursion_limit=1500)

    @parameterized.expand([
        "single_input",
        "file_input",
        "eval_input",
        "decorator",
        "decorators",
        "decorated",
        "funcdef",
        "parameters",
        "typedargslist",
        "tfpdef",
        "varargslist",
        "vfpdef",
        "stmt",
        "simple_stmt",
        "small_stmt",
        "expr_stmt",
        "testlist_star_expr",
        "augassign",
        "del_stmt",
        "pass_stmt",
        "flow_stmt",
        "break_stmt",
        "continue_stmt",
        "return_stmt",
        "yield_stmt",
        "raise_stmt",
        "import_stmt",
        "import_name",
        "import_from",
        "import_as_name",
        "dotted_as_name",
        "import_as_names",
        "dotted_as_names",
        "dotted_name",
        "global_stmt",
        "nonlocal_stmt",
        "assert_stmt",
        "compound_stmt",
        "if_stmt",
        "while_stmt",
        "for_stmt",
        "try_stmt",
        "with_stmt",
        "with_item",
        "except_clause",
        "suite",
        "test",
        "test_nocond",
        "lambdef",
        "lambdef_nocond",
        "or_test",
        "and_test",
        "not_test",
        "comparison",
        "comp_op",
        "star_expr",
        "expr",
        "xor_expr",
        "and_expr",
        "shift_expr",
        "arith_expr",
        "term",
        "factor",
        "power",
        "atom",
        "testlist_comp",
        "trailer",
        "subscriptlist",
        "subscript",
        "sliceop",
        "exprlist",
        "testlist",
        "dictorsetmaker",
        "classdef",
        "arglist",
        "argument",
        "comp_iter",
        "comp_for",
        "comp_if",
        "yield_expr",
        "yield_arg",
        "str",
        "number",
        "integer",
        "newline",
        "NAME",
        "STRING_LITERAL",
        "BYTES_LITERAL",
        "decimal_integer",
        "OCT_INTEGER",
        "HEX_INTEGER",
        "BIN_INTEGER",
        "float_number",
        "IMAG_NUMBER",
        "skip_",
        "unknown_char",
        "SHORT_STRING",
        "LONG_STRING",
        "LONG_STRING_ITEM",
        "LONG_STRING_CHAR",
        "STRING_ESCAPE_SEQ",
        "NON_ZERO_DIGIT",
        "DIGIT",
        "OCT_DIGIT",
        "HEX_DIGIT",
        "BIN_DIGIT",
        "POINT_FLOAT",
        "EXPONENT_FLOAT",
        "INT_PART",
        "FRACTION",
        "EXPONENT",
        "SHORT_BYTES",
        "LONG_BYTES",
        "LONG_BYTES_ITEM",
        "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE",
        "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE",
        "LONG_BYTES_CHAR",
        "BYTES_ESCAPE_SEQ",
        "SPACES",
        "COMMENT",
        "LINE_JOINING",
        "ID_START",
        "ID_CONTINUE",
        "INDENT",
        "DEDENT",
    ])
    def test_derivation_generator(self, use_case):
        for trial in range(1, 3):
            self.rg.init_rules()
            self.rg.random_derivation(use_case)
