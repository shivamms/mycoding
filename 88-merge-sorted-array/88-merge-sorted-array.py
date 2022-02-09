class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0 and m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n > 0 and m > 0:
            temp = []*(m+n)
            i = j = 0
            while i < m and j < n:
                if nums1[i] < nums2[j]:
                    temp.append(nums1[i])
                    i += 1
                else:
                    temp.append(nums2[j])
                    j += 1
            if i < m:
                temp += nums1[i:]
            elif j < n:
                temp += nums2[j:]
            print(temp)
            for i in range(m+n):
                nums1[i] = temp[i]
                
        