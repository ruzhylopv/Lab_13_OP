class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
from collections import deque

# Pre-order traversal
def pre_order(node):
    res = []
    stack = deque()
    if node:
        stack.append(node)

    while stack:
        probe = stack.pop()
        for n in [probe.right,probe.left]:
            if n:
                stack.append(n)
        res.append(probe.data)
    return res


def pre_order_recursive(node):
    if node is None:
        return []
    return [node.data] + pre_order_recursive(node.left) + pre_order_recursive(node.right)

# In-order traversal
def in_order(node):
    if node is None:
        return []
    # if node.left is None:
    #     return [node.data]

    # lst = []
    # lst.extend(in_order(node.left))
    # lst.append(node.data)
    # lst.extend(in_order(node.right))
    return in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    # if node.left is None:
    #     return [node.data]
    
    return post_order(node.left) + post_order(node.right) + [node.data]


a = Node('1')
b = Node('2')
c = Node('3')
d = Node('4')
e = Node('5')
f = Node('6')
g = Node('7')

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g


print(pre_order(a))
print(in_order(a))
print(post_order(a))
print(pre_order_recursive(a))