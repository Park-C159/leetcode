from collections import deque

def bfs(tree, start, goal=None):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()
        if node == goal:
            print(node, end=" ")
            return True
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(tree[node])


def bfs_graph(matrix, start):
    n = len(matrix)
    visited = [False] * n
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")
            for neighbor in range(n):
                if matrix[node][neighbor] and not visited[neighbor]:
                    queue.append(neighbor)