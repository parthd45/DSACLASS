# Reverse a singly linked list

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node at the end
    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Display the linked list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Reverse the linked list
    def reverse(self):
        current = self.head
        prev = None

        while (current):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


# Create linked list
list1 = LinkedList()

list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)

# Display original list
print("Original list:")
list1.display()

# Reverse linked list
list1.reverse()

# Display reversed list
print("Reversed list:")
list1.display()