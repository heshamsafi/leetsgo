# Runtime Beats 100.00%
# Memory Beats 16.81%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and not (low<=root.val<=high):
            if root.val > high:
                root = root.left
            elif root.val < low:
                root = root.right
            else:
                raise RuntimeError("Dead case")

        if not root:
            return None

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root
