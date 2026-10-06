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
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node  # appending new node

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            # Safely skip the next node
            if temp.next is not None:
                temp = temp.next.next
            else:
                break


# Driver Code
list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))

list.print()