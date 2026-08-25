"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        values  = []

        def dfs(root):
            
            if root is None:
                return 0

            for children in root.children:
                dfs(children)

            values.append(root.val)

        dfs(root)
        return values