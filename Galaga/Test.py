# from Enemies.butterfly_class import Butterfly

# thing = Butterfly()


import numpy as np

test = np.array(
    [[0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]]
)
result = np.argwhere(test == 1)

print(result[0][0])
print(result[0][1])