func removeElement(nums []int, val int) int {
    k := 0 // 慢指针，记录有效元素的写入位置
    
    for i := 0; i < len(nums); i++ { // 快指针遍历数组
        if nums[i] != val {
            nums[k] = nums[i] // 覆盖有效元素
            k++
        }
    }
    
    return k
}