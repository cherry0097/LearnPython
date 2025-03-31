'''
Here on the code we will discuss about datastructure and algorithm.
'''

A = [1, 2] # It actually means A = [1, 2, _, _]

'''Singly linked list'''

class SinglyNode:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)
D = SinglyNode(10)

Head.next = A
A.next = B
B.next = C
C.next = D
D.next = None

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

display(Head)

'''Doubly Linked list'''

class DoublyNode:
    def __init__(self,val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

head = tail = DoublyNode(1)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))

display(head)

def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next = head)
    head.prev = new_node
    return new_node,tail
head, tail = insert_at_beginning(head, tail, 11)
head, tail = insert_at_beginning(head, tail, 6)
head, tail = insert_at_beginning(head, tail, 13)

display(head)
