# Runtime Beats 100.00% 
# Memory Beats 32.96%

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1]*n for _ in range(m)]
        cache[0][0] = 1
        return uniquePaths(m-1, n-1, cache)

def uniquePaths(r: int, c: int, cache: List[List[int]]):
    if r < 0 or c < 0:
        return 0
    if cache[r][c] != -1:
        return cache[r][c] 

    cache[r][c] = uniquePaths(r-1, c, cache) + \
                  uniquePaths(r, c-1, cache)
    return cache[r][c]
