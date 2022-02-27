class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            # if target numbers[j] == 0 and :
            #     return [j+1,j+1]
            if numbers[i] == target - numbers[j]:
                return [i+1,j+1]
            elif numbers[i] < target - numbers[j]:
                i += 1
            elif numbers[i] > target - numbers[j]:
                j -= 1