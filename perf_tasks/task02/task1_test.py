import pytest

from task import *


def test_1():
    result= myfunc("abba")
    assert result ==True


def test_2():
    result= myfunc("abbu")
    assert result ==False
