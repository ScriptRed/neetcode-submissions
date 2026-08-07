class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)

        # Always binary search the smaller array
        if m > n:
            A, B, m, n = B, A, n, m

        total = m + n
        half = total // 2

        l, r = 0, m

        while l <= r:
            i = (l + r) // 2          # partition in A
            j = half - i              # partition in B

            # Boundaries (use ±inf when out of range)
            L1 = A[i-1] if i > 0 else float('-inf')
            R1 = A[i]   if i < m else float('inf')
            L2 = B[j-1] if j > 0 else float('-inf')
            R2 = B[j]   if j < n else float('inf')

            # Correct partition found
            if L1 <= R2 and L2 <= R1:
                if total % 2 == 1:
                    return min(R1, R2)
                return (max(L1, L2) + min(R1, R2)) / 2

            # Move i left
            elif L1 > R2:
                r = i - 1

            # Move i right
            else:
                l = i + 1
