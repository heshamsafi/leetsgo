# Runtime Beats 5.61%
# Memory Beats 40.08%

from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # Get depth of tree
        d = depth(root)

        # track levels and sum
        l, s = 1, 0

        # BFS
        q = deque()
        q.append(root)
        q.append(None)
        while len(q) > 0:
            n = q.popleft()
            if n:
                # We are at the leaf level
                # Accumulate sum
                if l == d:
                    s += n.val
                
                # Append children to frontier, if any
                for ch in [n.left, n.right]:
                    if ch:
                        q.append(ch)

            # If we are not at the last level, then add a new level separator, and begin iterating over next level
            elif len(q) > 0:
                l += 1
                q.append(None)
        return s

def depth(root: Optional[TreeNode], n=0) -> int:
    if root == None:
        return n

    return max(depth(root.left, n+1), depth(root.right, n+1))

