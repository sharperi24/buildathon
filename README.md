# RTGS-Style AI Analyst for Telangana Open Data

## Overview

This project implements an **RTGS-style AI Analyst** CLI tool that ingests, cleans, and analyzes datasets from the **Telangana Open Data Portal**.
The system is **data-agnostic** — meaning it works across multiple domains (weather, transport, agriculture, electricity, etc.) without hardcoding for a single dataset.

Stakeholders (like government departments, policy analysts, and researchers) can use this tool to quickly extract insights, generate plots, and build reports for decision-making.

---

## Features

* **CLI Tool (Python Click-based)**

  * `ingest`: Standardize dataset column names.
  * `clean`: Handle missing values, datatype conversions, and prepare datasets.
  * `analyze`: Generate **statistical reports** and **visual plots**.
  * `help`: Usage guide and examples.

* **Generalized Workflow**

  * Works on any structured dataset from the Telangana Open Data Portal.
  * No hardcoding for rainfall/agriculture-specific columns.

* **Outputs**

  * Processed datasets saved to `/data/processed`
  * Reports and plots saved to `/out/reports` and `/out/plots`

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rtgs-cli.git
cd rtgs-cli
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the pipeline

```bash
# Step 1: Ingest raw dataset
python -m rtgs.cli ingest data/raw/rainfall.csv

# Step 2: Clean the standardized dataset
python -m rtgs.cli clean data/processed/rainfall_standardized.csv

# Step 3: Analyze cleaned dataset
python -m rtgs.cli analyze data/processed/rainfall_cleaned.csv

# Step 4: Get help if needed
python -m rtgs.cli help
```

---

## Example Outputs

* **Reports** (CSV + TXT summaries)
* **Plots** (saved in `/out/plots`):

  * Bar Charts (category-wise averages)
  * Line Charts (trends over time)
  * Histograms (distributions)
  * Boxplots (variability)
  * Heatmaps (correlations)

---

## Project Structure

```
rtgs-cli/
│
├── data/
│   ├── raw/              # Raw datasets
│   ├── processed/        # Standardized + cleaned datasets
│
├── out/
│   ├── reports/          # Generated reports
│   ├── plots/            # Plots and charts
│
├── rtgs/
│   ├── cli.py            # Main CLI entrypoint
│   ├── ingest.py         # Ingest datasets
│   ├── clean.py          # Clean datasets
│   ├── analyze.py        # Analyze datasets
│
├── logs/                 # Log files
├── README.md
```

---

## Future Scope

* **Feature Engineering**:
  Automatically generate derived features (e.g., monthly averages, growth rates, anomaly flags).

* **AI-powered Insights**:
  Integrate semantic prompts or LLM-based agents to allow natural language queries like:

  > *"Which district saw the steepest rise in rainfall in 2025?"*

* **Automated Data Fetching**:
  Connect directly to the Telangana Open Data Portal to fetch the latest datasets without manual download.

* **Dashboard Application**:
  Extend the CLI into a **web dashboard** (Flask/Streamlit) for policymakers with interactive plots.

* **Cross-dataset Comparisons**:
  Support merging datasets from different domains (e.g., rainfall vs crop yield) for richer insights.

---

## Why This Matters

Government stakeholders need **quick, reliable, and scalable insights**.
This system ensures:

* Faster **data-to-decision pipeline**
* Consistent preprocessing across datasets
* Reusable, extensible, and data-agnostic foundation
