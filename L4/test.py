import json
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

with open("traversals.json", 'r') as f:
    data = json.load(f)

p = [0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 4, 4, 4, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0]
q = [0, 1, 1, 2, 2, 2, 5, 2, 3, 3, 4, 4, 4, 4, 5, 4, 4, 4, 6, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 3, 5, 5, 5, 5, 5, 4, 4, 4, 4, 2, 4, 3, 2, 1, 0, 2, 2, 2, 1, 1, 1, 1, 2, 4, 3, 3, 4, 4, 7, 5, 5, 5, 4, 4, 3, 3, 2, 2, 1, 2, 2, 5, 2, 2, 3, 3, 4, 4, 5, 5, 5, 4, 4, 6, 3, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 0, 0]
fig = plt.figure(figsize=(15, 9))
plt.plot(p, label="linia A")
plt.plot(q, label="linia B")
plt.grid(True)
plt.legend(fontsize=16)
plt.savefig("test.png", dpi=300)

mat = np.corrcoef(np.array(p), np.array(q))
print(mat[0, 1])

pp = pd.Series(p).corr(pd.Series(q))
print(pp)