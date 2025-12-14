class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        total = carry
        if l1:
            total+=l1.val
            l1=l1.next
        if l2:
            total+=l2.val
            l2=l2.next
        carry = total//10
        curr.next = ListNode(total%10)
        curr = curr.next
    return dummy.next
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))



if __name__ == "__main__":
    l1 = build_linked_list([1,0,0])
    l2 = build_linked_list([1])
    print_linked_list(addTwoNumbers(l1, l2))
