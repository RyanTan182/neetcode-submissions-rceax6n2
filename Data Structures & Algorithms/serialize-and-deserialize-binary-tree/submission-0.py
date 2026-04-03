# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        final_str = []
        def dfs(node):
            if not node:
                final_str.append("N")
                return
            
            final_str.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(final_str)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        nodes = iter(data.split(","))

        def helper():
            val = next(nodes)
            if val == "N":
                return None
            
            root = TreeNode(int(val))
            root.left = helper()
            root.right = helper()

            return root
        return helper()
