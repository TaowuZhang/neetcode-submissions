import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        # 存储可用房间编号的堆
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        # 存储正在占用房间的堆: (end_time, room_id)
        # 堆会自动先比较 end_time，若相同则比较 room_id
        occupied_rooms = []
        # 记录每个房间会议次数
        count = [0] * n
        
        for start, end in meetings:
            # 1. 释放已结束的会议
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room_id = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room_id)
            
            # 2. 分配房间
            if available_rooms:
                room_id = heapq.heappop(available_rooms)
                heapq.heappush(occupied_rooms, (end, room_id))
            else:
                # 没有空闲房间，必须等待最早结束的会议
                room_end, room_id = heapq.heappop(occupied_rooms)
                # 计算延期后的结束时间
                new_end = room_end + (end - start)
                heapq.heappush(occupied_rooms, (new_end, room_id))
                
            count[room_id] += 1
            
        # 返回会议次数最多的房间号，次数相同时取最小值
        # max 的 key 设置为 (次数, -房间号)，这样可以在次数相同时通过最大化房间号的负值找到最小房间号
        # 或者直接遍历查找也可以
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i