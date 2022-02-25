# coding: utf-8
import pytest
if __name__ == "__main__":
    import sys
    import os
    # sys.path.append(os.path.realpath('..'))
    pytest.main([__file__])

def test_root(root_path):
    from oootmpl.utilities import util
    util_root = util.get_root()
    assert str(util_root) == str(root_path)
    