# Accepted submitted at Oct 29, 2024 10:40
# Runtime Beats 100.00%
# Memory MB Beats 69.54%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterator
    treeHead: TreeNode = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None: return
        
        # Visit

        # Link adjancent linked list nodes
        if self.treeHead:
          self.treeHead.right = root
        
        # Move the left, right pointers out of the node into stack frame
        # we gotta do this because, they will be wiped out in lower stack frames
        left, right = root.left, root.right
        root.left, root.right = None, None

        # Move iterator to next node
        self.treeHead = root
        
        # Recurse left and right
        self.flatten(left)
        self.flatten(right)
