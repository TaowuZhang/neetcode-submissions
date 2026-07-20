type Solution struct{}

// Encode 将字符串列表编码为一个单独的字符串
func (s *Solution) Encode(strs []string) string {
    var builder strings.Builder
    for _, str := range strs {
        // 写入长度 + # + 字符串主体
        builder.WriteString(strconv.Itoa(len(str)))
        builder.WriteByte('#')
        builder.WriteString(str)
    }
    return builder.String()
}

// Decode 将编码后的字符串解码回列表
func (s *Solution) Decode(encoded_string string) []string {
    var res []string
    i := 0
    
    for i < len(encoded_string) {
        // 1. 寻找长度分隔符 '#' 的位置
        j := i
        for encoded_string[j] != '#' {
            j++
        }
        
        // 2. 解析长度 N
        length, _ := strconv.Atoi(encoded_string[i:j])
        
        // 3. 截取长度为 N 的完整子串
        i = j + 1 // 跳过 '#'
        res = append(res, encoded_string[i:i+length])
        
        // 4. 移动指针到下一个编码块起点
        i += length
    }
    
    return res
}