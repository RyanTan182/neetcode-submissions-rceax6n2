class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final_list = []
        if not root:
            return final_list
        q = deque()
        
        q.append(root)

        while len(q) > 0:
            level_size = len(q)
            new_list = []
            for _ in range(level_size):
                node = q.popleft()
                new_list.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            final_list.append(new_list)

            
        return final_list