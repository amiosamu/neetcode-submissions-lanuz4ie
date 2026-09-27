type Node struct {
    key int
    value int
    next *Node
    prev *Node
}

type LRUCache struct {
    capacity int
    data map[int]*Node
    head *Node
    tail *Node
}

func Constructor(capacity int) LRUCache {
    data := make(map[int]*Node, capacity)
    head := &Node{}
    tail := &Node{}
    head.next = tail
    tail.prev = head

    return LRUCache{
        capacity: capacity,
        data: data,
        head: head,
        tail: tail,
    }
}

func (this *LRUCache) remove(node *Node) {
    node.prev.next = node.next
    node.next.prev = node.prev
}

func (this* LRUCache) addToHead(node *Node) {
    node.next = this.head.next
    node.prev = this.head
    this.head.next.prev = node
    this.head.next = node
}
func (this *LRUCache) Get(key int) int {
    node, ok := this.data[key]
    if !ok {
        return -1
    }
    this.remove(node)
    this.addToHead(node)
    return node.value
}

func (this *LRUCache) Put(key int, value int) {
    node, ok := this.data[key]
    if ok {
        this.remove(node)
        this.addToHead(node)
        node.value = value
        return
    }
    if len(this.data) >= this.capacity {
        node := this.tail.prev
        this.remove(node)
        delete(this.data, node.key)
    }
    node = &Node{
        key: key,
        value: value,
    }
    this.addToHead(node)
    this.data[key] = node
    return
}
