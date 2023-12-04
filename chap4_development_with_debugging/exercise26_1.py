import random

n_data = 10
window_size = 2

data = [random.randint(0, 10) for _ in range(n_data)]

n_windows = n_data - window_size + 1
for window_idx in range(n_windows): # BP
    start_idx, end_idx = window_idx, window_idx + window_size
    window = data[start_idx:end_idx]