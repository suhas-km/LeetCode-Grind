class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]

            else:
                anagrams[sorted_s].append(s)

        return list(anagrams.values())

        # -----------------------APPROACH 1-----------

        # dic={}
        # k=[]

        # for i in strs:
        #     l="".join(sorted(i))
        #     dic.setdefault(l,[]).append(i)

        # return dic.values()

        # --------------- APPROACH 2 --------------------

        # anagrams = defaultdict(list)

        # for i, v in enumerate(strs):
        #     sorted_str = ''.join(sorted(v))
        #     anagrams[sorted_str].append(v)
        # return list(anagrams.values())

        # -----------------APPROACH 3-----------------------------

    # def groupAnagrams(strs):
        # anagrams = {} # Initialize the hash table
        
        # for s in strs:
        #     # Sort the characters of the string and use it as a key
        #     sorted_s = ''.join(sorted(s))
            
        #     # If the sorted string is not in the hash table, add it
        #     if sorted_s not in anagrams:
        #         anagrams[sorted_s] = [s]
        #     else:
        #         # If it is in the hash table, append the original string to the corresponding list
        #         anagrams[sorted_s].append(s)
        
        # # Return the values of the hash table, which are lists of anagrams
        # return list(anagrams.values())

