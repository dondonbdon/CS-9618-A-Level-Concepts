# Declare a stack with 10 slots and all its pointers.
Stack = [None for i in range(10)]
BasePointer = 0
TopPointer = BasePointer - 1
StackFull = len(Stack) - 1


# create a procedure that pushes values into the stack.
def push(value):
    global TopPointer
    if StackFull > TopPointer:
        # Push value because stack has space.
        Stack[TopPointer + 1] = value
        TopPointer += 1
        print(f'{value} pushed')
    else:
        # Stack has no space so value can not be pushed.
        print('Stack full')


# create a procedure that pops values out of the stack.
def pop():
    global TopPointer
    if BasePointer <= TopPointer:
        value = Stack[TopPointer]
        Stack[TopPointer] = None
        TopPointer -= 1
        print(f'{value} popped')

    else:
        # Stack is empty so no value can be popped out.
        print('Stack empty')


# Testing data

# PUSH VALUES 1 THROUGH TO 11 AND PRINT ARRAY RESULT
# Expected result should be:

# The stack is full
# result1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(12):
    push(i)

print('result1:', Stack)


# POP 11 TIMES AND PRINT ARRAY RESULT
# Expected results should be:

# The stack is empty
# [None, None, None, None, None, None, None, None, None, None]
for i in range(12):
    pop()

print('result2:', Stack)
