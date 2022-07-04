# coding: utf-8
import pytest

if __name__ == "__main__":
    pytest.main([__file__])

import src.parser.mod_type as tm


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
        assert p_type.is_py_type
        assert p_type.realtype == type_map[key]


def test_rule_primative_seq():
    tester = tm.TypeRules()
    seq = 'sequence< long >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == 'typing.Tuple[int, ...]'
    assert p_type.requires_typing
    assert p_type.is_py_type
    assert p_type.realtype == 'tuple'
    assert p_type.origin == seq
    assert p_type.origtype == None
    assert len(p_type.children) == 1
    p_child = p_type.children[0]
    assert p_child.type == 'int'
    assert p_child.realtype == 'int'
    assert p_child.is_py_type
    assert p_child.requires_typing == False
    assert len(p_child.children) == 0
    assert len(p_child.get_all_from_imports()) == 0

    seq = 'sequence<string>'
    p_type = tester.get_python_type(seq)
    assert p_type.type == 'typing.Tuple[str, ...]'
    assert p_type.requires_typing
    assert p_type.is_py_type
    seq = 'aDXArray<string>'
    p_type = tester.get_python_type(seq)
    assert p_type.type == 'typing.List[str]'
    assert p_type.realtype == 'list'
    assert p_type.requires_typing
    assert p_type.is_py_type
    p_child = p_type.children[0]
    assert p_child.type == 'str'
    assert p_child.realtype == 'str'
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
    assert p_type.type == "typing.Tuple[XThing, ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == False
    assert p_type.realtype == 'tuple'
    assert p_type.get_all_from_imports() == set(['com.sun.star.beans.XThing'])
    assert len(p_type.children) == 1
    p_child = p_type.children[0]
    assert p_child.type == 'XThing'
    assert p_child.realtype == 'XThing'
    assert p_child.is_py_type == False
    assert p_child.requires_typing == True
    assert len(p_child.children) == 0
    assert len(p_child.get_all_from_imports()) == 0

    rule = tm.RuleSeqLikeNonPrim(tester)
    seq = 'sequence< .com.sun.star.beans.XThing >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[XThing, ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == False
    assert p_type.get_all_from_imports() == set(['com.sun.star.beans.XThing'])
    assert len(p_type.children) == 1
    p_child = p_type.children[0]
    assert p_child.type == 'XThing'
    assert p_child.realtype == 'XThing'
    assert p_child.is_py_type == False
    assert p_child.requires_typing == True
    assert len(p_child.children) == 0
    assert len(p_child.get_all_from_imports()) == 0

    seq = 'sequence< XThing >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[XThing, ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == False
    assert p_type.get_all_from_imports() == set(['XThing'])
    assert len(p_type.children) == 1
    p_child = p_type.children[0]
    assert p_child.type == 'XThing'
    assert p_child.realtype == 'XThing'
    assert p_child.is_py_type == False
    assert p_child.requires_typing == True
    assert len(p_child.children) == 0
    assert len(p_child.get_all_from_imports()) == 0

    seq = 'sequence< long >'
    assert rule.get_is_match(seq) == False
    # type is part of TYPE_MAP_KNOWN_PRIMITAVE
    seq = 'sequence< type >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[object, ...]"
    assert p_type.requires_typing
    assert len(p_type.get_all_from_imports()) == 0
    assert len(p_type.children) == 1
    p_child = p_type.children[0]
    assert p_child.type == 'object'
    assert p_child.realtype == 'object'
    assert p_child.is_py_type == True
    assert p_child.requires_typing == False
    assert len(p_child.children) == 0
    assert len(p_child.get_all_from_imports()) == 0


