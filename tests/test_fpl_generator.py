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
        cls.path_to_grammar = os.path.join(cls.path, "fpl.ebnf")
        cls.path_to_usecases = os.path.join(cls.path)
        with io.open(cls.path_to_grammar, 'r', encoding="utf-8") as file:
            grammar = file.read()
            cls.parser = tatsu.compile(grammar)
            cls.rg = TatSuRandomDerivation(cls.parser, max_length_regex=5, max_counter=5, recursion_limit=1500)

    @parameterized.expand([
        "Namespace",
        "NamespaceBlock",
        "WildcardTheoryNamespaceList",
        "ExtensionBlock",
        "ExtensionHeader",
        "ExtensionContent",
        "ExtensionTail",
        "ext",
        "end",
        "UsesClause",
        "TheoryBlock",
        "RulesOfInferenceBlock",
        "InferenceHeader",
        "inference",
        "inf",
        "PremiseHeader",
        "premise",
        "pre",
        "ConclusionHeader",
        "conclusion",
        "con",
        "RuleOfInferenceList",
        "RuleOfInference",
        "PremiseConclusionBlock",
        "PremiseBlock",
        "ConclusionBlock",
        "TheoryHeader",
        "theory",
        "th",
        "BuildingBlockList",
        "BuildingBlock",
        "uses",
        "Definition",
        "DefinitionClass",
        "ObjectDefinitionBlock",
        "FunctionalTermDefinitionBlock",
        "DefinitionContentList",
        "DefinitionContent",
        "DefinitionFunctionalTerm",
        "FunctionalTermSignature",
        "Mapping",
        "VariableSpecificationList",
        "VariableSpecification",
        "AssertionStatement",
        "assert",
        "NamedVariableDeclaration",
        "VariableType",
        "GeneralType",
        "IndexHeader",
        "index",
        "ind",
        "Type",
        "VariableList",
        "DefinitionPredicate",
        "PredicateHeader",
        "FunctionalTermHeader",
        "PredicateDefinitionBlock",
        "PredicateIdentifier",
        "AliasedId",
        "ClassHeader",
        "class",
        "cl",
        "predicate",
        "pred",
        "function",
        "func",
        "To",
        "ObjectHeader",
        "LongTemplateHeader",
        "TemplateHeader",
        "object",
        "obj",
        "template",
        "tpl",
        "Axiom",
        "AxiomHeader",
        "AxiomBlock",
        "axiom",
        "ax",
        "postulate",
        "post",
        "PropertyList",
        "Property",
        "DefinitionProperty",
        "ClassInstance",
        "FunctionalTermInstance",
        "PropertyHeader",
        "mandatory",
        "mand",
        "optional",
        "opt",
        "Constructor",
        "InstanceBlock",
        "Signature",
        "ParenthesisedGeneralType",
        "ParamTuple",
        "ArgumentParam",
        "NamedVariableDeclarationList",
        "TypeWithCoord",
        "EntityWithCoord",
        "CoordList",
        "CoordInSignature",
        "Entity",
        "AtList",
        "Coord",
        "RangeInSignature",
        "Range",
        "CallModifier",
        "Plus",
        "ConditionFollowedByResultList",
        "ConditionFollowedByResult",
        "At",
        "TheoremLikeStatementOrConjecture",
        "TheoremLikeStatementOrConjectureHeader",
        "theorem",
        "thm",
        "proposition",
        "prop",
        "lemma",
        "lem",
        "corollary",
        "cor",
        "conjecture",
        "conj",
        "Proof",
        "ProofIdentifier",
        "ProofHeadHeader",
        "ProofBlock",
        "ProofArgumentList",
        "ProofArgument",
        "VDash",
        "AssumeHeader",
        "AssumedPredicate",
        "DerivedPredicate",
        "qed",
        "trivial",
        "PremiseOrOtherPredicate",
        "ArgumentInference",
        "Revoke",
        "RevokeHeader",
        "Justification",
        "Slash",
        "proof",
        "prf",
        "assume",
        "ass",
        "revoke",
        "rev",
        "true",
        "false",
        "not",
        "and",
        "or",
        "impl",
        "iif",
        "xor",
        "is",
        "Predicate",
        "PrimePredicate",
        "QualifiedIdentifier",
        "PredicateWithArguments",
        "Identifier",
        "AmpersandVariable",
        "IndexValue",
        "Ampersand",
        "self",
        "PredicateList",
        "CompoundPredicate",
        "IsOperator",
        "Negation",
        "Conjunction",
        "Disjunction",
        "Implication",
        "Equivalence",
        "ExclusiveOr",
        "ParenthesisedPredicate",
        "All",
        "all",
        "Exists",
        "ex",
        "ExistsHeader",
        "ExistsTimesN",
        "Dollar",
        "PythonDelegate",
        "PythonIdentifier",
        "py",
        "LeftBracket",
        "RightBracket",
        "StatementList",
        "Statement",
        "ReturnStatement",
        "CaseStatement",
        "LoopStatement",
        "RangeStatement",
        "RangeOrLoopBody",
        "KeysOfVariadicVariable",
        "ClosedOrOpenRange",
        "LeftBound",
        "RightBound",
        "ExclamationMark",
        "range",
        "loop",
        "DefaultResult",
        "AssignmentStatement",
        "Assignee",
        "ReturnHeader",
        "UndefinedHeader",
        "return",
        "ret",
        "undefined",
        "undef",
        "ColonEqual",
        "else",
        "case",
        "Dot",
        "LeftBrace",
        "RightBrace",
        "LeftParen",
        "RightParen",
        "Comma",
        "Star",
        "Colon",
        "NamespaceIdentifier",
        "ArgumentIdentifier",
        "WildcardTheoryNamespace",
        "NamespaceModifier",
        "Alias",
        "alias",
        "IdStartsWithCap",
        "IdStartsWithSmallCase",
        "SW",
        "CW",
        "Comment",
        "LongComment",
        "IW",
        "XId",
        "Variable",
        "Digit",
        "LocalizationBlock",
        "LocalizationList",
        "Localization",
        "SemiColon",
        "Tilde",
        "TranslationList",
        "Translation",
        "LanguageCode",
        "EBNFTransl",
        "EBNFTerm",
        "EBNFFactor",
        "EBNFString",
        "EBNFBar",
        "LocalizationHeader",
        "localization",
        "loc",
        "extDigit"
    ])
    def test_derivation_generator(self, use_case):
        for trial in range(1, 3):
            self.rg.init_rules()
            self.rg.random_derivation(use_case)
