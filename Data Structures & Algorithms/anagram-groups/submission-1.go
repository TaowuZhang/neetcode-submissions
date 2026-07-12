func groupAnagrams(strs []string) [][]string {
    // 创建一个 map，key 是长度为 26 的数组，value 是字符串切片
    m := make(map[[26]byte][]string)
    
    for _, s := range strs {
        var count [26]byte
        for i := 0; i < len(s); i++ {
            count[s[i]-'a']++
        }
        m[count] = append(m[count], s)
    }
    
    // 将 map 中的值转换为结果切片
    res := make([][]string, 0, len(m))
    for _, group := range m {
        res = append(res, group)
    }
    
    return res
}