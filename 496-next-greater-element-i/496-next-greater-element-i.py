class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greaterNums = dict()
        stack = deque()
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[0]:
                greaterNums[stack.popleft()] = nums2[i]
            stack.appendleft(nums2[i])
        while stack:
                greaterNums[stack.popleft()] = -1
        result = []

        return [greaterNums[nums1[i]] for i in range(len(nums1))]
