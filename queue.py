# Python3 program to implement Queue
# using two stacks

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # Add an item to the queue
    def add(self, x):
        self.s1.append(x)

    def __front(self, pop=True):
        # if both stacks are empty
        if len(self.s1) == 0 and len(self.s2) == 0:
            return -1

        # if s2 is empty and s1 has elements
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            if pop:
                return self.s2.pop()
            return self.s2[-1]
        else:
            if pop:
                return self.s2.pop()
            return self.s2[-1]

    # Remove an item from the queue
    def remove(self):
        return self.__front(pop=True)

    # Returns the value of the top("front") item of the queue
    def peek(self):
        return self.__front(pop=False)

    # Returns the number of items in the queue
    def length(self):
        return len(self.s1) + len(self.s2)

    # Returns whether queue has items or not
    def is_empty(self):
        return self.length() == 0


if __name__ == '__main__':
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)

    print(q.remove())
    print(q.remove())
    print(q.remove())
