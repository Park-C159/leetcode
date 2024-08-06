from typing import List, Optional
from collections import deque

from binarytree import Node


def average_of_levels(root: Optional[Node]) -> List[float]:
    queue = deque([root])
    result = []

    while queue:
        layer_len = len(queue)
        level_sum = 0
        for _ in range(layer_len):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum / layer_len)

    return result
