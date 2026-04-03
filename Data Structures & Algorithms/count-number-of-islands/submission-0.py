class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        self.gridRow = len(grid)
        self.gridCol = len(grid[0])

        islandNo = 0
        for i in range(self.gridRow):
            for j in range(self.gridCol):
                if (grid[i][j] == "1"):
                    islandNo += 1
                    self.dfsIslands(grid, i, j)

        return islandNo
        
    
    def dfsIslands(self, grid: List[List[str]], row: int, col: int) -> None:
        if row < 0 or col < 0 or row >= self.gridRow or col >= self.gridCol or grid[row][col] != "1":
            return
        grid[row][col] = '0'

        self.dfsIslands(grid, row + 1, col)
        self.dfsIslands(grid, row - 1, col)
        self.dfsIslands(grid, row, col + 1)
        self.dfsIslands(grid, row, col - 1)
        