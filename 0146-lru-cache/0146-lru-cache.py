class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # {key: ListNode}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        
        if key not in self.hashmap:
            return -1
            
        node = self.hashmap[key]
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.add(node)
            
        else:
            new = ListNode(key=key, val=value)
            self.hashmap[key] = new
            self.add(new)
            
            if len(self.hashmap) > self.capacity:
                drop = self.head.next
                self.remove(drop) 
                del self.hashmap[drop.key]
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add(self, node):
        temp = self.tail.prev
        temp.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = temp
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)