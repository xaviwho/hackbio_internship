import numpy as np
import matplotlib.pyplot as plt

def logistic_growth(t, K, P0, r, lag_time, exp_time):
    """
    Simulates a logistic growth curve with randomized lag and exponential phases.

    Args:
        t (array): Time points.
        K (float): Carrying capacity.
        P0 (float): Initial population.
        r (float): Growth rate.
        lag_time (int): Randomized lag phase duration.
        exp_time (int): Randomized exponential phase duration.

    Returns:
        array: Population values over time.
    """
    P = np.zeros_like(t, dtype=float)
    for i, time in enumerate(t):
        if time < lag_time:
            P[i] = P0  # Lag phase (no growth)
        else:
            P[i] = K / (1 + ((K - P0) / P0) * np.exp(-r * (time - lag_time)))
    
    return P

# Example plot
t = np.arange(0, 50, 0.5)  # Time from 0 to 50 in steps of 0.5
K = 1000  # Carrying capacity
P0 = 10  # Initial population
r = 0.3  # Growth rate
lag_time = np.random.randint(2, 7)  # Randomized lag time
exp_time = np.random.randint(5, 12)  # Randomized exponential time

population = logistic_growth(t, K, P0, r, lag_time, exp_time)

plt.plot(t, population, label="Logistic Growth")
plt.xlabel("Time")
plt.ylabel("Population Size")
plt.title("Simulated Logistic Growth Curve")
plt.legend()
plt.show()
