class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next=self.next
        else:
            temp = self.head
            while temp.next is not self.next:
                temp = temp.next
            temp.next = new_node# appending new node
            new_node.next=self.next       
    def insert(self,new_node,pos):
        if pos==1:#1 insert node at first position
            temp=self.head
            while(temp.next!=self.head): #last node
                temp=temp.next
            new_node.next=self.head
            self.head=new_node
            temp.next=self.head
        else:#insert node from 2nd to last position
            p=1
            temp=self.head
            while(p!=pos-1):
                temp=temp.next
                p+=1
                new_node.next=temp.next
                temp.next=new_node
    def delete(self,value):
        temp=self.head
        prev=None
        if temp.data==value:#first node to delete
            while(temp.next!=self.head):#last node
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
        else:
            while(temp.data!=value and temp):
                prev=temp
                temp=temp.next
                if temp==self.head:
                    print("Value not found")
                    return
            prev.next=temp.next
            temp=None
    def print(self):
        print()
        print("List elements:")
        temp=self.head
        while(True):
            print(temp.data,end=" ")
            temp=temp.next
            if temp ==self.head:
                break
list1=LinkedList()
n1=Node(10)
n1=Node(20)
n1=Node(30)
n1=Node(40)
    # def insert(self,new_node,pos):
    #     if pos==1:#1 insert node at first position
    #         new node.next =self.head