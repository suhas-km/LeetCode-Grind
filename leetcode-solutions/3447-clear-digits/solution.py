class Solution:
    def clearDigits(self, s: str) -> str:
        stck = []

        for i in s:
            if i.isdigit() and stck:
                stck.pop()

            else:
                stck.append(i)
        
        return "".join(stck)

        # for i in s:
        #     stck.append(i)

        #     if i.isdigit():
        #         stck.pop()
        #         stck.pop()
        #     else:
        #         continue

        # return "".join(stck)
