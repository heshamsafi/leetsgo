# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        result = [[]]
        frontier = deque([root, None])
        while len(frontier) > 0:
            node = frontier.popleft()
            if node:
                # Visit node
                result[-1].append(node.val)

                # Enqueue children
                children = [node.left, node.right]
                for child in children:
                    if child:
                        frontier.append(child)
            elif len(frontier) > 0 and frontier[-1] != None:
                frontier.append(None)
                result.append([])

        for i in range(len(result)):
            if i%2 != 0:
                 result[i].reverse()

        return result
