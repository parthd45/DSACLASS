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

        # 4. Find Middle node, print its value, and delete it
        def find_and_delete_middle(self):
            if not self.head:
                print("List is empty!")
                return

            # Step 1: Count total nodes in the list
            count = 0
            temp = self.head
            while temp:
                count += 1
                temp = temp.next

            # Step 2: Traverse to the middle index (count // 2) and keep track of previous node
            mid_index = count // 2
            temp = self.head
            prev = None

            for i in range(mid_index):
                prev = temp
                temp = temp.next

            print(f"Middle node value: {temp.val}")

            # Step 3: Delete the middle node
            if prev is None:
                # Single node case: deleting head
                self.head = self.head.next
            else:
                # Skip the middle node
                prev.next = temp.next

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

        # 8. Delete the first and last node in SLL
        def delete_first_and_last(self):
            if not self.head:
                print("List is empty!")
                return

            # Case 1: Only 1 node in the list
            if not self.head.next:
                self.head = None
                print("First (and only) node deleted.")
                return

            # Case 2: Only 2 nodes in the list
            if not self.head.next.next:
                self.head = None
                print("First and last nodes deleted. List is now empty!")
                return

            # Case 3: 3 or more nodes
            # Step 1: Delete the first node
            self.head = self.head.next

            # Step 2: Delete the last node
            prev = None
            current = self.head
            while current.next:
                prev = current
                current = current.next

            prev.next = None
            print("First and last nodes deleted.")
        #9] Delete alternate node in sll
        def delete_alternate_nodes(self):
            prev= self.head
            temp= self.head.next
            while prev and temp:
                prev.next=temp.next
                temp=None##delte the node
                prev=prev.next
                if prev:
                    temp=prev.next
        #10] Concatenate two sll
        def concatenate(self, other_list):
            if not self.head:
                self.head = other_list.head
                return

            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = other_list.head
    # --- Execution Driver ---
    sll = SinglyLinkedList()

    print("--- 1. Creating Linked List ---")
    for value in [10, 20, 30, 40, 50,60,70,80,90,100]:
        sll.create(value)

    print("\n--- 2. Traversing List ---")
    sll.traverse()

    print("\n--- 3. Inserting 25 at Position 2 ---")
    sll.insert_at_position(2, 25)
    sll.traverse()

    print("\n--- 4. Finding and Deleting Middle Node ---")
    sll.find_and_delete_middle()
    sll.traverse()

    print("\n--- 5. Deleting Node with Value 30 ---")
    sll.delete_node(30)
    sll.traverse()

    print("\n--- 6. Reversing List ---")
    sll.reverse()
    sll.traverse()

    print("\n--- 7. Sum of Every Two Consecutive Node Values ---")
    sll.sum_consecutive_pairs()

    print("\n--- 8. Deleting First and Last Nodes ---")
    sll.delete_first_and_last()
    sll.traverse()
    
    print("\n--- 9. Deleting Alternate Nodes ---")
    sll.delete_alternate_nodes()
    sll.traverse()
    
    print("\n--- 10. Creating Second List (sll2) and Concatenating ---")
    sll2 = SinglyLinkedList()
    for value in [110, 120, 130]:
        sll2.create(value)

    print("List 2 (sll2):")
    sll2.traverse()

    sll.concatenate(sll2)
    print("Combined List (sll + sll2):")
    sll.traverse()


# Run assignment solution
solution()