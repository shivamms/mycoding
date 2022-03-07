class Solution:
    def interpret(self, command: str) -> str:
        cmd = intrep = '' 
        for c in command:
            cmd += c
            if cmd in ('G', '()', '(al)'):
                if cmd == '()': cmd = 'o'
                if cmd == '(al)': cmd = 'al'
                intrep += cmd
                cmd = ''
        return intrep
                