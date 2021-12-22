# coding: utf-8
import pytest
if __name__ == "__main__":
    import sys
    import os
    # sys.path.append(os.path.realpath('..'))
    pytest.main([__file__])

import parser.type_mod as tm


def test_rule_primative(test_log):
    tester = tm.TypeRules(logger=test_log)
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


def test_rule_primative_seq(test_log):
    tester = tm.TypeRules(logger=test_log)
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

    
