import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_127039.csv", skiprows=4)

exclude_codes = [
    'WLD','ARB','CEB','CSS','EAP','EAR','EAS','ECA','ECS','EMU','EUU',
    'FCS','HIC','HPC','IBD','IBT','IDA','IDB','IDX','INX','LAC','LCN',
    'LDC','LIC','LMC','LMY','LTE','MEA','MIC','MNA','NAC','OED','OSS',
    'PRE','PSS','PST','SAS','SSA','SSF','SST','TEA','TEC','TLA','TMN',
    'TSA','TSS','UMC'
]

df = df[~df['Country Code'].isin(exclude_codes)]

df = df[~df['Country Name'].str.contains(
    'World|income|IBRD|IDA|demographic|OECD|Asia|Europe|Latin|Caribbean|North|Africa',
    case=False
)]

df = df[['Country Name', '2020']].dropna()

df_sorted = df.sort_values(by='2020', ascending=False).head(10)

df_sorted['Population (Millions)'] = df_sorted['2020'] / 1e6

plt.figure(figsize=(12,6))

bars = plt.bar(
    df_sorted['Country Name'],
    df_sorted['Population (Millions)'],
    color=sns.color_palette("viridis", len(df_sorted))
)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f'{height:.0f}M',
        ha='center',
        va='bottom',
        fontsize=9
    )

plt.title("Top 10 Most Populous Countries (2020)", fontsize=16, weight='bold')
plt.xlabel("Country", fontsize=12)
plt.ylabel("Population (Millions)", fontsize=12)

plt.xticks(rotation=45)

sns.despine()

plt.tight_layout()

plt.savefig("FINAL_PROFESSIONAL.png", dpi=300)

plt.show()