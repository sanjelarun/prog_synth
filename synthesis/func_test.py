def mapper(nums: list):
    for i in range(len(nums)):
        nums[i] = nums[i] * 3
    return nums



def test_function():
    assert mapper([1,1,1]) == [3,3,3]


def test_function_2():
    assert mapper() != 3

def test_function_3():
    assert mapper() != "asdasd"
