def dfs(tree, start, end=None):
    stack = [start]
    visited = set()  # 环专用

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            if end is None:
                visited.add(node)
                stack.extend(reversed(tree[node]))
            else:
                if node == end:
                    return True
                else:
                    visited.add(node)
                    stack.extend(reversed(tree[node]))


# 示例调用
def dfs_graph(matrix, node, visited2):
    visited2[node] = True
    print(node, end=" ")

    for neighbor, is_connected in enumerate(matrix[node]):
        if is_connected and not visited2[neighbor]:
            dfs_graph(matrix, neighbor, visited2)