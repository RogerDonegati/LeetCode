class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# string solution
def addTwoNumbers( l1: ListNode, l2: ListNode) -> ListNode:
    val1 = str(l1.val)
    while l1.next:
        l1 = l1.next
        val1 += str(l1.val)

    val2 = str(l2.val)
    while l2.next:
        l2 = l2.next
        val2 += str(l2.val)

    val3 = int(val1[::-1]) + int(val2[::-1])
    val3 = str(val3)[::-1]
    head = l3 = ListNode(int(val3[0]))
    for s in val3[1:]:
        l3.next = ListNode(int(s))
        l3 = l3.next

    return head