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

'''Dequeue --> FIFO (First in first out)'''

from collections import deque

q = deque()

print(q)

# Enqueue - Add element to the right - O(1)

q.append(4)
q.append(5)
q.append(7)
q.append(10)

print(q)

# Dequeue - Remove element from left to the right - o(1)

p1 = q.popleft()
p2 = q.popleft()
print(f"We removed {p1} and {p2} from q and now q = {q}")

'''Recursion:'''

def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibo(n - 1) + fibo(n - 2)

print(fibo(34))

'''Bonus memoization:'''
def fiboMemo(n, memo = {}):
    if n in memo: return memo[n]
    if n == 0: return 0
    elif n == 1: return 1
    else: 
        memo[n] = fibo(n - 1) + fibo(n - 2)
        return memo[n]

print(fibo(34))

'''Lets fun with it.'''

def fibo_thead_fun(p):
    result = fibo(p)
    print(f"fibo(p) = {result}")
def fibo_thead_memo_fun(p):
    result = fiboMemo(p)
    print(f"fiboMemo(p) = {result}")

import threading

fibo_thread = threading.Thread(target=fibo_thead_fun,args=[5])
fiboMemo_thread = threading.Thread(target=fibo_thead_memo_fun,args=[5])

fibo_thread.start()
fiboMemo_thread.start()

fibo_thread.join()
fiboMemo_thread.join()

# import asyncio

# async def myMain(callval):
#     await asyncio.gather(fibo_thead_fun(callval),fibo_thead_memo_fun(callval))

# asyncio.run(myMain(37))

# I tried multi threading here.

'''Binary Search'''

Search_arr = [-10,-5,-3,0,2,5,7,9,11,13,43]
target = 9

def binarySearch(arr, tar, l, r):
    if arr[l] == tar:
        return l
    else:
        m = (l + r) // 2
        if arr[m] > tar: r = m
        else: l = m
        return binarySearch(arr,tar,l,r)
    

print(binarySearch(Search_arr,target,0,len(Search_arr)))

'''Shorting an array:'''

nums = [-4,-1,0,3,10]
squre_nums = [x**2 for x in nums]
print(squre_nums)
l = 0
r = len(squre_nums) - 1
shorted_squered_arr = []

while l <= r:
    if squre_nums[l] > squre_nums[r]: 
        shorted_squered_arr.append(squre_nums[l])
        l += 1
    else: 
        shorted_squered_arr.append(squre_nums[r])
        r -= 1
print(shorted_squered_arr)

