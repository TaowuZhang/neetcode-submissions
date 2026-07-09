func isAnagram(s string, t string) bool {
    // 长度不等直接返回 false
    if len(s) != len(t) {
        return false
    }

    // 使用长度为 26 的数组作为哈希表（针对小写英文字母）
    // 空间复杂度 O(1)
    var count [26]int

    for i := 0; i < len(s); i++ {
        count[s[i]-'a']++
        count[t[i]-'a']--
    }

    // 检查数组中是否所有计数都为 0
    for _, val := range count {
        if val != 0 {
            return false
        }
    }

    return true
}