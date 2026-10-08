class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Insert node at a given position
    # Positions start from 1
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        # Insert at first position
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        current_position = 1

        while temp is not None and current_position < pos - 1:
            temp = temp.next
            current_position += 1

        if temp is None:
            print("Position not found")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete the first node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next
        print("First node deleted")

    # Delete a node at a specific position
    # Positions start from 1
    def delete_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos < 1:
            print("Invalid position")
            return

        # Delete first node
        if pos == 1:
            self.head = self.head.next
            print("Node at position 1 deleted")
            return

        temp = self.head
        current_position = 1

        # Stop at the node before the target node
        while (
            temp is not None
            and temp.next is not None
            and current_position < pos - 1
        ):
            temp = temp.next
            current_position += 1

        if temp is None or temp.next is None:
            print("Position not found")
            return

        temp.next = temp.next.next
        print(f"Node at position {pos} deleted")

    # Delete the first node containing a specific value
    def delete_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        # If the head contains the value
        if self.head.data == value:
            self.head = self.head.next
            print(f"Node with value {value} deleted")
            return

        temp = self.head

        # Find the node before the matching node
        while temp.next is not None and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print(f"Value {value} not found")
        else:
            temp.next = temp.next.next
            print(f"Node with value {value} deleted")

    # Display linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Create linked list
list1 = LinkedList()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))

print("Original list:")
list1.display()

# Delete the first node
list1.delete_first()

print("\nAfter deleting the first node:")
list1.display()

# Delete node at position 2
list1.delete_position(2)

print("\nAfter deleting node at position 2:")
list1.display()

# Delete node by value
list1.delete_value(40)

print("\nAfter deleting node with value 40:")
list1.display()