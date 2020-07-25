# -*- coding: utf-8 -*-

import pytest
from annepy.skeleton import fib

__author__ = "Gilberto Charles"
__copyright__ = "Gilberto Charles"
__license__ = "GNU"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
