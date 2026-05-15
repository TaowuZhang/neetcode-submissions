class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        
        # 1. 先处理左右子树（自底向上）
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        # 2. 检查当前节点是否成为了新的 target 叶子节点
        if root.left is None and root.right is None and root.val == target:
            return None
            
        return root