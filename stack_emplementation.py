class Stack():

    def __init__(self):
        self.my_stack = [1,2]

    def is_empty(self):
        return self.my_stack == [1,2]

    def push_item(self,value):
        self.my_stack.append(value)

    def pop_item(self):
        if self.is_empty():
            print("Stack is empty")
        return self.my_stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        return self.my_stack[-1]

    def size(self):
        return len(self.my_stack)

    def display(self):
        print(self.my_stack)

s = Stack()
s.display()
s.push_item(3)
s.display()
s.push_item(4)
s.display()
print(s.pop_item())
s.display()
print(s.peek())
s.display()
print(s.size())
