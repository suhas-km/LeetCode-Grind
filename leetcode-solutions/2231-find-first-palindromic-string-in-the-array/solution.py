class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = ''
        
        for word in words:
            if word == word[::-1]:
                ans += word
                break
        return ans

        # for word in words:
        #     l, r = 0, len(word) - 1
        #     while word[l] == word[r]:
        #         l += 1
        #         r -= 1
        #         if l >= r:
        #             return word

        # return ""
