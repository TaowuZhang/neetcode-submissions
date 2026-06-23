import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 检查是否存在公共因子
        if str1 + str2 != str2 + str1:
            return ""
        
        # 计算长度的最大公约数
        max_len = math.gcd(len(str1), len(str2))
        
        # 返回该长度的前缀
        return str1[:max_len]