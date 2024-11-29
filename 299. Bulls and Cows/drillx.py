# Runtime Beats 64.81%
# Memory Beats 6.09%
from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if len(secret) != len(guess):
            raise RuntimeError("bad guess") 
        
        bulls, cows, n = 0, 0, len(secret)
        asecret, aguess = list(secret), list(guess)
        # Count and wipe bulls
        for i in range(n):
            if asecret[i] == aguess[i]:
                bulls += 1
                asecret[i], aguess[i] = "", ""

        occMap = defaultdict(int)
        for i in range(n):
            if asecret[i] == "":
                continue
            occMap[asecret[i]] += 1
        
        for i in range(n):
            g = aguess[i]
            if g != "" and g in occMap and occMap[g] > 0:
                cows += 1
                occMap[g] -=1

        return f"{bulls}A{cows}B"

