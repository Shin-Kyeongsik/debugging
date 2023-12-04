scores = [10, 20, 30] # BP

score_mean = sum(scores) / len(scores)
print(score_mean)

scores[0] -= score_mean
scores[1] -= score_mean
scores[2] -= score_mean

score_mean = sum(scores) / len(scores)
print(score_mean)