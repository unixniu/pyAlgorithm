__author__ = 'xniu'
'''
heapsort, best: nlogn; avg: nlogn; worst: nlogn, memory: 1; stable: no
'''

import math


def heapsort(a):
    heapify(a, len(a))
    for end in range(len(a) - 1, 0, -1):
        swap(a, 0, end)
        siftdown(a, 0, end - 1)


# this siftDown version of heapify treats the entire input array as a full but "broken" heap and "repairs"
# it starting from the last non-trivial sub-heap (that is, the last parent node).
# whereas siftUp version can be visualized as starting with an empty heap and successively inserting elements
def heapify(a, c):
    end = c - 1
    p = parent(end)
    while p >= 0:
        siftdown(a, p, c - 1)
        p -= 1


# repair the heap whose root is at index start, assuming sub-heaps rooted at its children are valid
# last element in the heap is at index end.
def siftdown(a, start, end):
    root = start
    while leftChild(root) <= end:
        lchild = leftChild(root)
        s = root
        if a[root] < a[lchild]:
            s = lchild
        rchild = lchild + 1
        if rchild <= end and a[rchild] > a[s]:
            s = rchild
        if s == root:
            return
        else:
            swap(a, root, s)
            root = s


def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


def leftChild(x):
    return 2 * x + 1


def parent(x):
    return math.floor((x - 1) / 2)


if __name__ == '__main__':
    a = [3, 5, 1, 9, 2, 6, 4, 8, 7]
    heapsort(a)
    print(a)