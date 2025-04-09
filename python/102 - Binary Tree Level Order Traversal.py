
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        result = []
        queue = [root]    
        while queue:
            aux = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                aux.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(aux)
        
        return result