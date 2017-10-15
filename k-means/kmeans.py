from typing import Iterable
from math import fsum, hypot
from pprint import pprint

points = [
    (10, 41, 23),
    (22, 30, 29),
    (11, 42, 5),
    (20, 32, 4),
    (12, 40, 12),
    (21, 36, 23),
]

def mean(data: Iterable[float]) -> float:
    'Accurate arithmetic mean'
    data = list(data)
    return fsum(data) / len(data)


