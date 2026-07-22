func productExceptSelf(nums []int) []int {
    n := len(nums)
    res := make([]int, n)

    // 第一遍遍历（从左往右）：计算每个位置左边所有数的乘积（前缀积）
    res[0] = 1
    for i := 1; i < n; i++ {
        res[i] = res[i-1] * nums[i-1]
    }

    // 第二遍遍历（从右往左）：将前缀积乘以右边所有数的乘积（后缀积）
    postfix := 1
    for i := n - 1; i >= 0; i-- {
        res[i] *= postfix
        postfix *= nums[i]
    }

    return res
}