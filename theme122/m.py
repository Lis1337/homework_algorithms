class MyQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.isEmpty():
            print(None)
        else:
            print(self.items.pop(0))
    
    def peek(self):
        if self.isEmpty():
            print(None)
        else:
            print(self.items[0])
    
    def size(self):
        print(len(self.items))

queue = MyQueue()

n = int(input())
for i in range(n):
    c = input()
    if c == 'pop':
        queue.pop()
    elif c == 'peek':
        queue.peek()
    elif c == 'size':
        queue.size()
    else:
        x = c.split()
        queue.push(int(x[-1]))