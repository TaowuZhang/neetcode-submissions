class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        curr_max, max_sum = 0, float('-inf')
        curr_min, min_sum = 0, float('inf')
        total_sum = 0
        
        for x in nums:
            total_sum += x
            
            # 标准 Kadane 求最大值
            curr_max = max(x, curr_max + x)
            max_sum = max(max_sum, curr_max)
            
            # 变体 Kadane 求最小值
            curr_min = min(x, curr_min + x)
            min_sum = min(min_sum, curr_min)
            
        # 如果 max_sum < 0，说明数组全为负数，直接返回 max_sum
        if max_sum < 0:
            return max_sum
            
        return max(max_sum, total_sum - min_sum)