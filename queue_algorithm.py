# Declare a queue with 10 slots and all its pointers.

Queue = [None for i in range(10)]
RearPointer = -1
FrontPointer = 0
QueueFull = len(Queue)
QueueLength = 0


# create a procedure that enqueues values into the queue.
def enqueue(value):
    global RearPointer, FrontPointer, QueueLength, Queue, QueueFull

    if QueueLength < QueueFull:
        if RearPointer > QueueFull:
            RearPointer = 0
        else:
            RearPointer += 1

        QueueLength += 1
        # QueueLength = QueueLength + 1
        Queue[RearPointer] = value
        print('value', value, 'was enqueued successfully')
    else:
        print('Queue is full, can not enqueue')


# create a procedure that enqueues values into the queue.
def dequeue():
    global RearPointer, FrontPointer, QueueLength, Queue, QueueFull

    if QueueLength != 0:
        value = Queue[FrontPointer]
        Queue[FrontPointer] = None
        print('value', value, 'was dequeued successfully')
        QueueLength -= 1
        # QueueLength = QueueLength + 1

        if FrontPointer == QueueFull - 1:
            FrontPointer = 0
        else:
            FrontPointer += 1

    else:
        print('Queue is empty')


# Testing data


# ENQUEUE VALUES 1 THROUGH TO 11 AND PRINT ARRAY RESULT
# Expected result should be:

# The queue is full
# result1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 12):
    enqueue(i)
print('result1:', Queue)


# DEQUEUE 11 TIMES AND PRINT ARRAY RESULT
# Expected results should be:

# The queue is empty
# [None, None, None, None, None, None, None, None, None, None]
for i in range(11):
    dequeue()
print('result2:', Queue)
