class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_dll(self):
        temp = self.head
        while temp !=None:
            print(temp.value)
            temp=temp.next
    def dll_append(self,value):
        new_node = Node(value)
        if self.length==0:            
            self.head = new_node
            self.tail = new_node
            self.length = 1        
        else:
            temp = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.prev = temp
            self.length +=1
        return True
    def prepend_dll(self,value):
        new_node = Node(value)
        if self.length==0:            
            self.head = new_node
            self.tail = new_node
            self.length = 1        
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            temp.prev = self.head
            self.length+=1
        return True
    def pop_first(self):
        if self.length == 0:
            return "Empty List"
        temp = self.head
        if self.length==1:
            self.head=None
            self.tail = None
            self.length=0
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
            self.length-=1
        return temp
    def get(self,index):
        if index<0 and index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        # print(temp.value)
        return temp
    def set_val(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self,index,value):
        if index<0 and index>=self.length:
            return False
        if index==0:
            return self.prepend_dll(value)
        if index==self.length:
            return self.dll_append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        temp1 = self.get(index)
        new_node.next=temp.next
        new_node.prev = temp
        temp1.prev=new_node
        temp.next=new_node
        self.length+=1
        return True

               


my_dll = DLL(1)
my_dll.dll_append(2)
my_dll.prepend_dll(0)
my_dll.set_val(1,15)
# my_dll.pop_first()
# my_dll.get(0)
my_dll.insert(1,98)
my_dll.print_dll()