import pytest

from task import *


def test_1():
    result= myfunc("cat runs to another cat","cat","bull")
    assert result =="bull runs to another bull"

def test_2():
    result= myfunc("cat   runs   to   another   cat","cat","bull")
    assert result =="bull   runs   to   another   bull"

def test_3():
    result2="bull   runs   to   another   bull   "
    result= myfunc("cat   runs   to   another   cat   ","cat","bull")
    assert len(result) ==len(result2)
    # assert result =="bull   runs   to   another   bull   "
