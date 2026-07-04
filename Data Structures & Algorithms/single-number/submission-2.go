func singleNumber(nums []int) int {
    // 1. 初始化一个变量 result，存结果。初始值设为 0。
    // := 是 Go 的短变量声明符，等于：var result int = 0
    result := 0 
    
    // 2. 这是一个迭代器，用于遍历数组 nums
    // range nums 会返回两个值：第一个是索引(index)，第二个是对应的值(value)
    // 因为这里我们不需要用到索引，所以用下划线 _ 把它“扔掉”（Go 要求定义的变量必须被使用，否则会报错）
    // num 就是当前遍历到的那个数字
    for _, num := range nums {
        
        // 3. ^= 是异或赋值运算符
        // 这行代码等同于：result = result ^ num
        // 它把当前的 result 和遍历到的数字进行异或，结果再存回 result
        result ^= num
    }
    
    // 4. 循环结束后，result 里存的就是那个落单的数字
    return result
}