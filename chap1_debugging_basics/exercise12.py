score1, score2, score3 = 10, 20, 30 # BP.1
n_studnets = 3

score_mean = (score1 + score2 + score3) / n_studnets

squared_diff1 = (score1 - score_mean)**2 # BP.2
squared_diff2 = (score2 - score_mean)**2
squared_diff3 = (score3 - score_mean)**2

variance = (squared_diff1 + squared_diff2 + squared_diff3) / n_studnets # BP.3
print(f"{variance}")