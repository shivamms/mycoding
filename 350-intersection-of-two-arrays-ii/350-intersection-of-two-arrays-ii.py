class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # simple method
        m, n = len(nums1), len(nums2)
        result = []
        if m > n:
            numsSet = Counter(nums1)
            nums = nums2
        else:
            numsSet = Counter(nums2)
            nums = nums1
        for num in (nums):
            if num in numsSet and numsSet[num] > 0:
                numsSet[num] -= 1
                result.append(num)
        return result
        
        