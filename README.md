# RTGS CLI – Telangana Open Data Analyzer

## Overview
RTGS CLI is a lightweight data pipeline built for exploring datasets from the [Telangana Open Data Portal](https://data.telangana.gov.in/).  
It standardizes, cleans, and analyzes government datasets in a **generalized, domain-agnostic way** — meaning it works not just for rainfall, but also for transport, electricity, health, and more.

The goal is to help **stakeholders and policymakers** quickly gain insights from raw datasets without manually cleaning and plotting.

---

## Features
- **Generalized Ingestion** – Standardizes column names across any dataset.  
- **Cleaning Pipeline** – Handles missing values, numeric imputation, and data type fixes.  
- **Feature Engineering** – Adds common derived features (e.g., per-capita ratios, rolling averages).  
- **Analysis & Reports**  
  - Summary statistics (counts, averages, distributions, correlations)  
  - Trend detection for time-series data  
  - Variability metrics (standard deviation, quartiles)  
  - One-click export of **plots & reports**  
- **CLI Interface** – Simple commands to ingest, clean, and analyze datasets.

---

## Installation
```bash
# Clone repository
git clone <your-repo-url>
cd rtgs-cli

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
