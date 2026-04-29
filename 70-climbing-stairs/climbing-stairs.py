class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        prev1 = 1  # ways to reach step 1
        prev2 = 2  # ways to reach step 2

        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr

        return prev2