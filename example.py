import io
import tatsu
from tatsurd import TatSuRandomDerivation

path_to_grammar = "../TatSuRDG/tests/tatsu.ebnf"  # path to your tatsu ebnf grammar


class ExampleRandomDerivation:

    def __init__(self, grammar_name, override_placeholders: dict):
        path_to_grammar = "tests/" + grammar_name
        with io.open(path_to_grammar, 'r', encoding="utf-8") as file:
            grammar = file.read()
            self.parser = tatsu.compile(grammar)

        self.rg = TatSuRandomDerivation(self.parser, max_length_regex=5, max_counter=5, recursion_limit=1500,
                                        override_placeholders=override_placeholders)

    def derive(self, rule_name):
        return self.rg.random_derivation(rule_name)


ex = ExampleRandomDerivation("calc.ebnf", {"number": "1"})
for i in range(1, 50):
    ex.rg.init_rules()
    print(ex.derive("expression"))
