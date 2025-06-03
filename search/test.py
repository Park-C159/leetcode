from dfs import dfs
from bfs import bfs

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

dfs(tree, "A", "D")
print()
bfs(tree, "A", "E")