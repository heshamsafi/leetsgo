class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            raise RuntimeError("not enough input")

        i, j = 0, len(numbers)-1

        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                # +1 because array is 1-based
                return [i+1, j+1]
            elif sum < target:
                # if the sum is too small
                # we need to increase it
                # Only advancing the i pointer will do that 
                i += 1
            elif sum > target:
                # if the sum is too large
                # we need to reduce it
                # Only advancing the j pointer will do that 
                j -= 1
            else:
                raise RuntimeError("This code should be dead")

        raise RuntimeError("No solution was found")
