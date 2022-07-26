class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        r = len(image)
        c = len(image[0])
        principale = image[sr][sc]
        if color == principale:
            return image

        def f(i,j):
            if image[i][j] != color:
                image[i][j] = color
            if i+1 >= 0 and j >= 0 and i+1<r and j < c and image[i+1][j]==principale :
                f(i+1,j)
            if   i-1 >= 0 and j >= 0 and i-1<r and j < c and image[i-1][j]==principale:
                f(i-1,j)
            if  i >= 0 and j-1 >= 0 and i<r and j-1 < c and image[i][j-1]==principale:
                f(i,j-1)
            if  i >= 0 and j+1 >= 0 and i<r and j+1 < c and image[i][j+1]==principale:
                f(i,j+1)
        
        f(sr,sc)
        return image