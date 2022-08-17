class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # result, m, n, left, right = 0, len(num1), len(num2), 0, 0
        # num1, num2 = num1[::-1], num2[::-1]
        # i, j = 0, 0
        # while i < m:
        #     left += (ord(num1[i])-48) * (10 ** i)
        #     i += 1
        # while j < n:
        #     right += (ord(num2[j])-48) * (10 ** j)
        #     j += 1
        # return str(left * right)
        #subsum school method
        result, m, n = 0, len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        subSum = 0
        for i in range(m):
            num = ord(num1[i])-48
            for j in range(n):
                stepSum = (ord(num2[j])-48) * (10 ** j) * num
                subSum += stepSum
            subSum *= (10 ** i)
            result += subSum
            subSum = 0
        return str(result)