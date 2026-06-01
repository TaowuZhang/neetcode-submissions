class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # 建立字符到优先级的映射
        order_map = {char: i for i, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            
            # 逐字符比较
            for j in range(len(w1)):
                # 如果 w2 比 w1 短，且 w1 前缀已经和 w2 匹配，说明顺序错误
                # 此时 w2 已经没有字符可以比较了
                if j == len(w2):
                    return False
                
                # 如果发现字符顺序不符
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    # 当前字符已经满足顺序，不再需要比较后面字符
                    break
            else:
                # 只有当 w1 是 w2 的前缀且 w1 比 w2 长时会漏检，
                # 但由于上面的逻辑，如果 w1 遍历完还没触发 return 或 break，
                # 说明 w1 是 w2 的前缀且 w1 长度 <= w2，即顺序合法。
                continue
                
        return True