"""Check the delivered notebook outputs against saved data and predictions."""
from pathlib import Path
import json
import hashlib
import pandas as pd
import nbformat
from sklearn.metrics import accuracy_score, f1_score, recall_score

root = Path(__file__).resolve().parents[1]
results = root / 'results'
meta = json.loads((results / 'run_metadata.json').read_text())
assert hashlib.sha256((root / 'data/telecom_customers_churn.csv').read_bytes()).hexdigest() == meta['dataset_sha256']
nb = nbformat.read(root / 'Telecom_Churn_Analysis.ipynb', as_version=4)
cells = [c for c in nb.cells if c.cell_type == 'code' and c.source.strip()]
assert [c.execution_count for c in cells] == list(range(1, len(cells) + 1))
assert not any(o.output_type == 'error' for c in cells for o in c.outputs)
assert len(pd.read_csv(results / 'validation_metrics.csv')) == 18
predictions = pd.read_csv(results / 'test_predictions.csv')
scores = json.loads((results / 'test_metrics.json').read_text())['test_metrics']
assert len(predictions) == meta['test_rows']
for name, metric in [('accuracy', accuracy_score), ('f1', f1_score), ('recall', recall_score)]:
    actual = metric(predictions.actual_churn, predictions.predicted_churn)
    assert abs(actual - scores[name]) < 1e-12
assert len(list((results / 'figures').glob('*.png'))) == 9
assert (root / 'Telecom_Churn_Report.html').stat().st_size > 100_000
print(f'PASS: {len(cells)} executed code cells, 18 validation rows, 9 figures, data checksum and test prediction count.')
