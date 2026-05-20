import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(max_heap, (-count, char))
        
        res = []
        
        while max_heap:
            count1, char1 = heapq.heappop(max_heap)
            count1 = -count1
            
            # 检查是否会连续出现 3 个相同字符
            if len(res) >= 2 and res[-1] == char1 and res[-2] == char1:
                if not max_heap:
                    # 没有其他字符可选了，只能结束
                    break
                
                # 取出数量第二多的字符
                count2, char2 = heapq.heappop(max_heap)
                count2 = -count2
                
                # 放入一个次多字符
                res.append(char2)
                count2 -= 1
                
                if count2 > 0:
                    heapq.heappush(max_heap, (-count2, char2))
                
                # 把第一多的字符放回堆中，留到下一轮
                heapq.heappush(max_heap, (-count1, char1))
            else:
                # 不会触发连续 3 个，直接放最多的字符
                # 策略优化：如果剩余很多，可以一次放2个，加速消耗；但如果它只是领先次多字符不多，放1个或2个都行。
                # 这里为了简单，每次放1个，由于外层是循环，它会连续放直到触发上面的限制。
                res.append(char1)
                count1 -= 1
                
                if count1 > 0:
                    heapq.heappush(max_heap, (-count1, char1))
                    
        return "".join(res)