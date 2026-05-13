class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0] # [偷, 不偷]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 1. 偷当前节点：子节点必须是不偷状态
            rob_val = node.val + left[1] + right[1]
            
            # 2. 不偷当前节点：子节点可偷可不偷，取大者
            not_rob_val = max(left) + max(right)
            
            return [rob_val, not_rob_val]
        
        return max(dfs(root))