class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        xlen = len(image)
        ylen = len(image[0])
        
        visited = set()

        og = image[sr][sc]
        
        def flood(i, j):
            if (i < 0 or j < 0 or i >= xlen or j >= ylen or
                (i,j) in visited or
                image[i][j] == color):
                return image
            
            visited.add((i,j))
            image[i][j] = color
            
            if image[i][j] == og:
                flood(i+1, j)
                flood(i, j+1)
                flood(i-1, j)
                flood(i, j-1)
            
            return image
        
        return flood(sr, sc)
            
                

        