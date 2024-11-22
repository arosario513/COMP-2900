#!venv/bin/python3
'''Main File'''

from random import randint, shuffle
from sorting_algorithms import bubble, selection

unsorted_asc: list[int] = list(range(0, 100_001))
unsorted_dec: list[int] = unsorted_asc.copy()[::-1]
unsorted_random: list[int] = list(randint(0, 100_000) for _ in range(0, 1001))
shuffle(unsorted_random)


print(unsorted_dec)
