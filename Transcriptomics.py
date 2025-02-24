import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# === Load the RNA-Seq Dataset ===
url = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"

# Load dataset (tab-separated)
rna_df = pd.read_csv(url, sep="\s+", engine="python")

# Display structure
print("Dataset Preview:\n", rna_df.head())
print("\nDataset Columns:", rna_df.columns)

# Ensure correct column names
required_columns = ["Gene", "log2FoldChange", "pvalue"]
for col in required_columns:
    if col not in rna_df.columns:
        raise ValueError(f"Missing required column: {col}")

# === Generate a Volcano Plot ===
# Define threshold for significance
rna_df["-log10(pvalue)"] = -np.log10(rna_df["pvalue"])

# Define colors based on conditions
def get_volcano_color(row):
    if row["log2FoldChange"] > 1 and row["pvalue"] < 0.01:
        return "red"  # Upregulated
    elif row["log2FoldChange"] < -1 and row["pvalue"] < 0.01:
        return "blue"  # Downregulated
    else:
        return "gray"  # Non-significant

rna_df["color"] = rna_df.apply(get_volcano_color, axis=1)

# Plot Volcano Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=rna_df, x="log2FoldChange", y="-log10(pvalue)", hue="color", palette={"red": "red", "blue": "blue", "gray": "gray"}, alpha=0.7)

# Highlight Upregulated and Downregulated Genes
plt.axvline(x=1, linestyle="--", color="black")  # Log2FC > 1
plt.axvline(x=-1, linestyle="--", color="black")  # Log2FC < -1
plt.axhline(y=-np.log10(0.01), linestyle="--", color="black")  # p < 0.01

plt.xlabel("Log2 Fold Change")
plt.ylabel("-Log10(p-value)")
plt.title("Volcano Plot of Differential Gene Expression")
plt.legend(["Threshold", "Upregulated", "Downregulated", "Not Significant"])
plt.show()

# === Identify Upregulated & Downregulated Genes ===
# Upregulated: Log2FC > 1 and p-value < 0.01
upregulated = rna_df[(rna_df["log2FoldChange"] > 1) & (rna_df["pvalue"] < 0.01)].sort_values(by="log2FoldChange", ascending=False)

# Downregulated: Log2FC < -1 and p-value < 0.01
downregulated = rna_df[(rna_df["log2FoldChange"] < -1) & (rna_df["pvalue"] < 0.01)].sort_values(by="log2FoldChange")

# Display top upregulated and downregulated genes
print("\nTop 5 Upregulated Genes:\n", upregulated.head(5)[["gene", "log2FoldChange", "pvalue"]])
print("\nTop 5 Downregulated Genes:\n", downregulated.head(5)[["gene", "log2FoldChange", "pvalue"]])

# === Retrieve Gene Functions (Manually in GeneCards) ===
print("\n **Next Step:** Search for the top 5 upregulated & downregulated genes in **GeneCards** (https://www.genecards.org/) to interpret their functions.")
