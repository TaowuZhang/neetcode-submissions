type ListNode struct {
    Key  int
    Next *ListNode
}

type MyHashSet struct {
    size    int
    buckets []*ListNode
}

func Constructor() MyHashSet {
    size := 10007
    buckets := make([]*ListNode, size)
    for i := 0; i < size; i++ {
        buckets[i] = &ListNode{Key: 0}
    }
    return MyHashSet{
        size:    size,
        buckets: buckets,
    }
}

func (this *MyHashSet) getHash(key int) int {
    return key % this.size
}

func (this *MyHashSet) Add(key int) {
    idx := this.getHash(key)
    curr := this.buckets[idx]
    for curr.Next != nil {
        if curr.Next.Key == key {
            return
        }
        curr = curr.Next
    }
    curr.Next = &ListNode{Key: key}
}

func (this *MyHashSet) Remove(key int) {
    idx := this.getHash(key)
    curr := this.buckets[idx]
    for curr.Next != nil {
        if curr.Next.Key == key {
            curr.Next = curr.Next.Next
            return
        }
        curr = curr.Next
    }
}

func (this *MyHashSet) Contains(key int) bool {
    idx := this.getHash(key)
    curr := this.buckets[idx].Next
    for curr != nil {
        if curr.Key == key {
            return true
        }
        curr = curr.Next
    }
    return false
}