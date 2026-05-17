class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
            
        target = total // 4
        
        # 策略 A：降序排序，优先处理长火柴
        matchsticks.sort(reverse=True)
        
        # 前置校验：最大元素不可超过边长
        if matchsticks[0] > target:
            return False
            
        # 4 个桶，记录每条边当前的长度
        edges = [0] * 4
        
        def dfs(index: int) -> bool:
            # 边界条件：所有火柴都已成功分配
            if index == len(matchsticks):
                return True
                
            match = matchsticks[index]
            
            for i in range(4):
                # 如果放入当前边会超出目标长度，直接剪枝
                if edges[i] + match > target:
                    continue
                    
                # 策略 B：等效去重（非常关键的剪枝）
                if i > 0 and edges[i] == edges[i - 1]:
                    continue
                    
                # 做出选择
                edges[i] += match
                
                # 递归进入下一层
                if dfs(index + 1):
                    return True
                    
                # 撤销选择（回溯）
                edges[i] -= match
                
            return False
            
        return dfs(0)