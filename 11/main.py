#!/usr/bin/env python3
import fileinput

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if (root is None or p is None or q is None):
        return None

    ancestor = root

    while True :
        if (p.val < ancestor.val and q.val < ancestor.val):
            ancestor = ancestor.left
        elif (p.val > ancestor.val and q.val > ancestor.val):
            ancestor = ancestor.right
        else:
            return ancestor


for line in fileinput.input():
    root = TreeNode(30, TreeNode(8, TreeNode(3), TreeNode(20, TreeNode(10), TreeNode(29))), TreeNode(52))
    a, b = line.split()
    a, b = TreeNode(int(a)), TreeNode(int(b))
    print(lowestCommonAncestor(root, a, b).val)
