import operator       #34622170


OPERATORS = {
    '+': operator.add,
    '*': operator.mul,
    '/': operator.truediv,
    '-': operator.sub
}


class Stack:            
    def _private(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def pol_calc_v2(input): 
    stack = Stack()
    stack._private()
    for i in input:
        if i not in OPERATORS:
            stack.push(int(i))
        else:
            z = stack.pop()
            x = stack.pop()
            stack.push(OPERATORS[i](x, z))
    return int(stack.pop())


if __name__ == "__main__": 
    c = input().split()
    print(pol_calc_v2(c))
