class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # 因为 to[i] <= 1000，初始化 1001 个站点的变动数组
        stations = [0] * 1001
        
        # 记录每个站点的净变动
        for num, start, end in trips:
            stations[start] += num
            stations[end] -= num
            
        # 从西向东累加，检查是否超载
        current_passengers = 0
        for num_change in stations:
            current_passengers += num_change
            if current_passengers > capacity:
                return False
                
        return True