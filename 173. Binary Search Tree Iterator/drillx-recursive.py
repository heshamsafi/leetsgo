# Runtime Beats 19.45%
# Memory Beats 24.58%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.gen, self.curr = iterator(root), None

        # Initialize self.curr (iterator) by pointing at first element if any
        self._advance()

    def next(self) -> int:
        # Push iterator (unless there is an unconsumed element at self.curr)
        # The idempotency of the hasNext API pays off here.
        # because a user can call hasNext n times before calling next and that 
        # should push the pointer only once
        _ = self.hasNext()

        # Consume self.curr
        # i.e return and wipe the value
        curr, self.curr = self.curr, None

        return curr

    # This API is designed to be idempotent
    def hasNext(self) -> bool:
        if self.curr is not None:
            return True

        self._advance()

        return self.curr != None

    def _advance(self):
        try:
            self.curr = next(self.gen)
        except StopIteration:
            self.curr = None

# Yield here is used to freeze the recursion stack trace
# which models the iterator state
def iterator(root):
    if root != None:
        yield from iterator(root.left)
        yield root.val
        yield from iterator(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
