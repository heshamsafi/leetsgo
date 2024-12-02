# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        # Pre-order traversal
        v, l, r = root.val, self.tree2str(root.left), self.tree2str(root.right)
        
        # If r is present then {l} must be
        if r == "":
            return f"{v}" \
                    + (f"({l})" if l != "" else "")

        return f"{v}({l})({r})"
