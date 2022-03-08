class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted([num for num in arr], key=lambda x:(bin(x).count("1"),x))
        # bits = []
        # for num in arr:
        #     bits.append((Counter(str(bin(num)))["1"], num))
        # bits.sort(key = lambda p: (p[0],p[1]))
        # return [p[1] for p in bits]
        