class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ## to aovid division by zero, do not use straight forward formula of 
        ## finding slope i.e. y2-y1 / x2-x1
        ## instead use x difference dx = x2-x1 and y difference dy = y2-y1 of first point and 
        ## check if the x difference * dy and y difference * dx is equal for all the subsequent
        ## points
        n = len(coordinates)
        dx = coordinates[1][0]-coordinates[0][0]
        dy = coordinates[1][1]-coordinates[0][1]
        for i in range(1, n-1):
            if dy * (coordinates[i+1][0]-coordinates[i][0]) !=  dx * (coordinates[i+1][1]-coordinates[i][1]):
                return False
        return True