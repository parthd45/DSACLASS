class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:", q.items)
print("Front element:", q.peek())
print("Removed element:", q.dequeue())
print("Queue after dequeue:", q.items)
print("Is queue empty?", q.is_empty())