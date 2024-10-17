"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node

        queue = [node]
        visited = {}
        visited[node] = Node(node.val, [])

        while queue:
            old = queue.pop(0)
            new = visited[old]

            for old_neigh in old.neighbors:
                if old_neigh in visited:
                    new.neighbors.append(visited[old_neigh])
                    continue
                
                queue.append(old_neigh)
                visited[old_neigh] = Node(old_neigh.val, [])
                new.neighbors.append(visited[old_neigh])

        return visited[node]