class Solution:
    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     x,y='',''
    #     bs_count = 0
    #     for c in s[::-1]:
    #         if c == '#':
    #             bs_count += 1
    #         elif bs_count:
    #             bs_count -= 1
    #         else:
    #             x += c
    #     bs_count = 0
    #     for c in t[::-1]:
    #         if c == '#':
    #             bs_count += 1
    #         elif bs_count > 0:
    #             bs_count -= 1
    #         else:
    #             y += c
    #     return x == y
    def backspaceCompare(self, S, T):
        def F(s):
            skip = 0
            for c in reversed(s):
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
