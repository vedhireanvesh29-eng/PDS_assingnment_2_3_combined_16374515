# Assignment 2 & 3 Project

Organized workspace for two assignments with shared data and reporting folders. Place the datasets in `data/` before running the scripts.

## Structure
- Assignment_2_3_Project/
  - Assignment_2/assignment2_usedcars.py
  - Assignment_3/ (placeholder for future work)
  - Assignment_3_Dataset2/analysis_dataset2.py
  - data/ (expects CSV inputs)
  - reports/ (script outputs)

## Data locations
- `data/train_Dataset_1.csv` (required for Assignment 2)
- `data/diabetes.csv` (optional if provided)
- `data/diabetes_Dataset_2.csv` (required for Dataset 2 analysis)

> Note: These CSV files were not found in the workspace, so they still need to be added to `data/`.

## Running scripts
1. Assignment 2 (used cars)
   ```bash
   cd Assignment_2_3_Project/Assignment_2
   python assignment2_usedcars.py
   ```
   - Outputs cleaned CSV to `../reports/Assignment2_cleaned_output.csv`.

2. Dataset 2 analysis (Assignment 3)
   ```bash
   cd Assignment_2_3_Project/Assignment_3_Dataset2
   python analysis_dataset2.py
   ```
   - Saves bootstrap histogram to `../reports/dataset2_bootstrap_bp.png`.

Ensure Python environment has `pandas`, `numpy`, and `matplotlib` installed.
