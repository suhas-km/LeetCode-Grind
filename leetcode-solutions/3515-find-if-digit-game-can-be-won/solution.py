class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        """
        """
        dSum = 0 
        sSum = 0

        for num in nums:
            if num > 9:
                dSum += num
            else:
                sSum += num
        
        return dSum != sSum

