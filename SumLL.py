class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Helper method to append nodes to the linked list
    def create(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Print sum of consecutive pairs
    def sum_consecutive_pairs(self):
        if not self.head or not self.head.next:
            print("At least two nodes are required to calculate consecutive pair sums.")
            return

        temp = self.head
        sums = []
        while temp and temp.next:
            pair_sum = temp.val + temp.next.val
            sums.append(str(pair_sum))
            temp = temp.next

        # Prints sums separated by space
        print(*sums)

# --- Driver Code ---
sll = SinglyLinkedList()

# Input: 5 -> 10 -> 15 -> -10 -> 50
for value in [5, 10, 15, -10, 50]:
    sll.create(value)

# Output: 15 25 5 40
sll.sum_consecutive_pairs()