# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            pivot = left + (right - left) // 2
            print(left, right, pivot, isBadVersion(pivot))
            if isBadVersion(pivot):
                right = pivot - 1
            else:
                if left == right:
                    return pivot + 1
                left = pivot + 1
        return pivot
            
            
        