# Singly Linear Linked List adding node at a given position

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next != None:
                temp = temp.next

            temp.next = new_node

    # Insert node at a given position
    def insert(self, new_node, pos):

        # Insert at first position
        if pos == 1:
            new_node.next = self.head
            self.head = new_node

        else:
            temp = self.head
            p = 1

            while p != pos - 1:
                temp = temp.next
                p += 1

            new_node.next = temp.next
            temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head

        while temp != None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Create linked list
list1 = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list1.append(n1)
list1.append(n2)
list1.append(n3)
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))

# Display original list
print("Original List:")
list1.display()

# Insert 100 at position 1
list1.insert(Node(100), 1)

print("\nAfter inserting 100 at position 1:")
list1.display()

# Insert 66 at position 4
list1.insert(Node(66), 4)

print("\nAfter inserting 66 at position 4:")
list1.display()