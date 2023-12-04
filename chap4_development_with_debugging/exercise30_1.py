import random

n_students = 100
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]

for score in scores: # BP
    if score >= threshold:
        continue
    else:
        continue
