class Solution:
    def countOdds(self, low: int, high: int) -> int:
        oddNums = (high - low) // 2
        if low % 2 != 0 or high % 2 != 0:
            oddNums += 1
        return oddNums
        

            
        