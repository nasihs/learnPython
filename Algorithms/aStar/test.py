OBSTACLE = [(x, 0) for x in range(7)] + [(0, y) for y in range(7)]
#print(OBSTACLE)

parent_node = {(1, 0): (2, 3)}
print(parent_node)
parent_node[(2, 0)] = (6, 6)
# print(parent_node[(2, 0)])
print(parent_node)