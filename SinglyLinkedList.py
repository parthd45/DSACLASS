# Create a Singly Linear Linked List with following operations
# Create Linked List
# Traverse and print the node values
# Insert node at a specific position
# Find Middle node and print its value
# Delete node
# Reverse list
# Calculate the sum of every two consecutive node values.
def solution():
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    class SinglyLinkedList:
        def __init__(self):
            self.head = None

        # 1. Create / Append Linked List
        def create(self, val):
            new_node = Node(val)
            if not self.head:
                self.head = new_node
                return
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        # 2. Traverse and print the node values
        def traverse(self):
            if not self.head:
                print("List is empty!")
                return
            temp = self.head
            while temp:
                print(temp.val, end=" -> " if temp.next else "")
                temp = temp.next
            print()

        # 3. Insert node at a specific position (0-indexed)
        def insert_at_position(self, pos, val):
            new_node = Node(val)
            if pos == 0:
                new_node.next = self.head
                self.head = new_node
                return

            temp = self.head
            for i in range(pos - 1):
                if not temp:
                    print(f"Invalid position: {pos}")
                    return
                temp = temp.next

            if not temp:
                print(f"Invalid position: {pos}")
                return

            new_node.next = temp.next
            temp.next = new_node

        # 4. Find Middle node and print its value (Simple Counting Approach)
        def find_middle(self):
            if not self.head:
                print("List is empty!")
                return

            # Step 1: Count total nodes in the list
            count = 0
            temp = self.head
            while temp:
                count += 1
                temp = temp.next

            # Step 2: Traverse to the middle index (count // 2)
            mid_index = count // 2
            temp = self.head
            for i in range(mid_index):
                temp = temp.next

            print(f"Middle node value: {temp.val}")

        # 5. Delete node by value
        def delete_node(self, val):
            if not self.head:
                print("List is empty!")
                return

            if self.head.val == val:
                self.head = self.head.next
                print(f"Node with value {val} deleted.")
                return

            temp = self.head
            while temp.next and temp.next.val != val:
                temp = temp.next

            if temp.next:
                temp.next = temp.next.next
                print(f"Node with value {val} deleted.")
            else:
                print(f"Value {val} not found in the list.")

        # 6. Reverse list
        def reverse(self):
            prev = None
            current = self.head

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            self.head = prev
            print("List reversed successfully.")

        # 7. Calculate the sum of every two consecutive node values
        def sum_consecutive_pairs(self):
            if not self.head or not self.head.next:
                print("At least two nodes are required to calculate consecutive pair sums.")
                return

            temp = self.head
            sums = []
            while temp and temp.next:
                pair_sum = temp.val + temp.next.val
                sums.append(f"({temp.val} + {temp.next.val} = {pair_sum})")
                temp = temp.next

            print("Consecutive pair sums:", ", ".join(sums))

    # --- Driver Code / Operations Demonstration ---
    sll = SinglyLinkedList()

    print("--- 1. Creating Linked List ---")
    for value in [10, 20, 30, 40, 50]:
        sll.create(value)

    print("\n--- 2. Traversing List ---")
    sll.traverse()

    print("\n--- 3. Inserting 25 at Position 2 ---")
    sll.insert_at_position(2, 25)
    sll.traverse()

    print("\n--- 4. Finding Middle Node ---")
    sll.find_middle()

    print("\n--- 5. Deleting Node with Value 30 ---")
    sll.delete_node(30)
    sll.traverse()

    print("\n--- 6. Reversing List ---")
    sll.reverse()
    sll.traverse()

    print("\n--- 7. Sum of Every Two Consecutive Node Values ---")
    sll.sum_consecutive_pairs()


# Run assignment solution
solution()