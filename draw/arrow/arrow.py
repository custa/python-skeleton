import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca()
ax.xaxis.set_ticks_position('top')
ax.invert_yaxis()
plt.plot([0, 100], [0, 200])
ax.arrow(99, 199, 100, 200, head_width=10, head_length=1, fc='k', ec='k')
plt.show()
