class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def middleNode(head: ListNode) -> ListNode:
    if not head.next:
        return head

    node = head
    fast_node = head.next

    while fast_node:
        fast_node = fast_node.next
        if fast_node:
            fast_node = fast_node.next
        node = node.next

    return node