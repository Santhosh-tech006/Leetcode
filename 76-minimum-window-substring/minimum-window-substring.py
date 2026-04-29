class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        from collections import Counter

        t_count = Counter(t)
        window = {}

        have = 0
        need = len(t_count)

        res = [-1, -1]
        res_len = float("inf")

        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in t_count and window[char] == t_count[char]:
                have += 1

            # Try to shrink window
            while have == need:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Remove left char
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1

        left, right = res
        return s[left:right + 1] if res_len != float("inf") else ""