def test_rule_seq_ns():
    ns = 'com.sun.star.uno'
    tester = tm.TypeRules(ns=ns)
    seq = 'sequence< com.sun.star.beans.XThing >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "typing.Tuple[XThing, ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == False
    assert p_type.realtype == 'tuple'
    assert p_type.get_all_from_imports(
        ns=ns) == set(['com.sun.star.beans.XThing'])
    assert len(p_type.children) == 1
    p_child = p_type.children[0]
    assert p_child.type == 'XThing'
    assert p_child.realtype == 'XThing'
    assert p_child.is_py_type == False
    assert p_child.requires_typing == True
    assert len(p_child.children) == 0
    assert len(p_child.get_all_from_imports()) == 0

    rule = tm.RuleSeqLikeNonPrim(tester)
    seq = 'sequence< .com.sun.star.beans.XThing >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[XThing, ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == False
    assert p_type.get_all_from_imports(
        ns=ns) == set(['com.sun.star.beans.XThing'])
    assert len(p_type.children) == 1
    p_child = p_type.children[0]
    assert p_child.type == 'XThing'
    assert p_child.realtype == 'XThing'
    assert p_child.is_py_type == False
    assert p_child.requires_typing == True
    assert len(p_child.children) == 0
    assert len(p_child.get_all_from_imports()) == 0

    seq = 'sequence< XThing >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[XThing, ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == False
    assert p_type.get_all_from_imports(
        ns=ns) == set(['com.sun.star.uno.XThing'])
    assert len(p_type.children) == 1
    p_child = p_type.children[0]
    assert p_child.type == 'XThing'
    assert p_child.realtype == 'XThing'
    assert p_child.is_py_type == False
    assert p_child.requires_typing == True
    assert len(p_child.children) == 0
    assert len(p_child.get_all_from_imports()) == 0

    seq = 'sequence< long >'
    assert rule.get_is_match(seq) == False
    # type is part of TYPE_MAP_KNOWN_PRIMITAVE
    seq = 'sequence< type >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[object, ...]"
    assert p_type.requires_typing
    assert len(p_type.get_all_from_imports(ns=ns)) == 0
    assert len(p_type.children) == 1
    p_child = p_type.children[0]
    assert p_child.type == 'object'
    assert p_child.realtype == 'object'
    assert p_child.is_py_type == True
    assert p_child.requires_typing == False
    assert len(p_child.children) == 0
    assert len(p_child.get_all_from_imports(ns=ns)) == 0


def test_rule_com():
    # RuleComType
    tester = tm.TypeRules()
    seq = 'com.sun.star.beans.Pair'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "tuple"
    assert p_type.realtype == "tuple"
    assert p_type.requires_typing == False
    assert p_type.is_py_type
    assert len(p_type.get_all_from_imports()) == 0
    rule = tm.RuleComType(tester)
    seq = 'com.sun.star.beans.Pair'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "Pair"
    assert p_type.requires_typing == False
    assert p_type.is_py_type == False
    assert p_type.get_all_from_imports() == set(['com.sun.star.beans.Pair'])
    seq = 'sequence< .com.sun.star.beans.XThing >'
    assert rule.get_is_match(seq) == False
    seq = '.com.sun.star.beans.XThing'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "XThing"
    assert p_type.realtype == "XThing"
    assert p_type.requires_typing == False
    assert p_type.get_all_from_imports() == set(['com.sun.star.beans.XThing'])
    assert p_type.is_py_type == False
    seq = 'XThing'
    assert rule.get_is_match(seq) == False


def test_rule_com_ns():
    # RuleComType
    ns = 'com.sun.star.uno'
    tester = tm.TypeRules(ns=ns)
    seq = 'com.sun.star.beans.Pair'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "tuple"
    assert p_type.realtype == "tuple"
    assert p_type.requires_typing == False
    assert p_type.is_py_type
    assert len(p_type.get_all_from_imports(ns=ns)) == 0
    rule = tm.RuleComType(tester)
    seq = 'com.sun.star.beans.Pair'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "Pair"
    assert p_type.requires_typing == False
    assert p_type.is_py_type == False
    assert p_type.get_all_from_imports() == set(['com.sun.star.beans.Pair'])
    seq = 'sequence< .com.sun.star.beans.XThing >'
    assert rule.get_is_match(seq) == False
    seq = '.com.sun.star.beans.XThing'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "XThing"
    assert p_type.realtype == "XThing"
    assert p_type.requires_typing == False
    assert p_type.get_all_from_imports(
        ns=ns) == set(['com.sun.star.beans.XThing'])
    assert p_type.is_py_type == False
    seq = 'XThing'
    assert rule.get_is_match(seq) == False


def test_rule_tup2():
    tester = tm.TypeRules()
    seq = 'com.sun.star.beans.Pair< string, string >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "typing.Tuple[str, str]"
    assert p_type.realtype == 'tuple'
    assert p_type.requires_typing
    assert p_type.is_py_type == True
    im = p_type.get_all_from_imports()
    assert len(im) == 0
    p1 = p_type.children[0]
    p2 = p_type.children[1]
    assert p1.type == 'str'
    assert p1.realtype == 'str'
    assert p2.type == 'str'
    assert p2.realtype == 'str'
    rule = tm.RuleTuple2Like(tester)
    seq = 'com.sun.star.beans.Pair< string, string >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[str, str]"
    assert p_type.realtype == 'tuple'
    assert p_type.requires_typing
    assert p_type.is_py_type == True
    im = p_type.get_all_from_imports()
    assert len(im) == 0
    p1 = p_type.children[0]
    p2 = p_type.children[1]
    assert p1.type == 'str'
    assert p1.realtype == 'str'
    assert p2.type == 'str'
    assert p2.realtype == 'str'
    seq = 'com.sun.star.beans.Pair< com.sun.star.uno.XInterface, string >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.requires_typing
    assert p_type.get_all_from_imports() == set(
        ['com.sun.star.uno.XInterface'])
    assert p_type.type == "typing.Tuple[XInterface, str]"
    assert p_type.realtype == 'tuple'
    assert p_type.is_py_type == False
    p1 = p_type.children[0]
    p2 = p_type.children[1]
    assert p1.type == 'XInterface'
    assert p1.realtype == 'XInterface'
    assert p1.is_py_type == False
    assert p2.type == 'str'
    assert p2.realtype == 'str'
    assert p2.is_py_type == True
    seq = 'sequence< com.sun.star.uno.XInterface >'
    assert rule.get_is_match(seq) == False


