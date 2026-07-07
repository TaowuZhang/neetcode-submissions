func getConcatenation(nums []int) []int {
    n := len(nums)
    // 创建一个长度为 2n 的切片
    ans := make([]int, 2*n)
    
    for i := 0; i < n; i++ {
        ans[i] = nums[i]
        ans[i+n] = nums[i]
    }
    
    return ans
}