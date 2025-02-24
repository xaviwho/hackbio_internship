import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# === Import Datasets ===
sift_url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv"
foldx_url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv"

# Load the datasets
sift_df = pd.read_csv(sift_url, sep="\s+", engine="python")
foldx_df = pd.read_csv(foldx_url, sep="\s+", engine="python")

# Display structure of datasets
print("SIFT Dataset Columns:", sift_df.columns)
print("FoldX Dataset Columns:", foldx_df.columns)

# Display structure of datasets
print("SIFT Dataset Preview:\n", sift_df.head(), "\n")
print("FoldX Dataset Preview:\n", foldx_df.head(), "\n")

# === Create Unique Mutation Identifier ===
# Concatenating 'Protein' and 'Amino_acid' columns
sift_df["specific_Protein_aa"] = sift_df["Protein"] + "_" + sift_df["Amino_Acid"]
foldx_df["specific_Protein_aa"] = foldx_df["Protein"] + "_" + foldx_df["Amino_Acid"]

# === Merge the Datasets ===
merged_df = pd.merge(sift_df, foldx_df, on="specific_Protein_aa", suffixes=('_sift', '_foldx'))

# Display merged dataset
print("Merged Dataset Preview:\n", merged_df.head(), "\n")

# === Filter for High-Impact Mutations ===
deleterious_mutations = merged_df[
    (merged_df["sift_Score"] < 0.05) & (merged_df["foldX_Score"] > 2)
]


# Display filtered results
print("Deleterious Mutations Affecting Both Structure & Function:\n", deleterious_mutations.head(), "\n")

# === Extract Amino Acid Impact ===
# Extract first amino acid from the mutation description (e.g., "E63D" -> "E")
deleterious_mutations["Amino_acid_initial"] = deleterious_mutations["Amino_Acid_sift"].str[0]

# Generate frequency table
amino_acid_counts = deleterious_mutations["Amino_acid_initial"].value_counts()

# Display frequency table
print("Amino Acid Impact Frequency Table:\n", amino_acid_counts, "\n")

# === Visualize Data ===
# Bar Plot
plt.figure(figsize=(10, 5))
sns.barplot(x=amino_acid_counts.index, y=amino_acid_counts.values, palette="viridis")
plt.xlabel("Amino Acid")
plt.ylabel("Frequency")
plt.title("Frequency of High-Impact Amino Acids")
plt.show()

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(amino_acid_counts, labels=amino_acid_counts.index, autopct="%1.1f%%", colors=sns.color_palette("viridis", len(amino_acid_counts)))
plt.title("Proportion of High-Impact Amino Acids")
plt.show()

# === Interpretation ===
# Identify the amino acid with the highest impact
highest_impact_aa = amino_acid_counts.idxmax()
highest_impact_count = amino_acid_counts.max()

print(f"\n🔬 The amino acid with the highest impact on protein structure & function is **{highest_impact_aa}** with **{highest_impact_count} occurrences**.")

# Amino acids occurring more than 100 times
high_occurrence_aas = amino_acid_counts[amino_acid_counts > 100]
print("\nAmino acids with more than 100 occurrences:\n", high_occurrence_aas)

print("\n🔍 **Analysis:**")
print("- The amino acid with the highest impact likely plays a crucial role in protein stability & function.")
print("- Amino acids with more than 100 occurrences may have distinct biochemical properties (e.g., charge, polarity, hydrophobicity) affecting structure & function.")
