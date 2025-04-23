import numpy as np
import matplotlib.pyplot as plt
from ortools.sat.python import cp_model

board_size = 4

model = cp_model.CpModel()

# The array index represents the column, and the value is the row.
queens = [
    model.new_int_var(0, board_size - 1, f'x{i}') for i in range(board_size)
]

# constraint: all rows must be different
model.add_all_different(queens)
model.add_all_different(queens[i] + i for i in range(board_size))
model.add_all_different(queens[i] - i for i in range(board_size))

solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = False
solver.Solve(model)

# constraint: no two queens can be on the same diagonal
all_queens = range(board_size)
state = []
for i in all_queens:
    for j in all_queens:
        if solver.Value(queens[j]) == i:
            # queen in row i and column j
            state.append(True)
        else:
            state.append(None)

states = np.array(state).reshape(-1, board_size)
fig = plt.figure(figsize=(5, 5))
markers = [
    x.tolist().index(True) if True in x.tolist() else None for x in np.transpose(states)
]

res = np.add.outer(range(board_size), range(board_size)) % 2
plt.imshow(res, cmap='binary_r')
plt.xticks([])
plt.yticks([])
plt.plot(markers, marker="*", linestyle="None", markersize=100/board_size, color="y")
plt.show()
