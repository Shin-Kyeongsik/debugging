import random

n_students = 10
scores = [random.randint(0, 120) for _ in range(n_students)]
print(scores)

scores_ = scores.copy() # BP
print()