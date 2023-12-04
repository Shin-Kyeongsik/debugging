score1, score2, score3 = 10, 20, 30
n_studnets = 3

mean_of_squared = (score1**2 + score2**2 + score3**2) / n_studnets # BP.1

score_mean = (score1 + score2 + score3) / n_studnets
squared_of_mean = score_mean**2

score_var = mean_of_squared - squared_of_mean # BP.2
score_std = score_var**0.5
print(f"{score_var = :.4f}")
print(f"{score_std = :.4f}") # BP.3