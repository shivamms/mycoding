class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n = len(a), len(b)
        if m == 1 and n == 1 and a[0] == "0" and b [0] == "0":
            return "0"
        result, dec1, dec2 = "", 0,0
        i,j = 0,0
        a,b = a[::-1], b[::-1]
        while i < m:
            dec1 += (ord(a[i])-48) * (2 ** i)
            i += 1
        while j < n:
            dec2 += (ord(b[j])-48) * (2 ** j)
            j += 1
        dec1 += dec2
        while dec1 >= 1:
            result += str(dec1 % 2)
            dec1 //= 2
        return result[::-1]