__author__ = 'william'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def ReverseList(pHead):
    # write code here
    pre = None
    cur = pHead
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return pre


def printList(pHead):
    cur = pHead
    l = []
    while cur:
        l.append(cur.val)
        cur = cur.next
    print(", ".join(map(lambda x: str(x), l)))


if __name__ == "__main__":
    nodes = []
    for i in range(1, 10):
        nodes.append(ListNode(i))
    for i in range(0, len(nodes)):
        nodes[i].next = None if i + 1 >= len(nodes) else nodes[i+1]

    printList(nodes[0])
    printList(ReverseList(nodes[0]))
