import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style for professional look
sns.set(style="whitegrid")

# Load dataset
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_127039.csv", skiprows=4)

# Remove aggregates
exclude_codes = [
    'WLD','ARB','CEB','CSS','EAP','EAR','EAS','ECA','ECS','EMU','EUU',
    'FCS','HIC','HPC','IBD','IBT','IDA','IDB','IDX','INX','LAC','LCN',
    'LDC','LIC','LMC','LMY','LTE','MEA','MIC','MNA','NAC','OED','OSS',
    'PRE','PSS','PST','SAS','SSA','SSF','SST','TEA','TEC','TLA','TMN',
    'TSA','TSS','UMC'
]

df = df[~df['Country Code'].isin(exclude_codes)]

# Prepare data
df = df[['Country Name', '2020']].dropna()
df_sorted = df.sort_values(by='2020', ascending=False).head(10)

# Convert population to millions for readability
df_sorted['Population (Millions)'] = df_sorted['2020'] / 1e6

# Plot
plt.figure(figsize=(12,6))

bars = plt.bar(df_sorted['Country Name'],
               df_sorted['Population (Millions)'],
               color=sns.color_palette("viridis", 10))

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             height,
             f'{height:.0f}M',
             ha='center',
             va='bottom',
             fontsize=9)

# Titles and labels
plt.title("Top 10 Most Populous Countries (2020)", fontsize=16, weight='bold')
plt.xlabel("Country", fontsize=12)
plt.ylabel("Population (Millions)", fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

# Save high quality image
plt.savefig("FINAL_PROFESSIONAL.png", dpi=300)

plt.show()