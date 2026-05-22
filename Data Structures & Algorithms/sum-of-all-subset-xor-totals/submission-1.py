class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        # 计算所有元素的按位或 (OR)
        or_sum = 0
        for num in nums:
            or_sum |= num
        
        # 结果为 or_sum * 2^(n-1)
        # 即使 nums 为空（题目约束 n>=1），公式依然成立
        return or_sum * (1 << (len(nums) - 1))