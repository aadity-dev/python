#using list as stack
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
