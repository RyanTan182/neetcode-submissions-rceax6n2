# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_height = 0
        def recursiveDiameter(node):
            nonlocal max_height

            if node is None:
                return 0
            right = recursiveDiameter(node.right)
            left = recursiveDiameter(node.left)
            max_height = max(max_height, left + right)
        
            return 1 + max(left, right)
        recursiveDiameter(root)
        return max_height
        