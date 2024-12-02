class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for c in s:
            # Pattern is still being aggregated
            # ] marks end of pattern
            # We never push ] into stack
            if c != "]":
                st.append(c)
                continue

            # Extract latest pattern in reverse order
            buffer = []
            while len(st) > 0 and st[-1] != '[':
                buffer.append(st.pop())

            # Extract multiplier
            m = 1
            if len(st) > 0 and st[-1] == '[':
                # Discard [
                st.pop()
                m = extractMultiplier(st)

            # Reappend pattern multiplied by multiplier
            st.append(m*''.join(buffer[::-1]))

        # Flush out the stack pass the extracted 
        # patterns through buffer for multiplication
        buffer = []
        while len(st) > 0:
            if st[-1] == '[':
                # Discard [
                st.pop()

                # extract multiplier
                m = extractMultiplier(st)
                st.append(m*''.join(buffer[::-1]))
            else:
                buffer.append(st.pop())

        return ''.join(buffer[::-1])

def extractMultiplier(st):
    x = []
    while len(st) > 0 and st[-1].isdigit():
        x.append(st.pop())
    return 1 if x == '' else int(''.join(x[::-1]))
