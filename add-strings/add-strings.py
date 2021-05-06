class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        added = ""
        carryover = 0
        lennum1 = len(num1) - 1
        lennum2 = len(num2) - 1
        while lennum1 >= 0 or lennum2 >= 0:
            d1 = ord(num1[lennum1]) - ord('0') if lennum1 >= 0 else 0
            d2 = ord(num2[lennum2]) - ord('0') if lennum2 >= 0 else 0
            added += str((d1 + d2 + carryover) % 10)
            carryover = (d1 + d2 + carryover) // 10
            lennum1 -= 1
            lennum2 -= 1
        if carryover:
            added += str(carryover)
        return added[::-1]
        #     subtotal1 = ord(d1) + ord(d2) - 48
        #     if subtotal > 57:
        #         subtotal -= 10
        #     added += str(ascii(subtotal)-carryover)
        #     if subtotal > 57:
        #         carryover += 1
        #     numdigits += 1
        # if len(num1) == numdigits:
        #     for d in range()
        
            