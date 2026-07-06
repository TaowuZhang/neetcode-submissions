func isValid(s string) bool {
    // 1️⃣ 预检：如果长度是奇数，直接判定无效（剪枝优化）
    if len(s)%2 != 0 {
        return false
    }

    // 2️⃣ 建立映射表：右括号 -> 对应的左括号
    pairs := map[rune]rune{
        ')': '(',
        ']': '[',
        '}': '{',
    }

    // 3️⃣ 创建栈：使用 rune 切片来记录左括号
    stack := []rune{}

    // 4️⃣ 遍历字符串中的每一个字符
    for _, char := range s {
        // 检查当前字符是否在 pairs 的键（Key）中，如果是，说明它是右括号
        if openBracket, exists := pairs[char]; exists {
            // 遇到右括号时：如果此时栈为空，或者栈顶元素与期望的左括号不匹配，直接返回 false
            if len(stack) == 0 || stack[len(stack)-1] != openBracket {
                return false
            }
            // 匹配成功，执行出栈操作（移除切片的最后一个元素）
            stack = stack[:len(stack)-1]
        } else {
            // 如果不是右括号（即它是左括号），则执行入栈操作
            stack = append(stack, char)
        }
    }

    // 5️⃣ 终结检查：遍历结束后，如果栈完全清空，说明全部匹配成功，返回 true
    return len(stack) == 0
}