__author__ = 'william'
'''
count the number of 1's in binary representation of given integer.
'''


def count1(a):
    import math
    n = math.floor(math.log(a, 2))
    count = 0
    x = 1
    for i in range(0, n):
        if a & x == x:
            count += 1
        x <<= 1
    return count + 1


'''Please note the fact that: n&(n-1) always eliminates the least significant 1.'''
def count1_better(a):
    count = 0
    while a != 0:
        a = (a & (a-1))
        count += 1
    return count


if __name__ == "__main__":
    a = 235220
    print("number of 1 in {0:#b}: {1}".format(a, count1_better(a)))
