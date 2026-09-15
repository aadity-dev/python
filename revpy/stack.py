# #using list as stack
stack = []

#push
stack.append(1)
stack.append('B')
stack.append('C')
print("stack: ", stack)

#peek
topElement = stack[-1]
print("Peek: ", topElement)

#pop
popElement = stack.pop()
print(popElement)

print("Stack after pop: ", stack)

isEmpty = not bool(stack)
print(isEmpty)
print(len(stack))

#creating a class using stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

myStack = Stack()

myStack.push('a')
myStack.push('b')
myStack.push(3)
print("Stack: ", myStack.stack)


print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())