scores = [10, 20, 30]

score_mean = sum(scores) / len(scores)
print(score_mean)

scores_ms = [] # BP
scores_ms.append(scores[0] - score_mean)
scores_ms.append(scores[1] - score_mean)
scores_ms.append(scores[2] - score_mean)

score_mean_ms = sum(scores_ms) / len(scores_ms)
print(score_mean_ms)