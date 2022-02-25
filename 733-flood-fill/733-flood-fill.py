class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        def fill(r,c):
            if r < 0 or r > m-1 or c < 0 or c > n-1:
                return
            if (r,c) not in visited:
                visited.add((r,c))
                if image[r][c] == oldColor:
                    image[r][c] = newColor
                    fill(r+1,c)
                    fill(r-1,c)
                    fill(r, c+1)
                    fill(r, c-1)
        fill(sr,sc)
        return image