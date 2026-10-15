class Solution(object):
    def firstUniqChar(self, s):
        ch = {}

        # Step 1: Count each character
        for c in s:
            if c in ch:
                ch[c] += 1
            else:
                ch[c] = 1

        # Step 2: Find the first unique character
        for i in range(len(s)):
            if ch[s[i]] == 1:
                return i

        # Step 3: No unique character found
        return -1
        