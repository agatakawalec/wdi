class Node:
    def __init__(self, da):
        self.data = da
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class BidirectionalList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addtail(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            m = self.tail
            new_node = Node(data)
            m.next = new_node
            new_node.prev = m
            self.tail = new_node
            self.size += 1

    def addhead(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            m = self.head
            new_node = Node(data)
            m.prev = new_node
            new_node.next = m
            self.head = new_node
            self.size += 1

    def insert(self, data, index):
        if not self.head:
            n = Node(data)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            n=self.head
            i=0
            while n and i !=index:
                i+=1
                n=n.next
            nextNode=n.next
            prevNode=n

            newNode = Node(data)
            newNode.prev = prevNode
            newNode.next = nextNode
            prevNode.next = newNode
            nextNode.prev = newNode
            self.size += 1

    def removetail(self,data):
        if not self.head:
            n = Node(data)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            n=self.tail
            n.prev=m #m= NewNode
            m=self.tail
            m.next=None
            self.size-=1

    def removehead(self,data):
        if not self.head:
            n = Node(data)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            n=self.head
            n.next=m
            m=self.tail
            m.prev=None
            self.size-=1

    def printList(self):
        n= self.head
        while n:
            print(n)
            n = n.next

    def printListT(self):
        n=self.tail
        while n:
            print(n)
            n=n.prev

    def findBest(selfself):
        if not self.head:
            n = Node(data)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            n=self.head
            i=n
            while n:
                if(n.data>i.data)
                    i=n
            n=n.next

ll = BidirectionalList()
ll.add(14)
ll.add("test")
ll.add(2.34)
ll.add(True)
ll.printList()