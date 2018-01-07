class Node:
    def __init__(self,nazwa,priorytet):
        self.nazwa=nazwa
        self.priorytet=priorytet
        self.next=None
        self.prev=None


class Bidirectional:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def add(self,nazwa,priorytet): #TO JEST STANOWCZO ZA DŁUGIE!!! (ale za to ładnie rozpisane :) )
        new_node=Node(nazwa,priorytet)
        # print("adding",nazwa,priorytet)
        if not self.head:
            self.head=new_node
            self.tail=new_node
            self.size+=1
        else:
            n=self.head
            if not n.next:
                if new_node.priorytet>n.priorytet:
                    self.tail=n
                    n.prev=new_node
                    new_node.next=n
                    self.head=new_node
                    self.size+=1
                else:
                    n.next=new_node
                    self.tail=new_node
                    new_node.prev=n
                    self.size+=1
            else:
                # n=n.next
                while n:
                    # print("skipping",n.nazwa, n.priorytet)
                    if n.priorytet>new_node.priorytet and n.next:
                        n=n.next
                    else:
                        if self.tail!=n and self.head!=n:
                            prev=n.prev
                            n.prev=new_node
                            new_node.prev=prev
                            new_node.next=n
                            prev.next=new_node
                            self.size+=1
                            return

                        elif self.head==n:
                            if n.priorytet<new_node.priorytet:
                                n.prev=new_node
                                new_node.next = n
                                self.head=new_node
                                self.size+=1
                                return
                            else:
                                next=n.next
                                n.next=new_node
                                new_node.prev=n
                                next.prev=new_node
                                self.size+=1
                                return

                        elif self.tail==n:
                            if n.priorytet>new_node.priorytet:
                                n.next=new_node
                                new_node.prev=n
                                self.tail=new_node
                                self.size+=1
                                return
                            else:
                                prev=n.prev
                                n.prev=new_node
                                prev.next=new_node
                                new_node.next=n
                                self.size+=1
                                return
                        else:
                            print("MASAKRA")

    def delete(self,nazwa,priorytet):
        current=self.head
        current.prev=None

        while current is not None:
            current=current.next
            if current.nazwa==nazwa and current.priorytet==priorytet:
                if current.prev is not None:
                    current.prev.next=current.next
                    current.next.prev=current.prev
                    self.size-=1
                    return
                else:
                    self.head=current.next
                    current.next.prev=None
                    self.size-=1
                    return

    def print(self):
        n=self.head
        while n:
            print(n.nazwa, n.priorytet)
            n=n.next




ll=Bidirectional()
ll.add('zakupy',2)
ll.add('bieganie',4)
ll.add('spanie',100)
ll.add('obiad',7)
ll.add('pranie',1)
ll.delete('obiad',7)
ll.add('cos',3)
ll.print()