class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        try:
            for i in range(len(nums)):
                n = abs(nums[i])
                if nums[n-1] < 0:
                    return n

                nums[n-1] *= -1
        finally:
            for i in range(len(nums)):
                if nums[i] < 0:
                    nums[i] *= -1

        raise RuntimeError("no dups found")
