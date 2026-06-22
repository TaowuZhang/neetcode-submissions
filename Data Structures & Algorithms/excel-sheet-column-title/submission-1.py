class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            # 将 1-26 映射到 0-25
            columnNumber -= 1
            # 计算当前位字符
            char = chr(ord('A') + (columnNumber % 26))
            result.append(char)
            # 向高位进位
            columnNumber //= 26
        
        # 结果是逆序的，需要反转
        return "".join(reversed(result))