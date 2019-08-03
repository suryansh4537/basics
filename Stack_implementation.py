class Stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "empty stack"
        else:
            return self.items[-1]

    def is_empty(self):
        return self.items==[]

    def print(self):
        return self.items

