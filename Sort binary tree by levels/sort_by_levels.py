
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
    def __repr__(self):
        return f'{self.value}'

from collections import defaultdict

def tree_by_levels(node):
    levels = defaultdict(list)
    levels[0] = [node]
    i = 0
    while True:

        for n in levels[i]:
            if n is None:
                continue
            levels[i+1].append(n.left)
            levels[i+1].append(n.right)
        if all(el is None for el in levels[i+1]):
            break
        i += 1
    res = []
    for j in range(len(levels)-1):
        for n in levels[j]:
            if n is None:
                continue
            res.append(n.value)

    return res
