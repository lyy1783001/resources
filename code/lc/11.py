class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(nums:list[int]):
    nodes = [TreeNode(val) if val is not None else None for val in nums]
    n = len(nums)
    for i in range(n):
        if 2*i+1 < n:
            nodes[i].left = nodes[2*i+1]
        if 2*i+2 < n:
            nodes[i].right = nodes[2*i+2]
    return nodes[0]

nums = [1,2,2,None,3,None,3]
root = buildTree(nums)
def f(root:TreeNode)->int:
    def traverse(p, q):
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True
        if p and q:
            return traverse(p.left, q.right) and traverse(p.right, q.left)
    return traverse(root.left, root.right)
print(f(root))