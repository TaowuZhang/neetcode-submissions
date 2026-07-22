type NumMatrix struct {
    sums [][]int
}

func Constructor(matrix [][]int) NumMatrix {
    m := len(matrix)
    if m == 0 {
        return NumMatrix{}
    }
    n := len(matrix[0])
    
    // 初始化 (m+1) x (n+1) 的切片，避开复杂的边界条件判断
    sums := make([][]int, m+1)
    for i := range sums {
        sums[i] = make([]int, n+1)
    }
    
    // 预计算二维前缀和
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            sums[i+1][j+1] = sums[i][j+1] + sums[i+1][j] - sums[i][j] + matrix[i][j]
        }
    }
    
    return NumMatrix{sums: sums}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    // 容斥原理，O(1) 算出矩形和
    return this.sums[row2+1][col2+1] - this.sums[row1][col2+1] - this.sums[row2+1][col1] + this.sums[row1][col1]
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */