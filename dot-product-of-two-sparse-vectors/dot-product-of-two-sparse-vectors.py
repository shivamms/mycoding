class SparseVector:
    def __init__(self, nums: List[int]):
        self.ht = {i:val for i, val in enumerate(nums) if val > 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum = 0
        length1 = len(self.ht)
        length2 = len(vec.ht)
        if length1 <= length2:
            for key, val in self.ht.items():
                if key in vec.ht.keys():
                    sum += val * vec.ht[key]
        else:
            for key, val in vec.ht.items():
                if key in self.ht.keys():
                    sum += val * self.ht[key]
        return sum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)