# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2009- Spyder Kernels Contributors
#
# Licensed under the terms of the MIT License
# (see spyder_kernels/__init__.py for details)
# -----------------------------------------------------------------------------

"""
Tests for dochelpers.py
"""
# Standard library imports
import os
import sys

# Test library imports
import pytest

# Local imports
from spyder_kernels.utils.dochelpers import (getargtxt, getdoc, getobj,
                                             isdefined)
from spyder_kernels.py3compat import PY2


class Test(object):
    def method(self, x, y=2):
        pass


@pytest.mark.skipif(not PY2, reason="It fails in Python 3")
def test_dochelpers():
    """Test dochelpers."""
    assert not getargtxt(Test.__init__)
    if PY2:                    
        assert getargtxt(Test.method) == ['x, ', 'y=2']
        assert getdoc(sorted) == {'note': 'Function of __builtin__ module',
                                  'argspec': u'(iterable, cmp=None, key=None, '
                                              'reverse=False)',
                                  'docstring': u'sorted(iterable, cmp=None, '
                                                'key=None, reverse=False) --> '
                                                'new sorted list',
                                  'name': 'sorted'}
        assert getargtxt(sorted) == ['iterable, ', ' cmp=None, ',
                                     ' key=None, ', ' reverse=False']
    else:
        assert not getargtxt(Test.method)
        if os.name == 'nt':
            assert getdoc(sorted) == {'note': 'Function of builtins module',
                                      'argspec': '(...)',
                                      'docstring': 'Return a new list '
                                                   'containing '
                                                   'all items from the '
                                                   'iterable in ascending '
                                                   'order.\n\nA custom '
                                                   'key function can be '
                                                   'supplied to customise the '
                                                   'sort order, and '
                                                   'the\nreverse flag can be '
                                                   'set to request the result '
                                                   'in descending order.',
                                      'name': 'sorted'}
        else:
            assert getdoc(sorted) == {'note': 'Function of builtins module',
                                      'argspec': '(...)',
                                      'docstring': 'Return a new list '
                                                   'containing '
                                                   'all items from the '
                                                   'iterable in ascending '
                                                   'order.\n\nA custom '
                                                   'key function can be '
                                                   'supplied to customize the '
                                                   'sort order, and '
                                                   'the\nreverse flag can be '
                                                   'set to request the result '
                                                   'in descending order.',
                                      'name': 'sorted'}
        assert not getargtxt(sorted)
    assert isdefined('numpy.take', force_import=True)
    assert isdefined('__import__')
    assert not isdefined('.keys', force_import=True)
    assert getobj('globals') == 'globals'
    assert not getobj('globals().keys')
    assert getobj('+scipy.signal.') == 'scipy.signal'
    assert getobj('4.') == '4'


if __name__ == "__main__":
    pytest.main()
