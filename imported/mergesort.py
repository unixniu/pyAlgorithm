__author__ = 'xniu'
'''
mergesort, best: nlogn; avg: nlogn; worst: nlogn, memory: n; stable: yes
'''

import math

# sort array a from start (inclusive) to end (exclusive)
def mergesort(a, start, end, b):
    if (end - start) < 2:
        return

    mid = int((start + end) / 2)
    mergesort(a, start, mid, b)
    mergesort(a, mid, end, b)
    merge(a, start, mid, end, b)
    copy(b, start, end, a)


# merge two parts of array split at mid
def merge(a, start, mid, end, b):
    i, j = start, mid
    x = 0
    for x in range(start, end):
        if i < mid and (j >= end or a[i] < a[j]):
            b[x] = a[i]
            i += 1
        else:
            b[x] = a[j]
            j += 1


def copy(a, start, end, b):
    for x in range(start, end):
        b[x] = a[x]


if __name__ == '__main__':
    a = [3, 5, 1, 9, 2, 6, 4, 8, 7]
    b = [0 for x in range(len(a))]
    mergesort(a, 0, len(a), b)
    print(a)