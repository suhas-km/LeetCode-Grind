class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the length of both strings aren't equal then they arent anagrams. return false.
        if len(s)!=len(t): 
            return False
        
        init=set();#declare a new set
        
        for letter in s:#for every letter in the string s
            if letter not in init:#if the letter is not there in the new set
                init.add(letter)#add the letter to the new set
                
                if s.count(letter)!=t.count(letter): 
                    return False
                #if the no of letters in not the same in both strings s and t, return False.
                #else return True.
        return True
