# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        newRoot = root
        newRoot.right, newRoot.left = newRoot.left, newRoot.right
        self.invertTree(newRoot.left)
        self.invertTree(newRoot.right)
        return newRoot
