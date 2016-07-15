__author__ = 'william'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.leftChild = None
        self.rightChild = None


def mirror(root):
    if swap(root):
        mirror(root.leftChild)
        mirror(root.rightChild)


def swap(node):
    if node:
        left = node.leftChild
        node.leftChild = node.rightChild
        node.rightChild = left
        return True
    else:
        return False


def inorder(root):
    if root is None:
        return

    inorder(root.leftChild)
    print(root.val)
    inorder(root.rightChild)


if __name__ == "__main__":
    root = TreeNode(10)
    root.leftChild = TreeNode(6)
    root.rightChild = TreeNode(8)
    root.leftChild.leftChild = TreeNode(3)
    root.leftChild.rightChild = TreeNode(4)
    root.rightChild.leftChild = TreeNode(2)
    root.rightChild.rightChild = TreeNode(7)
    inorder(root)
    mirror(root)
    print('after mirror:')
    inorder(root)


