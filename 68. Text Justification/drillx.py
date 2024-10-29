# Accepted
# submitted at Oct 28, 2024 14:34
# Runtime Beats 100.00%
# Memory Beats 23.49%

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Split the words into lines
        lines:List[List[str]] = []
        currLineLen = 0
        for word in words:
            # If the word does not fit on the current line, create a new line
            if len(lines) == 0 or (maxWidth - currLineLen) < len(word):
                lines.append([])
                currLineLen = 0

            lines[-1].append(word)
            # +1 to account for a space between word and next one
            currLineLen += len(word) + 1

        # For each line, we need to:
        linesfmted = []
        for i in range(len(lines) - 1):
            line, fmted = lines[i], ""
            slotsBetWords = len(line) - 1
            numChars = sum(len(word) for word in line) 
            numSpaces = maxWidth - numChars
            if len(line) == 1: # left justify if one word
                fmted = line[0] + ' ' * numSpaces
            else: # else distribute the extra spaces evenly
                spacesPerSlot, extraSpaces  = numSpaces // slotsBetWords, numSpaces % slotsBetWords
                for i in range(len(line) - 1):
                    fmted += line[i]
                    fmted += ' ' * (spacesPerSlot + (1 if i < extraSpaces else 0))
                # Handle last element separately to avoid trailing spaces
                fmted += line[-1]

            linesfmted.append(fmted)

        # Format the last line
        numChars = sum(len(word) for word in lines[-1]) + len(lines[-1]) - 1
        linesfmted.append(" ".join(lines[-1]) + " "*(maxWidth - numChars))
        return linesfmted
