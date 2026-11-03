# # #using list as stack
# stack = []

# #push
# stack.append(1)
# stack.append('B')
# stack.append('C')
# print("stack: ", stack)

# #peek
# topElement = stack[-1]
# print("Peek: ", topElement)

# #pop
# popElement = stack.pop()
# print(popElement)

# print("Stack after pop: ", stack)

# isEmpty = not bool(stack)
# print(isEmpty)
# print(len(stack))

# #creating a class using stack
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, element):
#         self.stack.append(element)

#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         return self.stack.pop()
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is Empty"
#         return self.stack[-1]
#     def isEmpty(self):
#         return len(self.stack) == 0

#     def size(self):
#         return len(self.stack)

# myStack = Stack()

# myStack.push('a')
# myStack.push('b')
# myStack.push(3)
# print("Stack: ", myStack.stack)


# print("Pop: ", myStack.pop())
# print("Stack after Pop: ", myStack.stack)
# print("Peek: ", myStack.peek())
# print("isEmpty: ", myStack.isEmpty())
# print("Size: ", myStack.size())

#stack using linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

        #insert at beginning
        def insert_at_beginning(Self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_Node
        
        #insert at end
        def insert_at_end(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            return 
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
    
