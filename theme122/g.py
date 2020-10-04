class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

# 0 > 1 > 2 > 3 >4 > 5
def solution(node):
    while node:
        print(node.value)
        node = node.next_item


def solution2(node, number):
    asd = []
    i = 0

    while node:
        if node.value == number:
            asd.append(node.value)
            return i
        node = node.next_item
        i += 1

    if len(asd) == 0:
        return '-1'

        
node4 = Node('4')
node3 = Node('3', node4)
node2 = Node('2', node3)
node1 = Node('1', node2)

solution(node1)

#print(solution2(node1, str(3)))

