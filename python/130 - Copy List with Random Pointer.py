
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: list[Node]) -> list[Node]:

    hash_map = {}
    node = head
    while node:
        hash_map[node] = Node(node.val)
        node = node.next

    node = head
    while node:
        aux_node = hash_map[node]
        aux_node.next = hash_map.get(node.next)
        aux_node.random = hash_map.get(node.random)
        node = node.next
    
    return hash_map.get(head)