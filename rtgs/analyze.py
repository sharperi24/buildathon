import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_dataset(file: str):
    df = pd.read_csv(file)
    results = {}
    os.makedirs("out/plots", exist_ok=True)
    os.makedirs("out/reports", exist_ok=True)

    # Overview
    rows, cols = df.shape
    results["rows"] = rows
    results["columns"] = cols
    missing = df.isna().sum()

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(include="object").columns.tolist()

    # --------------------
    # Plots
    # --------------------
    for col in cat_cols:
        plt.figure(figsize=(8,5))
        df[col].value_counts().head(10).plot(kind="bar")
        plt.title(f"Top Categories in {col}")
        plt.tight_layout()
        plt.savefig(f"out/plots/bar_{col}.png")
        plt.close()

    for col in numeric_cols:
        plt.figure(figsize=(8,5))
        sns.histplot(df[col].dropna(), bins=30, kde=True)
        plt.title(f"Distribution of {col}")
        plt.tight_layout()
        plt.savefig(f"out/plots/hist_{col}.png")
        plt.close()

    for col in numeric_cols:
        plt.figure(figsize=(6,5))
        sns.boxplot(x=df[col].dropna())
        plt.title(f"Boxplot of {col}")
        plt.tight_layout()
        plt.savefig(f"out/plots/box_{col}.png")
        plt.close()

    if len(numeric_cols) > 1:
        plt.figure(figsize=(8,6))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.savefig("out/plots/correlation_heatmap.png")
        plt.close()

    date_cols = df.select_dtypes(include="datetime").columns.tolist()
    if date_cols:
        for col in numeric_cols:
            for dcol in date_cols:
                plt.figure(figsize=(8,5))
                trend = df.groupby(df[dcol].dt.to_period("M"))[col].mean()
                trend.plot()
                plt.title(f"Trend of {col} over {dcol}")
                plt.tight_layout()
                plt.savefig(f"out/plots/line_{col}_over_{dcol}.png")
                plt.close()

    # -------------------------------
    # Single consolidated Excel report
    # -------------------------------
    report_file = "out/reports/analysis_report.xlsx"
    with pd.ExcelWriter(report_file) as writer:
        df.describe(include="all").T.to_excel(writer, sheet_name="Summary Stats")
        missing.to_frame("Missing").to_excel(writer, sheet_name="Missing Values")
        if len(numeric_cols) > 1:
            df[numeric_cols].corr().to_excel(writer, sheet_name="Correlation")

    print(f"[Analyze] Analysis complete. Report: {report_file}, Plots in out/plots/")
    results["report_file"] = report_file

    # Always add missing values summary
    results["missing"] = df.isna().sum().to_dict()

    # Always add columns summary
    columns_summary = []
    for col in df.columns:
        dtype = str(df[col].dtype)
        missing_count = int(df[col].isna().sum())
        if pd.api.types.is_numeric_dtype(df[col]):
            stats = {
                "min": df[col].min(),
                "max": df[col].max(),
                "mean": df[col].mean(),
                "std": df[col].std()
            }
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            stats = {
                "earliest": str(df[col].min()),
                "latest": str(df[col].max())
            }
        else:
            stats = {
                "unique": int(df[col].nunique()),
                "top": df[col].mode()[0] if not df[col].mode().empty else None
            }
        columns_summary.append({
            "column": col,
            "dtype": dtype,
            "missing": missing_count,
            "stats": stats
        })
    results["columns_summary"] = columns_summary

    return results
