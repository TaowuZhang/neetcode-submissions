func sortArray(nums []int) []int {
    n := len(nums)

    // Step 1: 构建最大堆
    // 从最后一个非叶子节点开始往上进行下沉（heapify）
    for i := n/2 - 1; i >= 0; i-- {
        siftDown(nums, i, n)
    }

    // Step 2: 逐个将堆顶元素（最大值）交换到末尾，并重新调整堆
    for i := n - 1; i > 0; i-- {
        nums[0], nums[i] = nums[i], nums[0] // 交换
        siftDown(nums, 0, i)                // 重新调整堆，此时堆的大小减小为 i
    }

    return nums
}

// siftDown 维护最大堆性质
func siftDown(nums []int, root, n int) {
    for {
        leftChild := 2*root + 1
        rightChild := 2*root + 2
        largest := root

        // 比较左孩子
        if leftChild < n && nums[leftChild] > nums[largest] {
            largest = leftChild
        }
        // 比较右孩子
        if rightChild < n && nums[rightChild] > nums[largest] {
            largest = rightChild
        }

        // 如果最大值不是当前根节点，则交换并继续向下调整
        if largest != root {
            nums[root], nums[largest] = nums[largest], nums[root]
            root = largest // 迭代继续向下 siftDown
        } else {
            break
        }
    }
}