# Given array of strings, group the stings that have the same letters

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # map character count to list of anagrams
        
        for s in strs: # For each string in the list...
            count = [0] * 26 # 26 zeros, a - z 

            for c in s: # For each character in the string...
                count[ord(c) - ord("a")] += 1 # 

            res[tuple(count)].append(s)

        return res.values()