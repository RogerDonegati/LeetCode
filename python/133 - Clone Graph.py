class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: list['Node']) -> list['Node']:
    if not node:
        return node
    root = node
    queue = [root]
    hash_map = {root.val: Node(root.val)}

    while queue:
        node = queue.pop(0)
        cloned_node = hash_map[node.val]
        for neighbor in node.neighbors:
            if neighbor.val not in hash_map:
                hash_map[neighbor.val] = Node(neighbor.val)
                queue.append(neighbor)
            cloned_node.neighbors.append(hash_map[neighbor.val])
        hash_map[node.val] = cloned_node
    return hash_map[root.val]