scores = [10, 20, 30] # BP

score_mean = sum(scores) / len(scores)
scores_squared_diff = [(scores[0] - score_mean)**2,
                       (scores[1] - score_mean)**2,
                       (scores[2] - score_mean)**2]

score_var = sum(scores_squared_diff) / len(scores_squared_diff)
score_std = score_var**0.5
print(f"{score_std = :.4f}")