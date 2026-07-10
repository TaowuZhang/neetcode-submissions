func twoSum(nums []int, target int) []int {
    // 创建一个哈希表来存储值到索引的映射
    // key: 数值, value: 索引
    prevMap := make(map[int]int)

    for i, num := range nums {
        diff := target - num
        
        // 检查差值是否已经在哈希表中
        if idx, ok := prevMap[diff]; ok {
            // 找到配对，返回结果
            return []int{idx, i}
        }
        
        // 将当前数值和索引存入哈希表
        prevMap[num] = i
    }
    
    return nil
}