def test_rule_tup2_ns():
    ns = 'com.sun.star.uno'
    tester = tm.TypeRules(ns=ns)
    seq = 'com.sun.star.beans.Pair< string, string >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "typing.Tuple[str, str]"
    assert p_type.realtype == 'tuple'
    assert p_type.requires_typing
    assert p_type.is_py_type == True
    im = p_type.get_all_from_imports(ns=ns)
    assert len(im) == 0
    p1 = p_type.children[0]
    p2 = p_type.children[1]
    assert p1.type == 'str'
    assert p1.realtype == 'str'
    assert p2.type == 'str'
    assert p2.realtype == 'str'
    rule = tm.RuleTuple2Like(tester)
    seq = 'com.sun.star.beans.Pair< string, string >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[str, str]"
    assert p_type.realtype == 'tuple'
    assert p_type.requires_typing
    assert p_type.is_py_type == True
    im = p_type.get_all_from_imports(ns=ns)
    assert len(im) == 0
    p1 = p_type.children[0]
    p2 = p_type.children[1]
    assert p1.type == 'str'
    assert p1.realtype == 'str'
    assert p2.type == 'str'
    assert p2.realtype == 'str'
    seq = 'com.sun.star.beans.Pair< com.sun.star.uno.XInterface, string >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.requires_typing
    assert p_type.get_all_from_imports(ns=ns) == set(
        ['com.sun.star.uno.XInterface'])
    assert p_type.type == "typing.Tuple[XInterface, str]"
    assert p_type.realtype == 'tuple'
    assert p_type.is_py_type == False
    p1 = p_type.children[0]
    p2 = p_type.children[1]
    assert p1.type == 'XInterface'
    assert p1.realtype == 'XInterface'
    assert p1.is_py_type == False
    assert p2.type == 'str'
    assert p2.realtype == 'str'
    assert p2.is_py_type == True
    assert p_type.origin == seq
    assert p_type.origtype is None
    seq = 'sequence< com.sun.star.uno.XInterface >'
    assert rule.get_is_match(seq) == False


def test_rule_seq_pair():
    tester = tm.TypeRules()
    seq = 'sequence< com.sun.star.beans.Pair< string, string > >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "typing.Tuple[typing.Tuple[str, str], ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == True
    assert len(p_type.get_all_from_imports()) == 0
    rule = tm.RuleSeqLikePair(tester)
    seq = 'sequence< com.sun.star.beans.Pair< string, string > >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[typing.Tuple[str, str], ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == True
    assert len(p_type.get_all_from_imports()) == 0
    seq = 'sequence< com.sun.star.beans.Pair< com.sun.star.uno.XInterface, com.sun.star.uno.XInterface > >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[typing.Tuple[XInterface, XInterface], ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == False
    assert p_type.get_all_from_imports() == set(
        ['com.sun.star.uno.XInterface'])


def test_rule_seq_pair_ns():
    ns = 'com.sun.star.uno'
    tester = tm.TypeRules(ns=ns)
    seq = 'sequence< com.sun.star.beans.Pair< string, string > >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "typing.Tuple[typing.Tuple[str, str], ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == True
    assert len(p_type.get_all_from_imports(ns=ns)) == 0
    rule = tm.RuleSeqLikePair(tester)
    seq = 'sequence< com.sun.star.beans.Pair< string, string > >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[typing.Tuple[str, str], ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == True
    assert len(p_type.get_all_from_imports(ns=ns)) == 0
    seq = 'sequence< com.sun.star.beans.Pair< com.sun.star.uno.XInterface, com.sun.star.uno.XInterface > >'
    assert rule.get_is_match(seq)
    p_type = rule.get_python_type(seq)
    assert p_type.type == "typing.Tuple[typing.Tuple[XInterface, XInterface], ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == False
    assert p_type.get_all_from_imports(ns=ns) == set(
        ['com.sun.star.uno.XInterface'])


