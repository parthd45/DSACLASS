#Priority Queue Implementation using Linked List
class Node:
    def __init__(self,value,pr):
        self.data=value
        self.priority=pr
        self.next=None

class PriorityQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.front is None:
            self.front=self.rear=new_node

        elif self.front.priority > new_node.priority:
            new_node.next=self.front
            self.front=new_node

        else:
            temp=self.front
            while temp.next:
                if new_node.priority < temp.next.priority:
                    break
                temp=temp.next

            new_node.next=temp.next
            temp.next=new_node

            if new_node.next is None:
                self.rear=new_node

    def display(self):
        if self.front is None:
            print()
        else:
            temp=self.front
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
            print()


pq=PriorityQueue()

pq.enqueue(Node(10,3))
pq.enqueue(Node(20,1))
pq.enqueue(Node(30,2))
pq.enqueue(Node(40,4))

pq.display()