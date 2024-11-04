# Runtime Beats 100.00%
# Memory Beats 11.52%
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs: List[List[int]] = []
        subsets(nums, [], subs, 0)
        return subs

def subsets(nums: List[int], buffer: List[int], subs, j: int):
    if j == len(nums):
        # Base case: if we have considered all elements in nums
        subs.append(buffer[:])
    else:
        # Recursive case: consider the next element in nums

        # Include the next element
        buffer.append(nums[j])
        subsets(nums, buffer, subs, j+1)

        # Exclude the next element
        buffer.pop()
        subsets(nums, buffer, subs, j+1)
