scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

score_sum = 0
for score in scores: # BP
    score_sum += score

score_mean = score_sum / len(scores)
print(score_mean)