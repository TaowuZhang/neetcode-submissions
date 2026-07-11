func longestCommonPrefix(strs []string) string {
    if len(strs) == 0 {
        return ""
    }

    // 将第一个字符串作为初始前缀
    prefix := strs[0]

    // 遍历数组中的其余字符串
    for i := 1; i < len(strs); i++ {
        // 当 strs[i] 不以 prefix 开头时，缩短 prefix
        for len(strs[i]) < len(prefix) || strs[i][:len(prefix)] != prefix {
            prefix = prefix[:len(prefix)-1]
            if prefix == "" {
                return ""
            }
        }
    }

    return prefix
}