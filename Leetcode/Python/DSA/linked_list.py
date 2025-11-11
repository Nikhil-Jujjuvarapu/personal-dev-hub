class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
    def print_LL(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append_l(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head=new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
    def pop(self):
        if self.length ==0:
            print("Emplty Linked List")
        if self.length==1:
            self.head=None
        else:
            temp = self.head
            pre_temp = self.head
            while temp.next!=None:
                pre_temp= temp
                temp = temp.next
            self.tail = pre_temp
            self.tail.next = None
            self.length-=1
    def prepend(self,value):
        new_node = Node((value))
        if self.length==0:            
            self.head = new_node
            self.tail = new_node      
        else:
            # temp = self.head
            # self.head = new_node
            # self.head.next = temp
            new_node.next = self.head
            self.head = new_node
        self.length+=1
    def popfirst(self):
        if self.length==0:
            print("Empty List")
            return None
        temp = self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head = self.head.next
            temp.next = None
        self.length-=1
        return temp.value
    def get(self,index):
        if index<0 or index >=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp #temp.value knwo the diff beacuse value in next method is not working
    def setLL(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
my_linked_list = LinkedList(17)
my_linked_list.append_l(19)
my_linked_list.append_l(1)
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.prepend(15)
my_linked_list.popfirst()
my_linked_list.print_LL()
my_linked_list.setLL(0,99)


