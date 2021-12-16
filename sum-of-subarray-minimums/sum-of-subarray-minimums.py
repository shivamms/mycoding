class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        length = len(arr)
        left = [1] * length
        right = [1] * length
        for i in range(length):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack[-1][1]
                stack.pop()
            stack.append((arr[i], count))
            left[i] = count

        stack = []
        for i in range(length-1, -1, -1):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack[-1][1]
                stack.pop()
            stack.append((arr[i],count))
            right[i] = count
        sum = 0
        for i in range(length):
            sum = (sum % (10**9 + 7)) + ((left[i] % (10**9 + 7)) * (right[i] % (10**9 + 7)) * (arr[i] % (10**9 + 7)))
        return sum
        