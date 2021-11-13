import io
import tatsu
from tatsurd import TatSuRDG


class ExampleRandomDerivation:

    def __init__(self, grammar_name, override_placeholders: dict):
        path_to_grammar = "tests/" + grammar_name
        with io.open(path_to_grammar, 'r', encoding="utf-8") as file:
            grammar = file.read()
        self.parser = tatsu.compile(grammar)
        self.rg = TatSuRDG(self.parser, max_length_regex=5, max_counter=5, recursion_limit=1500,
                           override_placeholders=override_placeholders)

    def derive(self, rule_name, trace):
        return self.rg.random_derivation(rule_name, trace)


ex = ExampleRandomDerivation("fpl.ebnf", {"IW": "", "LongComment": "", "Comment": ""})
for i in range(1, 50):
    ex.rg.init_rules()
    trace = []
    print(ex.derive("PredicateWithArguments", trace))
    print(str(trace))
