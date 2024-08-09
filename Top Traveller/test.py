import pandas as pd
from top_traveller import *

data = [
    [1, 'Alice'],
    [2, 'Bob'],
    [3, 'Alex'],
    [4, 'Donald'],
    [7, 'Lee'],
    [13, 'Jonathan'],
    [19, 'Elvis']]
users = pd.DataFrame(data, columns=['id', 'name']).astype(
    {'id': 'Int64', 'name': 'object'})
data = [[1, 1, 120],
        [2, 2, 317],
        [3, 3, 222],
        [4, 7, 100],
        [5, 13, 312],
        [6, 19, 50],
        [7, 7, 120],
        [8, 19, 400],
        [9, 7, 230]]
rides = pd.DataFrame(data, columns=['id', 'user_id', 'distance']).astype(
    {'id': 'Int64', 'user_id': 'Int64', 'distance': 'Int64'})

res = top_traveller_simple(users, rides)
# print(res)
