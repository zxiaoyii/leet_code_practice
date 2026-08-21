class ListNode:

    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None 
        self.next = None
    
class LRUCache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # key -> node
        self.start = ListNode()# least used
        self.end = ListNode() # most frequent used
        self.start.next = self.end
        self.end.prev = self.start
    
    def get(self, key) -> int:
        #if key exists
        if key in self.cache:
            node = self.cache[key]
            # put this node to the most frequent used
            # delete node from list
            self.delete(node) 
            # add node to most frequent
            self.addToFrequent(node) 
            return node.value
        else:
            return -1

    def put(self, key, value) -> None:
        #if key exists
        if key in self.cache:
            #update value
            node = self.cache[key]
            node.value = value
            # delete node from list
            self.delete(node) 
            # add node to most frequent
            self.addToFrequent(node) 
        else:
            #if exceeds capacity
            if len(self.cache) >= self.capacity:
                #delete LRU key
                temp = self.start.next
                self.delete(temp) 
                del self.cache[temp.key]
            # add new node to most recent
            node = ListNode(key, value)
            self.addToFrequent(node) 
            self.cache[key] = node

    def delete(self, node):
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p
        node.next = None
        node.prev = None
    
    def addToFrequent(self, node):
        p = self.end.prev
        p.next = node
        node.prev = p
        node.next = self.end
        self.end.prev = node
    

        
