import click
import pandas as pd
import os
import logging
import matplotlib.pyplot as plt
import seaborn as sns
from rtgs.utils import setup_logging, create_output_dirs


@click.command()
@click.argument("file", type=click.Path(exists=True))
def analyze(file):
    """Analyze cleaned dataset and generate a report + plots."""
    setup_logging()

    dataset_name = os.path.splitext(os.path.basename(file))[0].replace("_cleaned", "")
    reports_dir, plots_dir = create_output_dirs(dataset_name)

    try:
        logging.info(f"[Analyze] Loading dataset: {file}")
        df = pd.read_csv(file)

        # --- Basic Stats ---
        stats = {
            "rows": len(df),
            "columns": len(df.columns),
            "missing_values": df.isna().sum().to_dict(),
            "summary": df.describe(include="all").transpose()
        }

        # Save stats report
        report_path = os.path.join(reports_dir, f"{dataset_name}_report.txt")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("=== Dataset Overview ===\n")
            f.write(f"Rows: {stats['rows']}, Columns: {stats['columns']}\n\n")

            f.write("=== Missing Values ===\n")
            for col, val in stats["missing_values"].items():
                f.write(f"{col}: {val}\n")
            f.write("\n")

            f.write("=== Summary Statistics ===\n")
            f.write(str(stats["summary"]))
            f.write("\n")

        logging.info(f"[Analyze] Report saved: {report_path}")
        click.echo(f"Report generated: {report_path}")

        # --- Plots ---
        num_cols = df.select_dtypes(include="number").columns
        cat_cols = df.select_dtypes(include="object").columns

        # 1. Histograms for numeric columns
        for col in num_cols:
            plt.figure()
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f"Distribution of {col}")
            plt.savefig(os.path.join(plots_dir, f"{col}_hist.png"))
            plt.close()

        # 2. Boxplots for numeric columns
        for col in num_cols:
            plt.figure()
            sns.boxplot(x=df[col].dropna())
            plt.title(f"Boxplot of {col}")
            plt.savefig(os.path.join(plots_dir, f"{col}_box.png"))
            plt.close()

        # 3. Scatter plots for first two numeric columns (if available)
        if len(num_cols) >= 2:
            plt.figure()
            sns.scatterplot(x=df[num_cols[0]], y=df[num_cols[1]])
            plt.title(f"Scatter: {num_cols[0]} vs {num_cols[1]}")
            plt.savefig(os.path.join(plots_dir, f"{num_cols[0]}_vs_{num_cols[1]}_scatter.png"))
            plt.close()

        # 4. Correlation heatmap
        if len(num_cols) > 1:
            plt.figure(figsize=(8, 6))
            corr = df[num_cols].corr()
            sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Heatmap")
            plt.savefig(os.path.join(plots_dir, "correlation_heatmap.png"))
            plt.close()

        # 5. Bar charts for categorical columns
        for col in cat_cols:
            if df[col].nunique() < 20:  # only for low-cardinality columns
                plt.figure(figsize=(8, 4))
                df[col].value_counts().plot(kind="bar")
                plt.title(f"Bar Chart of {col}")
                plt.ylabel("Count")
                plt.savefig(os.path.join(plots_dir, f"{col}_bar.png"))
                plt.close()

        # 6. Line plot (if any datetime column exists)
        date_cols = df.select_dtypes(include="datetime").columns
        if len(date_cols) > 0 and len(num_cols) > 0:
            plt.figure()
            df.set_index(date_cols[0])[num_cols[0]].plot()
            plt.title(f"Line Plot of {num_cols[0]} over {date_cols[0]}")
            plt.ylabel(num_cols[0])
            plt.savefig(os.path.join(plots_dir, f"{num_cols[0]}_time_series.png"))
            plt.close()

        logging.info(f"[Analyze] Plots saved to {plots_dir}")
        click.echo(f"Plots saved to {plots_dir}")

    except Exception as e:
        logging.error(f"[Analyze] Failed for {dataset_name}: {e}")
        click.echo(f"Error during analysis: {e}")
