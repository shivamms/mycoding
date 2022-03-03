class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCount = Counter(magazine)
        ransomCount = Counter(ransomNote)
        for key,val in ransomCount.items():
            if key not in magazineCount or magazineCount[key] < val:
                return False
        return True
                