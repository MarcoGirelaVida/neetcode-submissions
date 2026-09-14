class ListNode:
    def __init__(self, val: int, next, prev):
        self.val = val
        self.next_node = next
        self.prev_node = prev

class LinkedList:
   
    def __init__(self):
        self.starter_node = None
        self.last_node = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if self.size // 2 > index:
            node = self.starter_node
            for _ in range(index):
                node = node.next_node
        else:
            node = self.last_node
            for _ in range(self.size - 1 - index):
                node = node.prev_node
        return node.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.starter_node, None)
        if self.starter_node is not None:
            self.starter_node.prev_node = new_node
        else:
            self.last_node = new_node
        self.starter_node = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val, None, self.last_node)
        if self.last_node is not None:
            self.last_node.next_node = new_node
        else:
            self.starter_node = new_node
        self.last_node = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        node = self.starter_node
        if self.size // 2 >= index:
            for _ in range(index):
                node = node.next_node
        else:
            node = self.last_node
            for _ in range(self.size - 1 - index):
                node = node.prev_node
        
        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            self.starter_node = node.next_node
            
        if node.next_node:
            node.next_node.prev_node = node.prev_node
        else:
            self.last_node = node.prev_node
            
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values_array = []
        node = self.starter_node
        for i in range(self.size):
            values_array.append(node.val)
            node = node.next_node
        return values_array