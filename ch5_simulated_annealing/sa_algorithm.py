import math
import random

# Inspired by: https://www.geeksforgeeks.org/dsa/implement-simulated-annealing-in-python/


def simulated_annealing(objective, bounds, iterations, step_size, temp):
    best = [random.uniform(bound[0], bound[1]) for bound in bounds]
    best_eval = objective(best)
    current = best
    current_eval = best_eval
    scores = [best_eval]

    for i in range(iterations):
        # decrease temperature
        t = temp / float(i + 1)

        # Candidate Solution
        candidate = get_neighbor(current, step_size)
        candidate_eval = objective(candidate)

        # Keep the current solution?
        if candidate_eval < best_eval or random.random() < math.exp((current_eval - candidate_eval) / t):
            current, current_eval = candidate, candidate_eval

            if candidate_eval < best_eval:
                best, best_eval = candidate, candidate_eval
                scores.append(best_eval)

        # Print progress
        if i % 100 == 0:
            print(f"{i: 4d}: Temperature: {t:.3f}, Best evaluation: {best_eval:.5f}")

    return best, best_eval, scores



# Example
def rastrigin_function(x):
    return 10 * len(x) + sum([(xi**2 - 10 * math.cos(2 * math.pi * xi)) for xi in x])

def get_neighbor(current, step_size=0.1):
    neighbor = current[:]
    idx = random.randint(0, len(current) - 1)
    neighbor[idx] += random.uniform(-step_size, step_size)
    return neighbor


# Problem domain

# 2-dimensional Rastrigin function
bounds = [(-5.0, 5.0) for _ in range(2)]
iterations = 1000
step_size = 0.1
temp = 10.0

best, score, _scores = simulated_annealing(rastrigin_function, bounds, iterations, step_size, temp)

print(f'Best Solution: {best}')
print(f'Best Score: {score}')

