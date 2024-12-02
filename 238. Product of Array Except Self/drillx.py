class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r, r2l = rollingProd(nums), rollingProd(nums[::-1])[::-1]
        result = []
        for i in range(len(nums)):
            l, r = i-1, i+1
            l = 1 if l < 0 else l2r[l]
            r = 1 if r >= len(nums) else r2l[r]
            result.append(l*r)
        return result

def rollingProd(nums):
   rProd, prev = [], 1
   for num in nums:
       prev = prev*num
       rProd.append(prev)
   return rProd

