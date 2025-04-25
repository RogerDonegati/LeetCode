class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def middleNode(head: ListNode) -> ListNode:
    if not head.next:
        return head

    node = fast_node = head
    while fast_node and fast_node.next:
        fast_node = fast_node.next.next
        node = node.next

    return node