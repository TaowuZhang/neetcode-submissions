func sortColors(nums []int) {
    left, i := 0, 0
    right := len(nums) - 1

    for i <= right {
        if nums[i] == 0 {
            // 遇到 0，交换到左侧
            nums[left], nums[i] = nums[i], nums[left]
            left++
            i++
        } else if nums[i] == 2 {
            // 遇到 2，交换到右侧
            nums[right], nums[i] = nums[i], nums[right]
            right--
            // 注意：此时 i 不增加，因为交换过来的数需要再次判断
        } else {
            // 遇到 1，直接跳过
            i++
        }
    }
}