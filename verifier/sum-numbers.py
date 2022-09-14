from typing import List

def sum_num(nums: List[int]) -> int:
    s = 0
    for i in nums:
        s += i
    return s


def test_case_0():
    int_0 = -2799
    list_0 = [int_0, int_0, int_0]
    int_1 = sum_num(list_0)
    assert int_1 == -8391


def test_case_1():
    list_0 = []
    int_0 = sum_num(list_0)
    assert int_0 == 0