from typing import List


def temp_gen(n: List[int]) -> int:
    count = 0
    for i in n:
        if i > 1:
            count += 1
    return count
