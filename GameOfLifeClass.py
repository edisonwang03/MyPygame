class gameoflifegrid():
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.grid = []
        self.newGrid = []
        for r in range(self.rows):
            self.grid.append([])
            self.newGrid.append([])
            for c in range(self.cols):
                self.grid[r].append(0)
                self.newGrid[r].append(0)

    def neighbors(self,r,c):
        neighbor = []
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                if i>=0 and i<self.rows and j>=0 and j<self.cols and (i!=r or j!=c):
                    neighbor.append((i,j))
        return neighbor

    def aliveneighbors(self,r,c):
        alive = 0
        for (row,column) in self.neighbors(r,c):
            alive += self.grid[row][column]
        return alive

    def nextstep(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1:
                    if self.aliveneighbors(r, c) == 2 or self.aliveneighbors(r, c) == 3:
                        self.newGrid[r][c] = 1
                    else:
                        self.newGrid[r][c] = 0
                if self.grid[r][c] == 0:
                    if self.aliveneighbors(r, c) == 3:
                        self.newGrid[r][c] = 1
                    else:
                        self.newGrid[r][c] = 0
        temporaryGrid = self.grid
        self.grid = self.newGrid
        self.newGrid = temporaryGrid
        
    def makeGliderGun(self):
        self.grid[6][5] = 1
        self.grid[6][6] = 1
        self.grid[5][5] = 1
        self.grid[5][6] = 1
        self.grid[5][15] = 1
        self.grid[6][15] = 1
        self.grid[7][15] = 1
        self.grid[8][16] = 1
        self.grid[9][17] = 1
        self.grid[9][18] = 1
        self.grid[4][16] = 1
        self.grid[3][17] = 1
        self.grid[3][18] = 1
        self.grid[4][20] = 1
        self.grid[5][21] = 1
        self.grid[6][21] = 1
        self.grid[7][21] = 1
        self.grid[6][22] = 1
        self.grid[8][20] = 1
        self.grid[6][19] = 1
        self.grid[5][25] = 1
        self.grid[5][26] = 1
        self.grid[4][26] = 1
        self.grid[4][25] = 1
        self.grid[3][25] = 1
        self.grid[3][26] = 1
        self.grid[2][27] = 1
        self.grid[6][27] = 1
        self.grid[2][29] = 1
        self.grid[1][29] = 1
        self.grid[6][29] = 1
        self.grid[7][29] = 1
        self.grid[3][39] = 1
        self.grid[4][39] = 1
        self.grid[4][40] = 1
        self.grid[3][40] = 1