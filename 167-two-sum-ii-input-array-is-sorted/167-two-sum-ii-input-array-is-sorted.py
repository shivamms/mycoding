class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] == target - numbers[j]:
                return [i+1,j+1]
            elif numbers[i] < target - numbers[j]:
                i += 1
            elif numbers[i] > target - numbers[j]:
                j -= 1