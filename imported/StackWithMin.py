__author__ = 'william'
'''
定义栈的数据结构，要求添加一个min函数，能够得到栈的最小元素。要求函数min、push以及pop的时间复杂度都是O(1)。
http://stackoverflow.com/questions/685060/design-a-stack-such-that-getminimum-should-be-o1
'''


class StackWithMin:
    data = []
    auxiliary = []

    def push(self, val):
        self.data.append(val)
        if len(self.auxiliary) == 0:
            self.auxiliary.append(val)
        else:
            currentMin = self.auxiliary[-1]
            self.auxiliary.append(currentMin if currentMin <= val else val)

    def pop(self):
        if len(self.data) > 0:
            x = self.data[-1]
            del self.data[-1]
            del self.auxiliary[-1]
            return x
        else:
            return None

    def min(self):
        return None if len(self.auxiliary) == 0 else self.auxiliary[-1]


if __name__ == "__main__":
    s = StackWithMin()
    s.push(9)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(1)

    for i in range(0, 9):
        print('current min: ', s.min())
        print('popped: : ', s.pop())

