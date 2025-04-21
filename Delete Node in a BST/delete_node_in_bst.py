
from collections import deque
def bfs(node):
    res = []
    queue = deque()
    if node:
        queue.append(node)

    while queue:
        probe = queue.popleft()
        if not probe:
            res.append(None)
            continue
        for n in [probe.left, probe.right]:
            queue.append(n)
        if probe:

            res.append(probe.val)
    return res





class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{bfs(self)}'
        

    def __repr__(self):
        if self.left:
            l = self.left.val
        else:
            l = None
        if self.right:
            r = self.right.val
        else:
            r = None
        return f'Node({self.val}, left: {l}, right: {r})'


class Solution:

    def leftMax(self, curr: TreeNode):
        while curr and curr.right:
            curr = curr.right
        return curr

    def deleteNode(self, root: TreeNode, key: int):
        if root is None:
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # print(root.left)
                lmax = self.leftMax(root.left)
                root.val = lmax.val
                root.left = self.deleteNode(root.left, lmax.val)
        return root

root = TreeNode(5)
root.right = TreeNode(6)
root.right.right = TreeNode(7)


root.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left = TreeNode(2)




# root1 = TreeNode(0)
# print(Solution.deleteNode(Solution, root, 3))
s = Solution()

print(s.deleteNode(root, 3))