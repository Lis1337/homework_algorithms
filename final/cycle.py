def has_cycle(node):  #34627921     Ваша функция должна называться hasCycle. 
    slow, fast = node, node
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast: 
            return True 
        if fast is None: 
            return False 
    return False 
 
if __name__ == "__main__":
    hasCycle(node) 
    #main(input().split())
    #Формат ввода: В этой задаче вам нужно реализовать только функцию с решением, считывать входные данные не нужно.
