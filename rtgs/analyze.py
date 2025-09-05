import pandas as pd
from tabulate import tabulate

def analyze_rainfall(file: str, district: str = None):
    df = pd.read_csv(file)

    if district:
        df = df[df["district"].str.lower() == district.lower()]

    avg_rainfall = df.groupby("district")["rain_(mm)"].mean().reset_index()
    max_rain = avg_rainfall.loc[avg_rainfall["rain_(mm)"].idxmax()]
    min_rain = avg_rainfall.loc[avg_rainfall["rain_(mm)"].idxmin()]
    heavy_days = df[df["rain_(mm)"] > 20].shape[0]

    return {
        "avg_table": tabulate(avg_rainfall, headers="keys", tablefmt="pretty", showindex=False),
        "wettest": (max_rain["district"], round(max_rain["rain_(mm)"], 2)),
        "driest": (min_rain["district"], round(min_rain["rain_(mm)"], 2)),
        "heavy_days": heavy_days
    }
