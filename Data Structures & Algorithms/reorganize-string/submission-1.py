import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1. 统计频率
        counts = Counter(s)
        max_heap = [[-cnt, char] for char, cnt in counts.items()]
        heapq.heapify(max_heap)
        
        # 2. 校验可行性：最频繁字符的次数不能超过 (n + 1) // 2
        if -max_heap[0][0] > (len(s) + 1) // 2:
            return ""
        
        res = ""
        # 3. 贪心构造：每次取出两个频率最高的字符
        while len(max_heap) >= 2:
            cnt1, char1 = heapq.heappop(max_heap)
            cnt2, char2 = heapq.heappop(max_heap)
            
            res += char1
            res += char2
            
            # 如果还有剩余，变动频率后重新入堆
            if cnt1 + 1 < 0:
                heapq.heappush(max_heap, [cnt1 + 1, char1])
            if cnt2 + 1 < 0:
                heapq.heappush(max_heap, [cnt2 + 1, char2])
        
        # 4. 处理最后可能剩余的一个字符
        if max_heap:
            cnt, char = heapq.heappop(max_heap)
            res += char
            
        return res