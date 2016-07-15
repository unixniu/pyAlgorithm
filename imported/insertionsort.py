__author__ = 'xniu'
'''
insertion sort, best: n; avg: n ^ 2; worst: n ^ 2, memory: 1; stable: yes
'''

def insertsort(a):
    for i in range(1, len(a)):
        for j in range(i-1, -1, -1):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
            else:
                break


if __name__ == '__main__':
    a = [3, 5, 1, 9, 2, 6, 4, 8, 7]
    insertsort(a)
    print(a)

