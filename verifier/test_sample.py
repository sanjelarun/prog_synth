import pytest


def f():
    return 3


def test_function():
    assert f() == 4


def test_function_2():
    assert f() == 3

def test_function_3():
    assert f() == "asdasd"

def random_func():
    yield