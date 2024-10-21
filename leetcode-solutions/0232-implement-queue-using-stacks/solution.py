class MyQueue:

    def __init__(self):
        self.stack1 = []  # Stack used for enqueue operations
        self.stack2 = []  # Stack used for dequeue operations

    def push(self, x: int) -> None:
        # Always push the new element onto stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # Transfer elements from stack1 to stack2 only if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop from stack2, which represents the front of the queue
        return self.stack2.pop()

    def peek(self) -> int:
        # Transfer elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Peek the last element in stack2, which is the front of the queue
        return self.stack2[-1]

    def empty(self) -> bool:
        # The queue is empty if both stacks are empty
        return not self.stack1 and not self.stack2

