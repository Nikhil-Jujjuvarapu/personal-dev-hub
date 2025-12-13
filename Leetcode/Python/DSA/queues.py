class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = self.last = new_node
            self.length = 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        if self.length == 0:
            raise Exception("Queue is empty")
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp.value  # Return value, not node


my_q = Queue(1)
my_q.enqueue(2)
my_q.dequeue()
my_q.print_queue()
        