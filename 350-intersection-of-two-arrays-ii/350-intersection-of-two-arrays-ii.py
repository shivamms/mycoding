class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ## simple method
        # m, n = len(nums1), len(nums2)
        # result = []
        # if m > n:
        #     numsSet = Counter(nums1)
        #     nums = nums2
        # else:
        #     numsSet = Counter(nums2)
        #     nums = nums1
        # for num in (nums):
        #     if num in numsSet and numsSet[num] > 0:
        #         numsSet[num] -= 1
        #         result.append(num)
        # return result
        
        ## sorting method to avoid extra space - Two pointer
        nums1.sort()
        nums2.sort()
        i = j = 0
        output = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                output.append(nums2[j])
                i += 1
                j += 1
        return output
                
        
        
        