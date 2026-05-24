class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def backtrack(start, path):
            # 终止条件：找到一个组合
            if len(path) == k:
                res.append(path[:])
                return
            
            # 剪枝逻辑
            # range 的终点：n - (剩余需要的个数 - 1)
            # 即：n - (k - len(path)) + 1
            # 这里 +2 是因为 range 是左闭右开，所以要比上限多 1
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop() # 回溯
        
        backtrack(1, [])
        return res