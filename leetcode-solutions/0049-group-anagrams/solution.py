class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # Initialize the hash table
        
        for s in strs:
            # Sort the characters of the string and use it as a key
            sorted_s = ''.join(sorted(s))
            
            # If the sorted string is not in the hash table, add it
            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]
            else:
                # If it is in the hash table, append the original string to the corresponding list
                anagrams[sorted_s].append(s)
        
        # Return the values of the hash table, which are lists of anagrams
        return list(anagrams.values())
        
        

### SOLUTION 2 ####
#         res = defaultdict(list) 

#         for s in strs:
#             count = [0] * 26 #a...z - array for the 26 charecters

#             for c in s:
#                 count[ord(c) - ord("a")] += 1

#             res[tuple(count)].append(s)

#         return res.values()
