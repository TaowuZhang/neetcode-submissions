type Node struct {
    Key, Val int
    Next     *Node
}

type MyHashMap struct {
    buckets []*Node
    size    int
}

func Constructor() MyHashMap {
    // 10007 是一个质数，能有效减少哈希冲突
    size := 10007 
    return MyHashMap{
        buckets: make([]*Node, size),
        size:    size,
    }
}

func (this *MyHashMap) hash(key int) int {
    return key % this.size
}

func (this *MyHashMap) Put(key int, value int) {
    idx := this.hash(key)
    curr := this.buckets[idx]
    
    // 情况1：桶为空，直接插入头节点
    if curr == nil {
        this.buckets[idx] = &Node{Key: key, Val: value}
        return
    }
    
    // 情况2：遍历链表
    for {
        if curr.Key == key {
            curr.Val = value // key已存在，更新value
            return
        }
        if curr.Next == nil {
            break
        }
        curr = curr.Next
    }
    
    // 尾插法（也可以选择头插法）
    curr.Next = &Node{Key: key, Val: value}
}

func (this *MyHashMap) Get(key int) int {
    idx := this.hash(key)
    curr := this.buckets[idx]
    
    for curr != nil {
        if curr.Key == key {
            return curr.Val
        }
        curr = curr.Next
    }
    return -1
}

func (this *MyHashMap) Remove(key int) {
    idx := this.hash(key)
    curr := this.buckets[idx]
    
    if curr == nil {
        return
    }
    
    // 特殊处理头节点
    if curr.Key == key {
        this.buckets[idx] = curr.Next
        return
    }
    
    // 遍历删除后续节点
    for curr.Next != nil {
        if curr.Next.Key == key {
            curr.Next = curr.Next.Next
            return
        }
        curr = curr.Next
    }
}