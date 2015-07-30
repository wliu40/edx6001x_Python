'''
For this exercise, you will be coding your very first class, a Queue class. Queues are a fundamental computer 
science data structure. A queue is basically like a line at Disneyland - you can add elements to a queue, 
and they maintain a specific order. When you want to get something off the end of a queue, you get the item that 
has been in there the longest (this is known as 'first-in-first-out', or FIFO). You can read up on queues 
at Wikipedia if you'd like to learn more.

In your Queue class, you will need three methods:

    __init__: initialize your Queue (think: how will you store the queue's elements? You'll need to initialize 
    an appropriate object attribute in this method)
    insert: inserts one element in your Queue
    remove: removes (or 'pops') one element from your Queue and returns it. If the queue is empty, 
    raises a ValueError.

When you're done, you should test your implementation. Your results should look something like this:

>>> queue = Queue()
>>> queue.insert(5)
>>> queue.insert(6)
>>> queue.remove()
5
>>> queue.insert(7)
>>> queue.remove()
6
>>> queue.remove()
7
>>> queue.remove()
Traceback (most recent call last):
  File "<stdin>", line 26, in <module>
  File "queue.py", line 15, in remove
    raise ValueError()
ValueError
'''

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def insert(self, val):
        if self.head == None:
            self.head = self.tail = Node(val)            
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    def remove(self):
        try:
            res = self.head.val
            self.head = self.head.next
            return res
        except:
            raise ValueError()
