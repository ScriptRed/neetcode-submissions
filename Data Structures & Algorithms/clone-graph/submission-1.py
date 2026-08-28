"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        head = None
        nodeToNew = {}
        stack = deque([node])
        
        def dfs(parent):
            if not parent:
                return None
            newNode = Node(parent.val)
            nodeToNew[parent] = newNode
            for neighbour in parent.neighbors:
                if neighbour not in nodeToNew:
                    new = dfs(neighbour)
                    newNode.neighbors.append(new)
                else:
                    newNode.neighbors.append(nodeToNew[neighbour])
            return newNode

        return dfs(node)


        
        
        