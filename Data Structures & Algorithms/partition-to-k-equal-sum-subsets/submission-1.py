from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k
        nums.sort(reverse=True)
        
        # 记忆化搜索：记录 mask 状态是否可行
        memo = {}

        def backtrack(mask, current_sum, count):
            # 找到 k-1 个子集后，剩下的数字必然构成第 k 个子集
            if count == k - 1: return True
            if mask in memo: return memo[mask]
            
            if current_sum == target:
                # 开启下一个子集的搜索
                res = backtrack(mask, 0, count + 1)
                memo[mask] = res
                return res
            
            for i in range(len(nums)):
                # 检查该数字是否已用过
                if not (mask & (1 << i)):
                    if current_sum + nums[i] <= target:
                        # 递归尝试
                        if backtrack(mask | (1 << i), current_sum + nums[i], count):
                            memo[mask] = True
                            return True
                    else:
                        # 剪枝：因为 nums 已从大到小排序，若当前数太大，后续更小的数也可能凑出，但需跳过
                        continue
            
            memo[mask] = False
            return False

        return backtrack(0, 0, 0)