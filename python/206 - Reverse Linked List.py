class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    if not head:
        return None

    node = head
    previous = None
    
    while node.next:
        tempNode = node
        tempNext = node.next

        node.next = previous
        previous = tempNode
        node = tempNext
    node.next = previous
    return node

def deleteDuplicates(head: ListNode) -> ListNode:
    previousNode = head
    node = head.next
    while node:
        if node.val == previousNode.val:
            previousNode.next = node.next
        node = node.next

    return head

head = node = ListNode(1)
for i in range(2,5):
    node.next = ListNode(i)
    node = node.next

node.next = ListNode(i)

print(deleteDuplicates(head)) 





