__author__ = 'william'
# -*- coding:utf-8 -*-
'''
在一个字符串中找到第一个只出现一次的字符。如输入abaccdeff，则输出b。 分析：这道题是2006年google的一道笔试题。
In Java, you could use a LinkedHashMap<Character,Integer> to count how many times each character appears in the string.
Since LinkedHashMap preserves insertion order, you could then iterate over its entries to find the first character that
appears exactly once.
'''


def find_first_single_occurrence(str):
    hashmap = {}
    for i, c in enumerate(str):
        if c in hashmap:
            hashmap[c] = -1
        else:
            hashmap[c] = i
    ret = None
    min = -1
    for k, v in hashmap.items():
        if v == -1:
            continue
        elif min == -1 or min > v:
            min = v
            ret = k
    return ret


if __name__ == "__main__":
    str = "awysdfhghdfgqafds"
    print("first single occurrence char in \'{}\' is {}".format(str, find_first_single_occurrence(str)))


