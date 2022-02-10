class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        output = []
        for num in nums2:
            if num in count:
                count[num] -= 1
                output.append(num)
                if count[num] == 0:
                    del count[num]
        return output
        
        