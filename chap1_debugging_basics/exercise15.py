score1, score2, score3 = 10, 20, 30
n_students = 3

mean_of_squared = (score1**2 + score2**2 + score3**2) / n_students # BP.1
score_mean = (score1 + score2 + score3) / n_students
squared_of_mean = score_mean**2

score_std = (mean_of_squared - squared_of_mean)**0.5
print(f"score mean(before ms): {score_mean}")
print(f"score std(before ms): {score_std:.4f}\n")

score1 = (score1 - score_mean) / score_std # BP.2
score2 = (score2 - score_mean) / score_std
score3 = (score3 - score_mean) / score_std

mean_of_squared = (score1**2 + score2**2 + score3**2) / n_students # BP.3
score_mean = (score1 + score2 + score3) / n_students
squared_of_mean = score_mean**2

score_std = (mean_of_squared - squared_of_mean)**0.5
print(f"score mean(after ms): {score_mean}")
print(f"score std(after ms): {score_std}") # BP.4