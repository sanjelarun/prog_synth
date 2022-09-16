from typing import List

def func_0 (dataset: List[int]):
    total = 0 

    for i in dataset:
    if i % 2 == 0:
        total = i * 2 + total

    return t