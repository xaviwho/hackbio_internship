def time_to_80_percent(K, P0, r, lag_time):
    """
    Determines time to reach 80% of carrying capacity.

    Args:
        K (float): Carrying capacity.
        P0 (float): Initial population.
        r (float): Growth rate.
        lag_time (int): Lag phase duration.

    Returns:
        float: Time to reach 80% of K.
    """
    P_target = 0.8 * K
    t_80 = lag_time + (np.log((K - P0) / (P_target - P0)) / r)
    return t_80

# Example usage
time_80 = time_to_80_percent(K=1000, P0=10, r=0.3, lag_time=4)
print(f"Time to reach 80% of carrying capacity: {time_80:.2f}")
