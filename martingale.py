import numpy as np
import config

def generate_martingales():
    martingales = np.zeros((config.num_trials, config.num_steps))
    for trial in range(config.num_trials):
        path = [0]
        for _ in range(1, config.num_steps):
            step = np.random.choice([-1, 1])
            next_val = path[-1] + step
            next_val = max(min(next_val, config.bound), -config.bound)
            path.append(next_val)
        martingales[trial] = path
    return martingales
