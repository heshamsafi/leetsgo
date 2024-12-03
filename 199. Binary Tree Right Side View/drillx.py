# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        # BFS while keeping track of levels
        # We keep track of levels by sandwitching 
        # a None in the frontier between every two levels
        rightView = [None]
        frontier = deque([root, None])
        while len(frontier) > 0:
            node = frontier.popleft()
            if node:
                rightView[-1] = node.val
                # Make sure to go left to right
                # This way the last node we see in every level
                # is the one on the rightSideView
                for child in [node.left, node.right]:
                    if child:
                        frontier.append(child)
            elif len(frontier) > 0 and frontier[-1] is not None:
                # Going into a deeper tree level
                frontier.append(None)
                rightView.append(None)

        return rightView

