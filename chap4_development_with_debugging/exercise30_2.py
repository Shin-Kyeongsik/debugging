import random

n_students = 100
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]

score_dict = {key: 0 for key in ['pass_sum', 'no_pass_sum',
                                 'pass_cnt', 'no_pass_cnt']}
for score in scores: # BP
    if score >= threshold:
        score_dict['pass_sum'] += score
        score_dict['pass_cnt'] += 1
    else:
        score_dict['no_pass_sum'] += score
        score_dict['no_pass_cnt'] += 1
