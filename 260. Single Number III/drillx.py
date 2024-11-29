class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # all the duplicates will eliminate each other
        # xorMask = n1 xor n2
        # Then we need to find a way to separate [n1, n2] 
        # which is the solution
        xorMask = 0
        for num in nums:
            xorMask ^= num

        # This operation creates a bit mask with a single bit set.
        # This bit will be the least significant set bit in xorMask
        #
        # This because -xorMask = 2's compliment of xorMask
        # 2's compliment = invert all the bits, then add 1 to number
        #
        # Example:
        # n = 18 (binary: 00010010)
        # -n = -18 (binary: 11101110 in two's complement form)
        # n & -n:
        # 00010010 & 11101110 = 00000010
        singleBitMask = xorMask & -xorMask

        # Divide the nums into two subsets using the singleBitMask
        # Set1 => numbers that have the selected bit set.
        # Set2 => numbers that have the selected bit unset.
        # Each set has only one number that is not duplicated
        # All the duplicated numbers will cancel each other out
        # and only the single Number from each set will remain.
        n1, n2 = 0, 0
        for num in nums:
            if num & singleBitMask:
                n1 ^= num
            else:
                n2 ^= num

        return [n1, n2]

        
