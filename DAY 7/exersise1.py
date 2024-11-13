class Stack:
    def __init__(self, content=None):
        if content:
            self.content = content
        else:
            self.content = []

    def __str__(self):
        return "".join([f"<{str(val)}>\n" for val in self.content[::-1]])

    def __add__(self, other):
        return Stack(self.content + other.content)

    def push(self, value):
        self.content.append(value)

    def pop(self):
        if self.isempty():
            return "The stack is empty"
        else:
            return self.content.pop()

    def top(self):
        if self.isempty():
            return "The stack is empty"
        else:
            return self.content[-1]

    def isempty(self):
        return len(self.contant) == 0


stack = Stack()
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(2)
stack1 = Stack()
stack1.push(3)
stack1.push(3)
stack1.push(3)
stack1.push(3)
print(stack.top())
print(stack + stack1)
