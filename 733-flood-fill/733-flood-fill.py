class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        oldColor = image[sr][sc]
        n, m = len(image), len(image[0])
        def fillColor(r, c, nc, oc, visited):
            if r < 0 or r > n-1 or c < 0 or c > m-1 or image[r][c] != oc:
                return
            visited.add((r,c))
            image[r][c] = nc
            if (r+1,c) not in visited and r+1 <= n-1 and image[r+1][c] == oc:
                fillColor(r+1, c, nc, oc, visited)
            if (r-1, c) not in visited and r-1 >= 0  and image[r-1][c] == oc:
                fillColor(r-1, c, nc, oc, visited)
            if (r, c+1) not in visited and c+1 <= m-1 and image[r][c+1] == oc:
                fillColor(r, c+1, nc, oc, visited)
            if (r, c-1) not in visited and c-1 >= 0 and image[r][c-1] == oc:
                fillColor(r, c-1, nc, oc, visited)
            return 
        
        fillColor(sr, sc, newColor, oldColor, visited)
        return image
            
        