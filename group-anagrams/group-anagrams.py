class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hashmap = defaultdict(list)
        for s in strs:
            hashmap[''.join(sorted(s))].append(s)
        return [val for key,val in hashmap.items()]