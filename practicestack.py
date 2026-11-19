class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:", s.items)
print("Top element:", s.peek())
print("Removed element:", s.pop())
print("Stack after pop:", s.items)
print("Is stack empty?", s.is_empty())