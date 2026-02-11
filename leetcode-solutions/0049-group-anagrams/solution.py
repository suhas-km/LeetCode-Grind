from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        # SORTING APPROACH
        # for word in strs:
        #     sorted_key = "".join(sorted(word))
        #     seen[sorted_key].append(word)
        
        # return list(seen.values())

        # time: n. K logk, where k is the total number of strings in the strs array
        # space: n.k, to strore both groups in the hashmap

        # [1, 0, 0, 0, 1, .... 1, 0000] -> len -> 26
        


        for word in strs:
            key = [0] * 26
            # logic to prepare the key
            for ch in word:
                key[ord(ch) - ord('a')] += 1

            anagrams[tuple(key)].append(word) # cant store list as key in hashmap
        
        res = []
        for key, value in anagrams.items():
            res.append(value)
        
        return res

        # time: O (n * k), where k is the average length of each string
        # space: O(n)

