#Stack Imlementation using lINKED list
class Node :
    def __init__(self,val):
        self.data=val
        self.next=None
        
class stack:
    def __init__(self):
        self.top=None
    def __isempty(self):
        return self.top is None
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.__isempty():
            print("Stack is empty")
        else:
            temp=self.top
            print("Popped element:", temp.data)
            self.top=self.top.next
            temp=None
    def print(self):
        if self.__isempty():
            print("Stack is empty")
        else:    
            print("Stack elements:")
            temp=self.top
            while(temp):
                print(temp.data)
                temp=temp.next
st=stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.print()
st.pop()
st.print()