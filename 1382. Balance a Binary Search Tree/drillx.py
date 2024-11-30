# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vine = []
        convertToVine(root, vine)
        return balanceVine(vine, 0, len(vine))
        
def convertToVine(root: Optional[TreeNode], vine: List[TreeNode]):
    if root is not None:
        convertToVine(root.left, vine)
        vine.append(root)
        convertToVine(root.right, vine)

def balanceVine(vine, l, h):
    if l >= h:
        return None

    m = (h+l)//2
    vine[m].left, vine[m].right = \
            balanceVine(vine, l, m), balanceVine(vine, m+1, h)

    return vine[m]

