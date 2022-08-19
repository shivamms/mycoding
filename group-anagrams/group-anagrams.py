class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # using sorting
        # hashmap = defaultdict(list)
        # for s in strs:
        #     hashmap[''.join(sorted(s))].append(s)
        # return [val for key,val in hashmap.items()]
    
        # using direct access array 
        hashmap  = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            hashmap[tuple(count)].append(s)
        return [val for key,val in hashmap.items()]
        