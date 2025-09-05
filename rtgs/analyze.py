import pandas as pd
from tabulate import tabulate
import os

def run(file: str):
    print(f"[Analyze] Loading dataset: {file}")
    df = pd.read_csv(file)

    results = {}

    # Average rainfall per district
    avg_rain = df.groupby("district")["rain_(mm)"].mean().reset_index()
    results["avg_rain"] = avg_rain

    # District with max and min average rainfall
    max_district = avg_rain.loc[avg_rain["rain_(mm)"].idxmax()]
    min_district = avg_rain.loc[avg_rain["rain_(mm)"].idxmin()]

    results["max"] = max_district
    results["min"] = min_district

    # Print nicely
    print("\n[Analyze] Average Rainfall per District (mm)")
    print(tabulate(avg_rain, headers="keys", tablefmt="grid", showindex=False))

    print("\n[Analyze] Wettest District:", max_district["district"], "-", round(max_district["rain_(mm)"], 2), "mm")
    print("[Analyze] Driest District:", min_district["district"], "-", round(min_district["rain_(mm)"], 2), "mm")

    # Save results
    os.makedirs("out", exist_ok=True)
    avg_rain.to_csv("out/avg_rainfall.csv", index=False)

    print("\n[Analyze] Results saved in out/avg_rainfall.csv")
