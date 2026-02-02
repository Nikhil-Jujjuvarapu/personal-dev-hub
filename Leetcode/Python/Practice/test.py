class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
    def pop(self):
        if self.length == 0:
            return None
        
        if self.length==1:
            self.head = self.tail = None
            self.length-=1
            return temp
        temp =self.head
        while temp.next!=None:
            pre_temp =temp
            temp = temp.next
        self.tail = pre_temp
        self.tail.next = None
        self.length-=1
        return temp
        
    def print_linked_list(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return
        while temp!=None:
            print(temp.value)
            temp=temp.next



# my_linked_list = LinkedList()
# my_linked_list.append(1)
# my_linked_list.append(1)
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.print_linked_list()

