#n = int(input())
#asd = []
#for i in range(n):
    #asd.append(str(input()))

#n = 8

class Stack:
    def __init__(self):
       self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self): 
        if self.items:
            return self.items.pop()
        print('error')

    def get_max(self):
        if self.items:
            return int(max(self.items))
        return None


stack = Stack()

n = int(input())
for i in range(n):
    c = input()
    if c == 'pop':
        stack.pop()
    elif c == 'get_max':
        print(stack.get_max())
    else:
        x = c.split()
        stack.push(int(x[-1]))
        