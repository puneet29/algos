import sys

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(root: TreeNode, lower: int = -sys.maxsize, upper: int = sys.maxsize) -> bool:
            if(root is None):
                return True
            if(root.val > lower and root.val < upper):
                if(root.left is None and root.right is None):
                    return True
                if(root.right is None):
                    return root.left.val < root.val and helper(root.left, lower, root.val)
                if(root.left is None):
                    return root.right.val > root.val and helper(root.right, root.val, upper)
                if(root.val > root.left.val and root.val < root.right.val):
                    return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)
            return False

        return helper(root)
