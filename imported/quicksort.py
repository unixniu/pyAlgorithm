__author__ = 'xniu'
'''
quicksort, best: nlogn; avg: nlogn; worst: n ^ 2, memory: logn on average; stable: no
'''

def quicksort(a, start, end):
    if (end - start) < 1:
        return

    split = partition(a, start, end)
    quicksort(a, start, split)
    quicksort(a, split+1, end)


def partition(a, start, end):
    pivot = a[start]
    j, k = start, end
    while True:
        while a[j] < pivot:
            j += 1
        while a[k] > pivot:
            k -= 1
        if j < k:
            swap(a, j, k)
            j += 1
            k -= 1
        else:
            return k if k >=0 else 0


def swap (a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


if __name__ == '__main__':
    a = [3, 5, 1, 9, 2, 6, 4, 8, 7]
    quicksort(a, 0, len(a)-1)
    print(a)