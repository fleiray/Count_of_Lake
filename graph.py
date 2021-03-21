import numpy as np
import matplotlib.pyplot as plt
from matplotlib.table import Table

graph = np.array([[1, 1, 0, 0, 0],
                  [0, 1, 0, 0, 1],
                  [1, 0, 0, 1, 1],
                  [0, 0, 1, 1, 0],
                  [1, 0, 1, 0, 1]])
fig,ax=plt.subplots(figsize=(6,6))
tb = Table(ax)
#cellText and cellColours
nrows, ncols = len(graph),len(graph)
width, height = 1.0 / ncols, 1.0 / nrows   
for (i,j),val in np.ndenumerate(graph):
    tb.add_cell(i, j, width, height)
    tb.add_cell(i, j, width, height, loc='center')


# tb.auto_set_font_size(False)
# tb.set_fontsize(15)
ax.add_table(tb)
ax.set_aspect('equal')
plt.axis("off")
plt.show()