def test_python_type_imports():
    p_a = tm.PythonType(from_imports='a')
    p_b = tm.PythonType(from_imports='b')
    p_c = tm.PythonType(from_imports='c')
    p_1a = tm.PythonType(from_imports='1a')
    p_1b = tm.PythonType(from_imports='1b')
    p_1c = tm.PythonType(from_imports='1c')
    p_1c_a = tm.PythonType(from_imports='1ca')
    p_1c.children.append(p_1c_a)
    p_a.children.append(p_1a)
    p_b.children.append(p_1b)
    p_c.children.append(p_1c)
    p_main = tm.PythonType(from_imports='main')
    p_main.children.append(p_a)
    p_main.children.append(p_b)
    p_main.children.append(p_c)
    im = set([
        'a',
        'b',
        'c',
        '1a',
        '1b',
        '1c',
        '1ca',
        'main'
    ])
    imports = p_main.get_all_from_imports()
    assert imports == im


def test_python_type_imports_ns():
    ns = 'com.sun.star.uno'
    p_a = tm.PythonType(from_imports='a')
    p_b = tm.PythonType(from_imports='b')
    p_c = tm.PythonType(from_imports='c')
    p_1a = tm.PythonType(from_imports='1a')
    p_1b = tm.PythonType(from_imports='1b')
    p_1c = tm.PythonType(from_imports='1c')
    p_1c_a = tm.PythonType(from_imports='1ca')
    p_1c.children.append(p_1c_a)
    p_a.children.append(p_1a)
    p_b.children.append(p_1b)
    p_c.children.append(p_1c)
    p_main = tm.PythonType(from_imports='main')
    p_main.children.append(p_a)
    p_main.children.append(p_b)
    p_main.children.append(p_c)
    im = set([
        'com.sun.star.uno.a',
        'com.sun.star.uno.b',
        'com.sun.star.uno.c',
        'com.sun.star.uno.1a',
        'com.sun.star.uno.1b',
        'com.sun.star.uno.1c',
        'com.sun.star.uno.1ca',
        'com.sun.star.uno.main'
    ])
    imports = p_main.get_all_from_imports(ns=ns)
    assert imports == im


def test_typedef():
    tester = tm.TypeRules()
    seq = 'typedef sequence< any >'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "typing.Tuple[object, ...]"
    assert p_type.requires_typing
    assert p_type.is_py_type == True
    im = p_type.get_all_from_imports()
    assert len(im) == 0


def test_signed():
    tester = tm.TypeRules()
    seq = 'signed char'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "str"
    assert p_type.requires_typing == False
    assert p_type.is_py_type == True
    assert p_type.origin == "char"
    assert p_type.origtype is None
    p2 = p_type.copy()
    assert p2.type == "str"
    assert p2.requires_typing == False
    assert p2.is_py_type == True
    assert p2.origin == "char"
    assert p2.origtype is None


def test_unsigned():
    tester = tm.TypeRules()
    seq = 'unsigned long'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "int"
    assert p_type.requires_typing == False
    assert p_type.is_py_type == True
    assert p_type.origin == "long"
    assert p_type.origtype is None


def test_long():
    tester = tm.TypeRules()
    seq = 'long long'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "int"
    assert p_type.requires_typing == False
    assert p_type.is_py_type == True


def test_short():
    tester = tm.TypeRules()
    seq = 'short short'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "int"
    assert p_type.requires_typing == False
    assert p_type.is_py_type == True


def test_unsigned_short():
    # there is no specific rule for unsigned short int
    # rules are matched recurivly for rules based upon RuleBaseWord
    # there is a rule for unsigned (RuleWordUnSigned) and a rule for short ( RuleWordShort )
    tester = tm.TypeRules()
    seq = 'unsigned short int'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "int"
    assert p_type.requires_typing == False
    assert p_type.is_py_type == True


def test_long_long_int_short():
    # there is no specific rule for unsigned short int
    # rules are matched recurivly for rules based upon RuleBaseWord
    # there is a rule for long (RuleWordLong)
    tester = tm.TypeRules()
    seq = 'long long int'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "int"
    assert p_type.requires_typing == False
    assert p_type.is_py_type == True


def test_hyper():
    # there is no specific rule for unsigned short int
    # rules are matched recurivly for rules based upon RuleBaseWord
    # there is a rule for long (RuleWordLong)
    tester = tm.TypeRules()
    seq = 'hyper'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "int"
    assert p_type.requires_typing == False
    assert p_type.is_py_type == True

    seq = 'hyper long'
    p_type = tester.get_python_type(seq)
    assert p_type.type == "int"
    assert p_type.requires_typing == False
    assert p_type.is_py_type == True
