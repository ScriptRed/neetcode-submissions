class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        tot = (m-1) + (n-1)
        return (math.factorial(tot) // (math.factorial(tot - (n-1)) * math.factorial(n-1)))