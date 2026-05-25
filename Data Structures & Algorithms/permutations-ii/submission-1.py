class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                # 核心剪枝逻辑保持不变
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
                
        backtrack([])
        return res