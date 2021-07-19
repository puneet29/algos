import sys

class Stack:
    """
    A LIFO Stack implementation
    """
    def __init__(self, max_size=sys.maxsize):
        self.stack = []
        self.max_size = max_size

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        repr = "HEAD -> "
        for i in self.stack[::-1]:
            repr += str(i) + ", "
        return repr[:-2]
    
    def push(self, element):
        if len(self) + 1 >= self.max_size:
            raise Exception(f"Stack Overflow: Max Size for Stack is {self.max_size}")
        else:
            self.stack.append(element)
    
    def pop(self):
        if len(self) > 0:
            return self.stack.pop()
        else:
            raise Exception("Stack is empty. Can't use pop when stack is empty")
    
    def peep(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self) == 0
    
    def isFull(self):
        return len(self) == self.max_size

if __name__ == '__main__':
    stack = Stack()
    print("stack.push(10)")
    stack.push(10)
    print("stack.push(20)")
    stack.push(20)
    print("stack.push(30)")
    stack.push(30)
    print("stack.push(40)")
    stack.push(40)
    print("stack.isFull():", stack.isFull())
    print("stack:", stack)
    print("stack.peep():", stack.peep())
    print("stack.pop():", stack.pop())
    print("len(stack):", len(stack))
    print("stack.pop():", stack.pop())
    print("stack.pop():", stack.pop())
    print("stack.pop():", stack.pop())
    print("stack.isEmpty():", stack.isEmpty())
    