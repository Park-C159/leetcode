from binarytree import Node
from collections import deque
from typing import List

root1 = Node(3)
root1.left = Node(9)
root1.right = Node(20)
root1.right.left = Node(15)
root1.right.right = Node(7)

root2 = Node(3)
root2.left = Node(9)
root2.left.left = Node(15)
root2.left.right = Node(7)
root2.right = Node(20)

from average_of_levels import *

print(average_of_levels(root1))
# print(average_of_levels(root2))