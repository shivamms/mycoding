class Solution:
    # from collections import Counter, defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
    #     set1 = Counter(s1)
    #     l = len(s1)
    #     set2 = Counter(s2[:l])
    #     set2 = defaultdict(int, set2)
    #     remove = 0
    #     for i in range(l,len(s2)):
    #         if set1 == set2:
    #             return True
    #         set2[s2[remove]] -= 1
    #         if set2[s2[remove]] <= 0:
    #             set2.pop(s2[remove])
    #         set2[s2[i]] += 1
    #         remove += 1
    #     return set1 == set2
        m, n = len(s1), len(s2)
        if m > n:
            return False
        count = Counter(s1)
        for i in range(m):
            if s2[i] in count:
                count[s2[i]] -= 1
        if min(count.values()) == 0 and max(count.values()) == 0:
                return True
        start, end = 1, m
        while end < n:
            if s2[start-1] in count:
                count[s2[start-1]] += 1
            if s2[end] in count:
                count[s2[end]] -= 1
            if min(count.values()) == 0 and max(count.values()) == 0:
                return True
            start += 1
            end += 1
        return False        
    
                
            