import random

n_students = 1000
threshold = 95
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

pass_scores = []
for score in scores:
    if score >= threshold: # BP: score >= threshold
        pass_scores.append(score)

pass_score_mean = sum(pass_scores) / len(pass_scores)
print(f"{pass_score_mean = }")