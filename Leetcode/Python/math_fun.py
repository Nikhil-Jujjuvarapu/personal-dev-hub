class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0          
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def apend_ll(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length+=1
    def pop(self):
        if self.length==0:
            print("Empty Linked List")
        if self.length==1:
            self.head=None
        else:
            temp = self.head
            pre_temp = self.head
            while temp.next!=None:
                pre_temp = temp
                temp = temp.next
            self.tail = pre_temp
            self.tail.next = None
            self.length-=1
    def prepend(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
    def pop_first(self):
        if self.length==0:
            print("Empty Linked List")
        if self.length==1:
            self.head=None           
        else:
            temp = self.head
            self.head = temp.next
        self.length-=1
    def 


my_ll = LinkedList(15)
my_ll.apend_ll(15)
my_ll.prepend(88)
my_ll.prepend(88)
my_ll.pop_first()
my_ll.print_ll()