import random
import copy
class MinesweeperTile():
    def __init__(self):
        self.covered = True
        self.mine = False
        self.flagged = False
        self.mineNeighbor = 0
    def key(self):
        if self.flagged:
            return "flagged"
        if self.covered:
            return "covered"
        if not self.mine:
            return str(self.mineNeighbor)
        else:
            return "mine"

class MinesweeperGrid():
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = []
        self.fail = False
        self.success = False
        self.firstClick = True
        for r in range(self.rows):
            self.grid.append([])
            for c in range(self.cols):
                self.grid[r].append(MinesweeperTile())

    def setUpGame(self,row,column):
        minesToBeLaid = self.mines
        while minesToBeLaid > 0:
            r = random.randint(0,self.rows-1)
            c = random.randint(0,self.cols-1)
            if not (r == row and c == column) and self.grid[r][c].mine == False:
                self.grid[r][c].mine = True
                minesToBeLaid -= 1
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c].mineNeighbor = self.mineneighbors(r,c)

    def neighbors(self, r, c):
        neighbor = []
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if i >= 0 and i < self.rows and j >= 0 and j < self.cols and (i != r or j != c):
                    neighbor.append((i, j))
        return neighbor

    def mineneighbors(self,r,c):
        nearbymines = 0
        for (row,column) in self.neighbors(r,c):
            if self.grid[row][column].mine:
                nearbymines += 1
        return nearbymines

    def openTile(self,r,c):
        self.backupGrid = copy.deepcopy(self.grid)
        if self.firstClick:
            self.firstClick = False
            self.setUpGame(r,c)
        if not self.grid[r][c].covered:
            return
        self.grid[r][c].covered = False
        if self.grid[r][c].mine:
            self.fail = True
            for r1 in range(self.rows):
                for c1 in range(self.cols):
                    self.grid[r1][c1].covered = False
            return
        if self.grid[r][c].mineNeighbor == 0:
            for (row, column) in self.neighbors(r, c):
                self.openTile(row,column)


    def flagTile(self,r,c):
        self.backupGrid = copy.deepcopy(self.grid)
        if not self.grid[r][c].covered:
            return
        if self.grid[r][c].flagged:
            self.grid[r][c].flagged = False
        else:
            self.grid[r][c].flagged = True

    def openAllNeighborTiles(self,r,c):
        if not self.grid[r][c].flagged and not self.grid[r][c].covered:
            flaggedCounter = 0
            for (row, column) in self.neighbors(r, c):
                if self.grid[row][column].flagged:
                    flaggedCounter += 1
            if self.grid[r][c].mineNeighbor == flaggedCounter:
                for (row, column) in self.neighbors(r, c):
                    if not self.grid[row][column].flagged and self.grid[row][column].covered:
                        self.openTile(row, column)

    def reverseStep(self):
        self.grid = self.backupGrid
        self.fail = False










