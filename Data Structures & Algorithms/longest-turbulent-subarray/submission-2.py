class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        if not arr: 
            return 0
        n = len(arr)
        if n == 1: 
            return 1
        
        max_len = 1
        left = 0
        
        for right in range(1, n):
            # 获取当前比较结果：1 (>) , -1 (<), 0 (=)
            c = (arr[right-1] > arr[right]) - (arr[right-1] < arr[right])
            
            if c == 0:
                left = right
            elif right == n - 1 or c * ((arr[right] > arr[right+1]) - (arr[right] < arr[right+1])) != -1:
                max_len = max(max_len, right - left + 1)
                left = right
                
        return max_len