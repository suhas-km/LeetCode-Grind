# class ProductOfNumbers:

#     def __init__(self):
#         self.lst = [] # initialize with an empty stream
#         self.result = [] # to keep track of prefix multiples

#     def add(self, num: int) -> None:
#         self.lst.append(num) # append num into lst

#         if len(self.lst) == 1: # start prefix product for lst
#             self.result.append(num)
        
#         else:
#             for i in self.lst: # prefix product for lst
#                 self.result.append(self.result[i-1] * self.lst[i])
#             return self.result

#     def getProduct(self, k: int) -> int:
#         if len(self.lst) == 1: # if first element
#             return self.lst[0]

#         elif len(self.lst) >= k: # find the prefix product of k integers from the lst
#             return // need help here
            

# # Your ProductOfNumbers object will be instantiated and called as such:
# # obj = ProductOfNumbers()
# # obj.add(num)
# # param_2 = obj.getProduct(k)
class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]  # Initialize with 1 as the multiplicative identity

    def add(self, num: int) -> None:
        if num == 0:
            # A zero resets the product chain
            self.prefix = [1]
        else:
            # Append the new product based on the last prefix value
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is larger than the current prefix chain length,
        # it means there was a zero within the last k elements.
        if k >= len(self.prefix):
            return 0
        # The product of the last k numbers is the ratio of the current
        # cumulative product to the product before these k numbers.
        return self.prefix[-1] // self.prefix[-k - 1]

