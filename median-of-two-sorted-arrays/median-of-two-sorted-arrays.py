class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            median_index = [int(length / 2) - 1, int(length / 2)]
        else:
            median_index = [int(length / 2)]
        combined = []
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] <= nums2[0]:
                combined.append(nums1[0])
                del nums1[0]
                if len(nums1) > 0 and len(nums2) > 0 and nums1[0] <= nums2[0]:
                    combined.append(nums1[0])
                    del nums1[0]
                else:
                    combined.append(nums2[0])
                    del nums2[0]
            else:
                combined.append(nums2[0])
                del nums2[0]
                if len(nums1) > 0 and len(nums2) > 0 and nums2[0] <= nums1[0]:
                    combined.append(nums2[0])
                    del nums2[0]
                else:
                    combined.append(nums1[0])
                    del nums1[0]
        if len(nums1) > 0:
            combined = combined + nums1
        elif len(nums2) > 0:
            combined = combined + nums2
        if len(median_index) == 1:
            median = combined[median_index[0]]
        else:
            median = ((combined[median_index[0]] + combined[median_index[1]]) * 1.0) / 2
        return median
        