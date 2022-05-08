'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_univals(root, count):
    count, tmp = helper(root)
    return count

def helper(root):
    if root is None:
        return 0, True
    left_count, left_is_unival = helper(root.left)
    right_count, right_is_unival = helper(root.right)
    count = left_count + right_count
    if left_is_unival and right_is_unival:
        if root.left and root.left.val != root.val:
            return count, False
        if root.right and root.right.val != root.val:
            return count, False
        return count + 1, True
    return count, False