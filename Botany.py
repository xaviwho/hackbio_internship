import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# === Load and Explore Dataset ===
url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt"

# Load dataset (tab-separated)
df = pd.read_csv(url, sep="\s+", engine="python")

df = df.T  # Transpose the dataset
df.reset_index(inplace=True)  # Convert row labels into a proper column
df.rename(columns={"index": "Metabolite"}, inplace=True)  # Rename the new column


# Display dataset structure
print("Dataset after Transposing:\n", df.head())
print("\nDataset Columns:", df.columns.tolist())

# Ensure correct columns exist
required_columns = ["Metabolite", "WT_DMSO_1", "WT_pesticide_24h_1", "mutant_DMSO_1", "mutant_pesticide_24h_1"]
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing required column: {col}")  

# === Calculate Difference in Metabolic Response (ΔM) ===
df["ΔM_WT"] = df["WT_pesticide_24h_1"] - df["WT_DMSO_1"]
df["ΔM_MT"] = df["mutant_pesticide_24h_1"] - df["mutant_DMSO_1"]

# === Generate Scatter Plot with Fitted Line ===
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="ΔM_WT", y="ΔM_MT", color="blue", alpha=0.7)

# Fitted line: y = x
x_vals = np.linspace(df["ΔM_WT"].min(), df["ΔM_WT"].max(), 100)
plt.plot(x_vals, x_vals, linestyle="--", color="black", label="y = x (Slope=1)")

plt.xlabel("ΔM Wild Type (WT)")
plt.ylabel("ΔM Mutant (MT)")
plt.title("Metabolic Response Difference: WT vs MT")
plt.legend()
plt.show()

# === Compute Residuals & Color Metabolites ===
df["Residual"] = df["ΔM_MT"] - df["ΔM_WT"]

# Define cutoff threshold
cutoff = 0.3

# Color metabolites
df["Color"] = np.where(
    (df["Residual"] >= -cutoff) & (df["Residual"] <= cutoff), "grey", "salmon"
)

# Re-plot with color coding
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="ΔM_WT", y="ΔM_MT", hue="Color", palette={"grey": "grey", "salmon": "salmon"}, alpha=0.7)

plt.plot(x_vals, x_vals, linestyle="--", color="black", label="y = x (Slope=1)")
plt.xlabel("ΔM Wild Type (WT)")
plt.ylabel("ΔM Mutant (MT)")
plt.title("Metabolic Response Difference with Residuals")
plt.legend()
plt.show()

# === Identify Outlier Metabolites ===
outliers = df[df["Color"] == "salmon"]
print("\nMetabolites Outside Residual Cutoff:\n", outliers[["Metabolite", "Residual"]])

# Select 6 metabolites for time-series plot
selected_metabolites = outliers["Metabolite"].head(6).tolist()

# === Plot Time Series for 6 Outlier Metabolites ===
plt.figure(figsize=(10, 6))
for metabolite in selected_metabolites:
    subset = df[df["Metabolite"] == metabolite]
    
    # Use the correct column names
    times = ["WT_DMSO_1", "WT_pesticide_8h_1", "WT_pesticide_24h_1"]
    
    values = subset[times].values.flatten()

    plt.plot([0, 8, 24], values, marker="o", linestyle="-", label=metabolite)

plt.xlabel("Time (hours)")
plt.ylabel("Metabolic Response")
plt.title("Metabolic Response Over Time for Selected Metabolites")
plt.legend()
plt.show()