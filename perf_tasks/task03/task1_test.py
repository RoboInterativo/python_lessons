import pytest

from task import *


def test_email():
    result= validate("alex.pricker@gmail.com",email_pattern)
    assert result ==True

def test_broke_email():
    result= validate("alex.prickergmail.com",email_pattern)
    assert result ==False

def test_phone():
    result= validate("+7-968-194-67-60",phone_pattern)
    assert result ==True

def test_login():
    result= validate("alexpricker",username_pattern)
    assert result ==True

def test_wrong_login():
    result= validate("123alexpricker",username_pattern)
    assert result ==False
# def test_broke_email():
#     result= validate("alex.prickergmail.com",email_pattern)
#     assert result ==False
# def test_2():
#     result= myfunc("abbu")
#     assert result ==False
