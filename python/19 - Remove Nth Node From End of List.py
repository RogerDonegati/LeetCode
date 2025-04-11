class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if not head or not head.next:
        return None

    node = head
    cache = []
    while node:
        cache.append(node)
        node = node.next

    if n+1 > len(cache):
        return head.next

    previousNode = cache[-n-1]
    previousNode.next = previousNode.next.next if previousNode.next else None
    return head

# TODO think of a different solution whithout using list.