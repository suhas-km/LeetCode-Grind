class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # time: o(n)
        # space: o(1)

        product = 1

        for num in nums:
            product *= num
        
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0

        return signFunc(product)
