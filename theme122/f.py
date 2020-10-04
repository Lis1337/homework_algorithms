def solution(node, idx):
    i = 0
    head = node
    if idx == 0:
        head = node.next_item
        return head

    while i != idx-1:
        node = node.next_item
        i += 1
    c = node.next_item
    node.next_item = c.next_item
    return head