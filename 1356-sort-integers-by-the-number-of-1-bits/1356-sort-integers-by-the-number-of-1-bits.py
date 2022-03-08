class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bits = []
        for num in arr:
            bits.append((Counter(str(bin(num)))["1"], num))
        bits.sort(key = lambda p: (p[0],p[1]))
        return [p[1] for p in bits]
        