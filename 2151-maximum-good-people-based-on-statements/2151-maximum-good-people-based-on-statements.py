class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        ans = 0
        mask = [0]*n
        true = [0]*n
        for i in range(n):
            for j in range(n):
                if statements[i][j] == 1:
                    true[i] |= 1<<j
                if statements[i][j] != 2:
                    mask[i] |= 1<<j
                    

        def consistent(cur):
            for i in range(n):
                if cur & 1 << i:
                    if (cur ^ true[i]) & mask[i]: return False
            return True;
        
        for i in range(1 << n):
            l = bin(i).count('1')
            if l > ans:
                if consistent(i): ans = l
        return ans
        