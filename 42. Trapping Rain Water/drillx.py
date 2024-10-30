# Accepted
# Runtime Beats 92.69%
# Memory Beats 17.18%

class Solution:
    def trap(self, height: List[int]) -> int:
        backtrack, trappedWater = [], 0
        for i in range(len(height)):
            # If the current height is greater than the last height in the backtrack
            while len(backtrack) > 0 and height[i] > height[backtrack[-1]]:
                iditch = backtrack.pop()

                # Left wall
                if len(backtrack) == 0:
                    break

                # Calculate the dimensions of the ditch
                l, r = backtrack[-1], i
                distance = r - l - 1
                depth = min(height[l], height[r]) - height[iditch]

                # Add the trapped water to the total
                trappedWater += distance*depth

            backtrack.append(i)

        return trappedWater
