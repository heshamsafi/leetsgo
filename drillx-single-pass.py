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
        frontier = deque([root, None])
        result, reverse = [], False
        currLevel = deque()
        while len(frontier) > 0:
            node = frontier.popleft()
            if node:
                # Visit node
                append = currLevel.appendleft if reverse else currLevel.append
                append(node.val)

                # Enqueue children
                for child in [node.left, node.right]:
                    if child:
                        frontier.append(child)
            else:
                result.append(list(currLevel))
                currLevel = deque()
                reverse = not reverse

                # Keep going?
                if len(frontier) > 0 and frontier[-1] != None:
                    frontier.append(None)

        return result
