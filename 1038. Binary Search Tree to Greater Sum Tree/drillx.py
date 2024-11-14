# Runtime Beats 100.00%
# Memory Beats 73.71%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    # In order DFS
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Exit condition
        if root == None:
            return None

        # go right then left
        # This ensures that we iterate from the largest item to smaller.
        # After all trees are a sorted data structure
        self.bstToGst(root.right)
        
        # Visit node
        root.val += self.sum
        self.sum = root.val

        # Now go left
        self.bstToGst(root.left)

        return root
