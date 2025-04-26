class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    node = fast_node = head

    while fast_node and fast_node.next:
        fast_node = fast_node.next.next
        node = node.next
        if node == fast_node:
            return True
        
    return False