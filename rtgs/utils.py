import os
import logging

def setup_logging():
    logging.basicConfig(
        filename="rtgs.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    logging.info("Logger initialized")

def create_output_dirs(dataset_name):
    base_dir = os.path.join("out", dataset_name)
    reports_dir = os.path.join(base_dir, "reports")
    plots_dir = os.path.join(base_dir, "plots")

    os.makedirs(reports_dir, exist_ok=True)
    os.makedirs(plots_dir, exist_ok=True)

    return reports_dir, plots_dir
