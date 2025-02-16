import pandas as pd

def generate_growth_dataframe(num_curves=100):
    """
    Generates a DataFrame with multiple logistic growth curves.
    
    Args:
        num_curves (int): Number of growth curves to generate.
        
    Returns:
        DataFrame: Growth data with 100 curves.
    """
    t = np.arange(0, 50, 0.5)  # Time points
    all_curves = {}

    for i in range(num_curves):
        lag_time = np.random.randint(2, 7)
        exp_time = np.random.randint(5, 12)
        K = np.random.randint(800, 1200)  # Varying carrying capacities
        P0 = np.random.randint(5, 15)  # Different starting populations
        r = np.random.uniform(0.2, 0.5)  # Growth rate variation

        population = logistic_growth(t, K, P0, r, lag_time, exp_time)
        all_curves[f"Curve_{i+1}"] = population

    df = pd.DataFrame(all_curves, index=t)
    df.index.name = "Time"
    
    return df

# Generate the DataFrame
growth_df = generate_growth_dataframe()
print(growth_df.head())  # View first few rows
