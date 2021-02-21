class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        strrep = []
        five = False
        three = False
        for i in range(1,n+1):
            five = i % 5
            three = i % 3
            if five == 0 and three == 0:
                strrep.append('FizzBuzz')
            elif five == 0:
                strrep.append('Buzz')
            elif three == 0:
                strrep.append('Fizz')
            else:
                strrep.append(str(i))
        return strrep
                