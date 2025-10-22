class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # Partition index for A
            j = half - i - 2  # Partition index for B (adjusted for 0-based indexing)

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # Correct partition found
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  # Odd total length
                    return min(Aright, Bright)
                else:  # Even total length
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
