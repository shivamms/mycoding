class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## using built-in function
        # m, n = len(s1), len(s2)
        # count1 = Counter(s1)
        # for i in range(n-m+1):
        #     if count1 == Counter(s2[i:i+m]):
        #         return True
        # return False
        
        ## faster way
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
                