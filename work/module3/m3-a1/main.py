#!venv/bin/python3
'''timing algorithms'''

import timeit


def iterative(n: int) -> int:
    '''iterative factorial'''
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def recursive(n: int) -> int:
    '''recursive factorial'''
    if n == 0:
        return 1
    return n * recursive(n-1)


def main() -> None:
    '''main function'''
    it_time = timeit.timeit(
        'iterative(10)', globals=globals(), number=10000)

    rec_time = timeit.timeit(
        'recursive(10)', globals=globals(), number=10000)

    print(f"Iterative Time: {it_time} seconds")
    print(f"Recursive Time: {rec_time} seconds")


if __name__ == '__main__':
    main()
