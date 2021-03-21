import numpy as np
import matplotlib.pyplot as plt
from matplotlib.table import Table

class Graph:

    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    # A function to check if a given cell (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number is in range and value is 1 and not yet visited
        safe = False
        if (i >= 0 and i < self.ROW and j >= 0 and j < self.COL and not visited[i][j] and self.graph[i][j] == 0):
            safe = True

        return safe

    # A utility function to do DFS for a 2D boolean matrix. It only considers the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited, output, count):
        # These arrays are used to get row and column numbers of 8 neighbours of a given cell
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]
        visited[i][j] = True
        output[i][j] = count+1
        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited,output, count)
    # The main function that returns count of islands in a given boolean 2D matrix

    def countIslands(self):
        # Make a bool array to mark visited cells. Initially all cells are unvisited
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
        output = [[0 for j in range(self.COL)]for i in range(self.ROW)]
        # Initialize count as 0 and travese through the all cells of given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet, then new island found
                if visited[i][j] == False and self.graph[i][j] == 0:
                    # Visit all cells in this island and increment island count
                    self.DFS(i, j, visited, output, count)
                    count += 1
        return count, output


graph = [[1, 0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 1, 0, 1],
         [1, 1, 1, 1, 0, 0, 1],
         [1, 0, 0, 1, 0, 1, 0],
         [1, 0, 1, 1, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 1],
         [0, 0, 0, 1, 0, 1, 1],
         [0, 0, 0, 1, 0, 0, 1],
         [1, 0, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 0, 0, 0]]
         
row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

count, output = g.countIslands()
output_as_array = np.array(output)
print("Corresponding output Matrix")
print(output_as_array)
print("Number of Lake is:")
print(count)

fig,ax=plt.subplots(figsize=(6,6))
tb = Table(ax)
nrows, ncols = len(output_as_array),len(output_as_array)
width, height = 1.0 / ncols, 1.0 / nrows   
for (i,j),val in np.ndenumerate(output_as_array):
    tb.add_cell(i, j, width, height)
    tb.add_cell(i, j, width, height, loc='center')
for i in range(row):
    for j in range(col):
        if(output[i][j]!=0):
            tb[(i,j)].set_facecolor("#56b5fd")
            tb[(i,j)].set_text_props(text=output[i][j])
        else:
            tb[(i,j)].set_facecolor("grey")       
ax.add_table(tb)
ax.set_aspect('equal')
plt.axis("off")

plt.savefig('output.jpg')
plt.show()