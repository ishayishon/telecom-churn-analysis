# Telecom Customer Churn Analysis

An academic data visualization and machine learning project based on 7,043 customer records and 21 columns. The analysis combines exploratory charts, group comparisons, feature engineering, and classification models to investigate customer churn.

## Project Files

- [Telecom_Churn_Report.html](Telecom_Churn_Report.html): the report with code, explanations, charts, and results. Download it and open it in a browser without installing anything.
- [Telecom_Churn_Analysis.ipynb](Telecom_Churn_Analysis.ipynb): the complete Jupyter notebook for editing and execution.
- `data/telecom_customers_churn.csv`: the supplied coursework dataset. Its external source and redistribution license have not been verified.
- `docs/assignment.pdf`: the instructor's assignment requirements.
- `docs/requirements-checklist.md`: a mapping from assignment requirements to the analysis.
- `docs/methodology.md`: the analysis protocol and experimental limitations.
- `results/`: comparison tables, test results, and figures.

## Setup

Tested with Python 3.12. Create a virtual environment:

```sh
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS or Linux:

```sh
source .venv/bin/activate
```

Install the dependencies:

```sh
python -m pip install -r requirements.txt
```

## Run

Open the notebook from the project directory, select the environment's Python kernel, and choose **Restart Kernel and Run All**. Alternatively:

```sh
python scripts/run_project.py
```

The script starts a fresh kernel, executes every cell, and saves the executed notebook and HTML report. Training may take several minutes. Outputs under `results/` are overwritten. All paths are relative; archived course materials are not required.

## Evaluation

The data is split into stratified training, validation, and test partitions of 60%, 20%, and 20%. Models are selected by validation F1 for the churn class. The chosen configuration is then refitted on training and validation data and evaluated on the held-out test set. A majority-class baseline provides a reference.

The experiments compare Random Forest, AdaBoost, and Logistic Regression with baseline features, a subscribed-service count, PCA, KMeans cluster indicators, and combined PCA and KMeans preprocessing. Hard and soft voting ensembles are also evaluated. Learned preprocessing is fitted within the training pipeline.

Detailed metrics are saved in `results/validation_metrics.csv` and `results/test_metrics.json`. The saved Logistic Regression model with baseline features achieved **80.6% test accuracy** and **0.604 churn F1**.

## Limitations

Group comparisons describe associations and do not establish causation. A single split has sampling uncertainty. These academic experimental results do not demonstrate production performance.
