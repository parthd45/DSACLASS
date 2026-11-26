#BST delete node :
# 1. Leaf node 
# 2. Node with right child 
# 3. Node with left child 
# 4. Node with both children

class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.cnt=0

    def insert(self, new_node):
        if self.root is None:
            self.root=new_node
            self.cnt+=1
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        self.cnt+=1
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        self.cnt+=1
                        return
                    else:
                        temp=temp.right

    def delete(self, rt, value):
        if rt is None:
            return rt
        if value<rt.data:
            rt.left=self.delete(rt.left, value)
        elif value>rt.data:
            rt.right=self.delete(rt.right, value)
        else:
            # Node with only one child ,two child,no child
            if rt.left is None: #node with only right child or no child
                return rt.right
            if rt.right is None: #node with only left child
                return rt.left
            
            # Node with two childrens (left and right child)
            succ=self.get_successor(rt)
            rt.data=succ.data
            rt.right=self.delete(rt.right, succ.data)
        return rt
        
    def get_successor(self, temp):
        temp=temp.right
        while temp.left is not None :
            temp=temp.left
        return temp
    
    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")
    def level_order(self,rt):
        if rt is None:
            print("BST is Empty")
            return
        arr=[]
        cnt=0#for counting visiting node 
        arr.append(rt)
        level=0
        while cnt<len(arr):
            node_count=len(arr)-cnt#number of nodes to be visited
            print("\n Level:",level,end=" ")
            for i in range (node_count):
                temp=arr[cnt]
                cnt+=1
                print(temp.data,end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)    
            level+=1        

b1=BST()
b1.insert(Node(100))
b1.insert(Node(20))
b1.insert(Node(450))
b1.insert(Node(10))
b1.insert(Node(65))
b1.insert(Node(300))
print("\nInorder:")
b1.inorder(b1.root)
print("\nPreorder:")
b1.preorder(b1.root)
print("\nPostorder:")
b1.postorder(b1.root)
b1.delete(b1.root, 10)
print("\nAfter deleting 10:")
b1.inorder(b1.root)
print("\nLevel Order:")
b1.level_order(b1.root)