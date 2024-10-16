#!venv/bin/python3
'''Testing Algorithms'''

from random import sample
from timeit import timeit
from sorting import bubble_sort, quick_sort

items: int = 1000
unsorted: list[int] = sample(range(0, 100_000), items)


def main() -> None:
    '''Main function'''
    print(f'Items in list: {items}\n')

    qs_time: float = timeit('quick_sort(unsorted)',
                            globals=globals(), number=10)
    bs_time: float = timeit('bubble_sort(unsorted)',
                            globals=globals(), number=10)

    print(f'Quicksort:  {qs_time:.4f}s')
    print(f'Bubblesort: {bs_time:.4f}s')


if __name__ == "__main__":
    main()
