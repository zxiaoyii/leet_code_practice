class ListNode:
    def __init__(self, key = 0, val = 0):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> nodes
        self.start = ListNode() # LRU
        self.end = ListNode()
        self.start.next = self.end
        self.end.prev = self.start

    def get(self, key: int) -> int:
        # get the node through cache if key exist
        if key in self.cache:
            node = self.cache[key]
            #delete the node
            self.deleteNodeFromLinkedList(node)
            #add it back to most frequent
            self.addNodeToMostFrequent(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key exist or not
        if key in self.cache:
            # update the value of key
            # get the node form cache
            node = self.cache[key]
            # delete
            self.deleteNodeFromLinkedList(node)
            # update it 
            node.val = value
            # move to most frequent
            self.addNodeToMostFrequent(node)
        else:
            # add the k-v pare
            # exceed capacity?
            if self.capacity == len(self.cache):
                #delete LRU
                temp = self.start.next
                self.deleteNodeFromLinkedList(temp)
                del self.cache[temp.key]

            # add to cache
            node = ListNode(key, value)
            self.cache[key] = node
            # add to linkedList(most frequent)
            self.addNodeToMostFrequent(node)

    
    def deleteNodeFromLinkedList(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        node.next = None
        node.prev = None

    def addNodeToMostFrequent(self, node):
        p = self.end.prev
        p.next = node
        node.next = self.end
        node.prev = p
        self.end.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)