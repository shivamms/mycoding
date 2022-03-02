class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n, oddSum = len(arr), 0
        for i in range(n-1, -1, -1):
            start, end = i-2, i+1
            while start >= 0:
                if (end - start) % 2 != 0: oddSum += sum(arr[start:end])
                start -= 1
        oddSum += sum(arr)
        return oddSum
                
                
                