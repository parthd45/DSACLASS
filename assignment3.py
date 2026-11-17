# Hospital Emergency Management using Priority Queue (Linked List)

class Node:
    def __init__(self, pid, name, pr):
        self.pid = pid
        self.name = name
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, pid, name, pr):
        new_node = Node(pid, name, pr)

        # If queue is empty OR new patient has higher priority than front
        if self.front is None or new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            while temp.next is not None and temp.next.priority <= new_node.priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Patient added!")

    def display_next(self):
        if self.front is None:
            print("No patients waiting.")
        else:
            print("Next Patient:", self.front.pid, "-", self.front.name, "(Priority:", self.front.priority, ")")

    def dequeue(self):
        if self.front is None:
            print("No patients to remove.")
        else:
            print("Removed Patient:", self.front.pid, "-", self.front.name)
            self.front = self.front.next

    def display_all(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            temp = self.front
            print("\nWaiting Patients:")
            while temp is not None:
                print("ID:", temp.pid, "| Name:", temp.name, "| Priority:", temp.priority)
                temp = temp.next


pq = PriorityQueue()

while True:
    print("\n1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        pr = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))
        pq.enqueue(pid, name, pr)

    elif ch == 2:
        pq.display_next()

    elif ch == 3:
        pq.dequeue()

    elif ch == 4:
        pq.display_all()

    elif ch == 5:
        break

    else:
        print("Wrong choice!")