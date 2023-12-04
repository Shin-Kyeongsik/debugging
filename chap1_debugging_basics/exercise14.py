score1, score2, score3 = 10, 20, 30
n_students = 3

score_mean = (score1 + score2 + score3) / n_students # BP.1
print(f"score mean(before ms): {score_mean}")

score1 -= score_mean # BP.2
score2 -= score_mean
score3 -= score_mean

score_mean = (score1 + score2 + score3) / n_students # BP.3
print(f"score mean(after ms): {score_mean}") # BP.4