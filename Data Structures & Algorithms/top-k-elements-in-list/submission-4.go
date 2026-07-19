func topKFrequent(nums []int, k int) []int {
    // Step 1: 统计频次
    count := make(map[int]int)
    for _, num := range nums {
        count[num]++
    }

    // Step 2: 桶排序
    buckets := make([][]int, len(nums)+1)
    for num, freq := range count {
        buckets[freq] = append(buckets[freq], num)
    }

    // Step 3: 收集结果
    res := make([]int, 0, k)
    for i := len(buckets) - 1; i > 0; i-- {
        for _, num := range buckets[i] {
            res = append(res, num)
            if len(res) == k {
                return res
            }
        }
    }
    return res
}