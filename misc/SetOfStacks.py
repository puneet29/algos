# Problem Description: start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack


class SetOfStacks:
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = [[0 for i in range(threshold)]]  # Set of one stack
        self.top = -1

    def push(self, val):
        if(self.top == self.threshold-1):
            self.stacks.append([0 for i in range(self.threshold)])
            self.top = -1
        self.top += 1
        self.stacks[-1][self.top] = val

    def pop(self):
        if(self.top == -1):
            if(len(self.stacks) <= 1):
                return -1
            del self.stacks[-1]
            self.top = self.threshold - 1
            element = self.stacks[-1][self.top]
            self.top -= 1
            return element
        element = self.stacks[-1][self.top]
        self.top -= 1
        return element


# For testing the class
if __name__ == "__main__":
    stackSet = SetOfStacks(10)
    for i in range(100):
        stackSet.push(i)

    for i in range(50):
        print(stackSet.pop())

    for i in range(10):
        stackSet.push(i*2)

    for i in range(60):
        print(stackSet.pop())
