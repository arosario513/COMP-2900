#!venv/bin/python3
"""Main File"""

from timeit import timeit
from random import randint, shuffle
from concurrent.futures import ProcessPoolExecutor
from sorting_algorithms import bubble, selection
import pandas as pd


def gen_test_cases(in_size):
    '''Create the test cases (best, worst, average)'''
    unsorted_asc = list(range(in_size + 1))
    unsorted_dec = unsorted_asc[::-1]
    unsorted_random = [randint(0, in_size) for _ in range(in_size + 1)]
    shuffle(unsorted_random)
    return {"asc": unsorted_asc, "dec": unsorted_dec, "rand": unsorted_random}


def get_time(algorithm, data):
    '''Get the time of the sorting algorithm'''
    time = timeit(lambda: algorithm(data.copy()), number=1)
    return time


input_sizes = range(10_000, 101_000, 10_000)
algs = {"selection": selection, "bubble": bubble}

algorithm_results = {name: [] for name in algs}

with ProcessPoolExecutor() as executor:
    for size in input_sizes:
        test_cases = gen_test_cases(size)

        for name, func in algs.items():
            futures = []
            for case_name, dataset in test_cases.items():
                futures.append(
                    executor.submit(get_time, func, dataset)
                )

            results = [future.result() for future in futures]
            for case_name, elapsed_time in zip(test_cases.keys(), results):
                algorithm_results[name].append(
                    {"Case": case_name, "Input Size": size, "Time": elapsed_time}
                )

for name, results in algorithm_results.items():
    df = pd.DataFrame(results)
    OUTPUT_FILE = f"{name}_results.csv"
    df.to_csv(OUTPUT_FILE, index=False)
    print("[+] Results saved!")
