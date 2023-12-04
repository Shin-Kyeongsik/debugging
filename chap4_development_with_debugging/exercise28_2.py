import random

n_students = 10
scores = [random.randint(0, 120) for _ in range(n_students)]

max_score, min_score = None, None
for score in scores: # BP
    if max_score == None or score > max_score:
        max_score = score

    if min_score == None or score < min_score:
        min_score = score

print(f"{max_score = }")
print(f"{min_score = }")