# 示例调用
from dfs import dfs_graph
from bfs import bfs_graph

matrix = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
n = len(matrix)
visited = [False] * n
dfs_graph(matrix, 0, visited)
print()
bfs_graph(matrix, 0)
# 输出: 0 1 2