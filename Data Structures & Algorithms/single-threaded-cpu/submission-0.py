import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # 1. 附带索引并排序
        extended_tasks = []
        for i, (eq, pr) in enumerate(tasks):
            extended_tasks.append((eq, pr, i))
        extended_tasks.sort(key=lambda x: x[0])
        
        res = []
        min_heap = []
        curr_time = 0
        i = 0
        n = len(tasks)
        
        # 2. 模拟推进
        while i < n or min_heap:
            # 状态 A: 堆为空且当前时间落后于下一个任务的到达时间
            if not min_heap and curr_time < extended_tasks[i][0]:
                curr_time = extended_tasks[i][0]
            
            # 状态 B: 将所有到达时间 <= curr_time 的任务入堆
            while i < n and extended_tasks[i][0] <= curr_time:
                # 堆内排序依据: (processing_time, original_index)
                heapq.heappush(min_heap, (extended_tasks[i][1], extended_tasks[i][2]))
                i += 1
            
            # 状态 C: 从堆中消费一个任务
            proc_time, index = heapq.heappop(min_heap)
            curr_time += proc_time
            res.append(index)
            
        return res