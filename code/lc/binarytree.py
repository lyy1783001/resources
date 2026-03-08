class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

# 你可以这样构建一棵二叉树：
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

# 构建出来的二叉树是这样的：
#     1
#    / \
#   2   3
#  /   / \
# 4   5   6

"""class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def midtrack(T: TreeNode) -> None:
    if T is None:
        return
    midtrack(T.left)
    midtrack(T.right)
    print(T.val)

midtrack(root)"""

from collections import deque

'''def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        p = q.popleft()
        print(p.val)
        if p.left is not None:
            q.append(p.left)
        if p.right is not None:
            q.append(p.right)
levelOrderTraverse(root)'''
class Status():
    def __init__(self, root:TreeNode, depth:int):
        self.node = root
        self.depth = depth
def levelOrderTraverse2(root:TreeNode):
    if root is None:
        return
    q = deque()
    q.append(Status(root, 1))
    while q:
        p = q.popleft()
        print(f'depth {p.depth}, val:{p.node.val}')
        if p.node.left is not None:
            q.append(Status(p.node.left, p.depth + 1))
        if p.node.right is not None:
            q.append(Status(p.node.right, p.depth + 1))
levelOrderTraverse2(root)