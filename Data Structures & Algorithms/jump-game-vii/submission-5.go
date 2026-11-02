func canReach(s string, minJump int, maxJump int) bool {
    n := len(s)
    // 如果最后一个字符是 '1'，永远无法到达
    if s[n-1] == '1' {
        return false
    }

    dp := make([]bool, n)
    dp[0] = true

    count := 0
    for j := 0; j < n; j++ {
        // 1. 维护滑动窗口右边界加入
        if j >= minJump {
            if dp[j-minJump] {
                count++
            }
        }
        // 2. 维护滑动窗口左边界移出
        if j > maxJump {
            if dp[j-maxJump-1] {
                count--
            }
        }

        // 3. 计算当前 dp[j]
        if j == 0 {
            dp[0] = true
        } else if s[j] == '0' && count > 0 {
            dp[j] = true
        } else {
            dp[j] = false
        }
    }

    return dp[n-1]
}