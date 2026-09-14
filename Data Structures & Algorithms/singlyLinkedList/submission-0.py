class LinkedList:
    
    def __init__(self):
        self.llist = []
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.llist[index]

    def insertHead(self, val: int) -> None:
        self.llist = [val] + self.llist
        self.size += 1

    def insertTail(self, val: int) -> None:
        self.llist += [val]
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        new_list = []
        for i in range(self.size):
            if i == index:
                continue
            new_list.append(self.llist[i])
        self.llist = new_list
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        return self.llist