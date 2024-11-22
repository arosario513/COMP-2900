#!venv/bin/python3
'''Sorting Algorithms'''


def selection(unsorted: list[int]) -> list[int]:
    '''
    Selection Sort
    Args:
        - unsorted (list[int]): Unsorted list
    Returns:
        list[int]: Sorted list
    '''
    for i in range(0, len(unsorted)):
        tmp = i
        for j in range(i+1, len(unsorted)):
            if unsorted[j] < unsorted[tmp]:
                unsorted[j], unsorted[tmp] = unsorted[tmp], unsorted[j]
    return unsorted


def bubble(unsorted: list[int]) -> list[int]:
    '''
    Bubble Sort
    Args:
        - unsorted (list[int]): Unsorted list
    Returns:
        list[int]: Sorted list
    '''

    for i in range(0, len(unsorted) - 1):
        for j in range(0, len(unsorted) - 1 - i):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

    return unsorted
