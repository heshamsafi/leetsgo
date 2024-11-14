# Runtime Beats 100.00%
# Memory Beats 18.60%

from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Group people by group sizes
        # Alternatively if we want to save space we can sort here to group by group sizes
        # but it is a trade off because sorting would increase the runtime from O(n) to O(nlogn)
        buckets = defaultdict(list)
        for i in range(len(groupSizes)):
            gs = groupSizes[i]
            buckets[gs].append(i)

        groups = []
        # Go over every bucket and split them into groups
        for gs, bucket in buckets.items():
            groupCount = len(bucket) // gs

            # The problem statement indicates that this should never happen with the
            # provided test cases
            if len(bucket) % gs != 0:
                raise RuntimeError("Bucket can not be split evenly")

            # Split the bucket into groups
            for i in range(groupCount):
                start, end = i*gs, i*gs+gs
                groups.append(bucket[start:end])

        return groups
