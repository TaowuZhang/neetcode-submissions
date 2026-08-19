func getConcatenation(nums []int) []int {
    // 方式 1：使用 append 切片解包（ Go 语言最 idiomatic 的写法）
    return append(nums, nums...)

    // 方式 2：预分配内存后复制（适合对内存分配性能要求极高的场景）
    /*
    n := len(nums)
    ans := make([]int, 2*n)
    copy(ans[:n], nums)
    copy(ans[n:], nums)
    return ans
    */
}