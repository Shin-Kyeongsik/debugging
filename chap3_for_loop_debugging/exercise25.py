scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

score_mean = sum(scores) / len(scores)
sum_squared_dev = 0
for score in scores: # BP.1
    sum_squared_dev += (score - score_mean)**2
score_var = sum_squared_dev / len(scores)

score_std = score_var**0.5
print(f"var: {score_var}")
print(f"std: {score_std}") # BP.2