# Reversing a stack using queue
class Node:
    def __init__(self, value):
        self.data = value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            poped_data=temp.data
            self.top=self.top.next
            top=None
            return poped_data

        
    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack contains...")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
# WAF to reverse the stack
    def reverse(self):
        temp=self.top
        while temp:
            st1.push(Node(temp.data))
            temp=temp.next
# WAF for comparing two stack
    def compare(self, other):
        temp1=self.top
        temp2=other.top

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False
            temp1=temp1.next
            temp2=temp2.next
        return temp1 is None and temp2 is None

class LQueue:
    def __init__(self):
        self.front=self.rear=None
    
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        temp=self.front
        print("deleted node:", temp.data)
        self.front=self.front.next
        if self.front==None:
            print("Queue is now empty")
            self.rear=None
        temp=None

    def print(self):
        temp=self.front
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print()

def reverse_stack(s1):
    q1=LQueue()
    while not s1.isempty(): 
        q1.enqueue(Node(s1.pop()))
    q1.print()


st=stack()
st1=stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.print()

reverse_stack(st)