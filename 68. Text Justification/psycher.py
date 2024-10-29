# Accepted
# submitted at Oct 29, 2024 18:04
# Runtime: 0ms     Beats 100.00%
# Memory:  16.60MB Beats 63.74%

# This is a refined solution
# I submitted one that wasn't as clean and browsed other solutions befor rendering this final version
# I got the idea of comparing remains with the word index from one of the solutions (line 32)

class Solution:
   def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
           out = []
           while len(words) > 0:
               count = maxWidth
               curr_line = []
               while len(words) > 0 and count >= len(words[0]):
                   w = words.pop(0)
                   count -= len(w) + 1
                   curr_line.append(w)
               
               num_spaces = count + len(curr_line)
               eq_sp      = num_spaces // (len(curr_line) - 1) if len(curr_line) > 1 else 0
               remains    = num_spaces  % (len(curr_line) - 1) if len(curr_line) > 1 else 0

               line = ""
               for i, w in enumerate(curr_line):
                   if i == len(curr_line) - 1: # last word in line
                       line += w
                       line += (maxWidth - len(line)) * " "
                   else:
                       line += w
                       line += " " if not len(words) else ( eq_sp + (1 if i < remains else 0)) * " "
               
               out.append(line)
           return out
