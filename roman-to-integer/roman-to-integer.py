class Solution:
    def romanToInt(self, s: str) -> int:
        intVal, previous = 0, ""
        m = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D": 500, "M": 1000}
        ms = {"I":("V", "X", 1), "X": ("L", "C", 10), "C": ("D", "M", 100)}
        
        for r in reversed(s):
            if previous and (r in ms and previous in ms[r]):
                intVal -= ms[r][2]
            else:
                intVal += m[r]
            previous = r
        return intVal