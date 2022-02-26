class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n > 0:
            for i in range(len(nums2)): nums1[i] = nums2[i] 

        j, k = m-1, n-1
        for i in range(m+n-1, -1 ,-1):
            if k < 0:
                break
            if j >= 0 and nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1
                
                