# coding: utf-8
import pytest
if __name__ == "__main__":
    import sys
    import os
    # sys.path.append(os.path.realpath('..'))
    pytest.main([__file__])

import parser.type_mod as tm


def test_rule_primative():
    tester = tm.TypeRules()
    type_map = {
        "any": "object",
        "short": "int",
        "long": "int",
        "float": "float",
        "double": "float",
        "string": "str",
        "char": "str",
        "boolean": "bool",
        "void": "None"
    }
    for key in type_map.keys():
        p_type = tester.get_python_type(key)
        assert p_type.type == type_map[key]
        assert p_type.requires_typing == False


def test_rule_primative_seq():
    tester = tm.TypeRules()
    seq = 'sequence< long >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == 'typing.List[int]'
    assert p_type.requires_typing
    seq = 'sequence<string>'
    p_type = tester.get_python_type(seq)
    assert p_type.type == 'typing.List[str]'
    assert p_type.requires_typing
    seq = 'aDXArray<string>'
    p_type = tester.get_python_type(seq)
    assert p_type.type == 'typing.List[str]'
    assert p_type.requires_typing
    rule = tm.RuleSeqLikePrimative(tester)
    seq = 'sequence<string>'
    assert rule.get_is_match(seq) == True
    seq = 'sequence< Pair >'
    assert rule.get_is_match(seq) == False
    seq = 'sequence< com.sun.star.beans.Pair< string, string > >'
    assert rule.get_is_match(seq) == False


def test_rule_seq():
    tester = tm.TypeRules()
    seq = 'sequence< com.sun.star.beans.XThing >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "'typing.List[XThing]'"
    assert p_type.requires_typing
    assert p_type.imports == set(['com.sun.star.beans.XThing'])
    rule = tm.RuleSeqLikeNonPrim(tester)
    seq = 'sequence< .com.sun.star.beans.XThing >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "'typing.List[XThing]'"
    assert p_type.requires_typing
    assert p_type.imports == set(['com.sun.star.beans.XThing'])
    seq = 'sequence< XThing >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "'typing.List[XThing]'"
    assert p_type.requires_typing
    assert p_type.imports == set(['XThing'])
    seq = 'sequence< long >'
    assert rule.get_is_match(seq) == False

def test_rule_com():
    # RuleComType
    tester = tm.TypeRules()
    seq = 'com.sun.star.beans.Pair'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "tuple"
    assert p_type.requires_typing == False
    assert len(p_type.imports) == 0
    rule = tm.RuleComType(tester)
    seq = 'com.sun.star.beans.Pair'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "Pair"
    assert p_type.requires_typing == False
    assert p_type.imports == set(['com.sun.star.beans.Pair'])
    seq = 'sequence< .com.sun.star.beans.XThing >'
    assert rule.get_is_match(seq) == False
    seq = '.com.sun.star.beans.XThing'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "XThing"
    assert p_type.requires_typing == False
    assert p_type.imports == set(['com.sun.star.beans.XThing'])
    seq = 'XThing'
    assert rule.get_is_match(seq) == False

def test_rule_tup2():
    tester = tm.TypeRules()
    seq = 'com.sun.star.beans.Pair< string, string >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "typing.Tuple[str, str]"
    assert p_type.requires_typing
    assert len(p_type.imports) == 0
    rule = tm.RuleTuple2Like(tester)
    seq = 'com.sun.star.beans.Pair< string, string >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[str, str]"
    assert p_type.requires_typing
    assert len(p_type.imports) == 0
    seq = 'com.sun.star.beans.Pair< com.sun.star.uno.XInterface, string >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.requires_typing
    assert p_type.imports == set(['com.sun.star.uno.XInterface'])
    assert p_type.type == "'typing.Tuple[XInterface, str]'"
    seq = 'sequence< com.sun.star.uno.XInterface >'
    assert rule.get_is_match(seq) == False


def test_rule_seq_pair():
    tester = tm.TypeRules()
    seq = 'sequence< com.sun.star.beans.Pair< string, string > >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "typing.List[typing.Tuple[str, str]]"
    assert p_type.requires_typing
    assert len(p_type.imports) == 0
    rule = tm.RuleSeqLikePair(tester)
    seq = 'sequence< com.sun.star.beans.Pair< string, string > >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.List[typing.Tuple[str, str]]"
    assert p_type.requires_typing
    assert len(p_type.imports) == 0
    seq = 'sequence< com.sun.star.beans.Pair< com.sun.star.uno.XInterface, com.sun.star.uno.XInterface > >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "'typing.List[typing.Tuple[XInterface, XInterface]]'"
    assert p_type.requires_typing
    assert p_type.imports == set(['com.sun.star.uno.XInterface'])
    