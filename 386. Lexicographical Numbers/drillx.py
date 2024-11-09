# This problem is asking for pre-order dfs for the decimal numbers indirectly

class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        self.result, self.upperlimit = [], n
        self.order(0)
        return self.result

    def order(self, prefix):
        # Prune tree leaves 
        if prefix > self.upperlimit:
            return

        # Visit (pre-order)
        if prefix > 0:
            self.result.append(prefix)

        for i in range(0, 10):
            # Skip the leading 0
            if prefix == 0 and i == 0:
                continue
            
            # Append the next digit
            nprefix = prefix *10 + i

            # go down the tree
            self.order(nprefix)




# Example 1

# 13
# -
# Loop on a single digit
# 1 
#  10 11 12 13 ~14~(over the limit)
# 2
#  ~20~ (over the limit)
# 3
#  ~30~ (over the limit)
# 4
#  ~40~ (over the limit)
# 5
#  ~50~ (over the limit)
# 6
#  ~60~ (over the limit)
# 7
#  ~70~ (over the limit)
# 8
#  ~80~ (over the limit)
# 9
#  ~90~ (over the limit)
# Break the loop

# Output : [1,10,11,12,13,2,3,4,5,6,7,8,9]

# Example 2
# 999
# -
# Loop on a single digit
# 1
#  10                                           11                                        12                                       13 14 15 16 17 18 19
#   100 101 102 103 104 105 106 107 108 109      110 111 112 113 114 115 116 117 118 119   120 121 122 123 124 125 126 127 128 129   130 131 132 133 134 135 136 137 138 139

