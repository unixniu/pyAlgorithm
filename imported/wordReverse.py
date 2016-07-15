__author__ = 'william'
# -*- coding:utf-8 -*-
'''
"I am a student.” -> "student. a am I"
'''


def reverse(line):
    return " ".join(reversed(line.split()))


if __name__ == "__main__":
    line = "this is, to test this program!"
    print(reverse(line))
