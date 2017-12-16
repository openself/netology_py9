import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.vq import whiten, kmeans2


DATA_FILE = r'Premier League 16-17.xlsx'

df = pd.read_excel(DATA_FILE, usecols=[5, 12])
# print(df.info())
# print(df.head())
#
# df.plot.scatter(x='Total market value, m of  £', y='L', s=100)
# plt.show()

whitened = whiten(df.as_matrix())
# print(whitened)

centroids, cluster_map = kmeans2(whitened, 5)
print(centroids, cluster_map)

colors_map = {0: 'r', 1: 'g', 2: 'b', 3: 'y', 4: 'm'}
colors_list = [colors_map[c] for c in cluster_map]
# print(colors)

df.plot.scatter(x='Total market value, m of  £', y='L', s=100, color=colors_list)
plt.ylabel('Losses')
plt.show()