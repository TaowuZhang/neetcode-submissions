func singleNumber(nums []int) int {
    result := 0
    for _, num := range nums {
        // 对每个元素进行异或运算
        result ^= num
    }
    return result
}