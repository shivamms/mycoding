class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        comp = defaultdict(int)
        result = 0
        for secs in time:
            rem = secs % 60
            if rem != 0:
                result += comp[60-rem]
            elif rem == 0:
                result += comp[0]
            comp[rem] += 1   
        return result