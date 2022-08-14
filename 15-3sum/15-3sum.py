class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#         def twoSum(nums, target):
#             hashmap = {}
#             for i in range(len(nums)):
#                 if target - nums[i] in hashmap:
#                     return hashmap[target - nums[i]], i
#                 else:
#                     hashmap[nums[i]] = i
#             return None, None
        
#         result = []
#         for i in range(len(nums)):
#             j, k = twoSum(nums[:i]+nums[i+1:], 0-nums[i])
#             if j is not None and k is not None:
#                 result.append(sorted([nums[i], nums[j], nums[k]]))
#         return [list(r) for r in {(r[0],r[1],r[2]) for r in result}]

        def twoSumII(nums, i, result):
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]: # to aovid duplicates
                twoSumII(nums, i, result)
        return result
            