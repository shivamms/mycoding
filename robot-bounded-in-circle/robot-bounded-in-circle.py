class Solution(object):
    def isRobotBounded(self, instructions):
        movmap = [(0,0,1), (1,1,0), (2,0,-1), (3, -1,0)]
        pos = [0,0]
        currentDir = 0
        x, y = 0, 0
        for i in range(4):
            for inst in instructions:
                x = movmap[currentDir][1]
                y = movmap[currentDir][2]
                if inst == 'G':
                    pos[0] += x
                    pos[1] += y
                elif inst == 'L':
                    currentDir += 3
                elif inst == 'R':
                    currentDir += 1
                if currentDir > 3:
                        currentDir -= 4
        return pos[0] == pos[1] == 0