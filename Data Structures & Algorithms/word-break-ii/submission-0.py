class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]
            
            if start in memo:
                return memo[start]
            
            res = []
            # 尝试所有可能的子串
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # 递归获取后续的拼接结果
                    sub_sentences = dfs(end)
                    for sub in sub_sentences:
                        # 如果 sub 是空字符串，说明到达了末尾
                        if sub == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sub)
            
            memo[start] = res
            return res

        return dfs(0)