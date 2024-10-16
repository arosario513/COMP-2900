#!venv/bin/python3
'''Sorting Algorithms'''


def bubble_sort(n_list: list[int]) -> list[int]:
    '''Bubblesort Algorithm'''
    tmp: list[int] = n_list.copy()
    for i in range(len(tmp)):
        for j in range(len(tmp) - i - 1):
            if tmp[j] > tmp[j+1]:
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
    return tmp


def quick_sort(n_list: list[int]) -> list[int]:
    '''Quicksort Algorithm'''
    if len(n_list) <= 1:
        return n_list

    pivot: int = n_list.pop()
    low: list[int] = []
    high: list[int] = []

    for i in n_list:
        if i >= pivot:
            high.append(i)
        else:
            low.append(i)

    sorted_list: list[int] = quick_sort(low) + [pivot] + quick_sort(high)
    return sorted_list
