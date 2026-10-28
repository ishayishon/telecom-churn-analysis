"""Execute the notebook in a fresh project kernel and export an embedded HTML report."""
from pathlib import Path
import os
import sys
import json
from importlib.metadata import version
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter

ROOT = Path(__file__).resolve().parents[1]
kernel_root = ROOT / '.runtime' / 'share' / 'jupyter'
kernel = kernel_root / 'kernels' / 'telecom-project'
kernel.mkdir(parents=True, exist_ok=True)
(kernel / 'kernel.json').write_text(json.dumps({'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'], 'display_name': 'Telecom project', 'language': 'python'}))
os.environ['JUPYTER_PATH'] = str(kernel_root) + os.pathsep + os.environ.get('JUPYTER_PATH', '')
path = ROOT / 'Telecom_Churn_Analysis.ipynb'
nb = nbformat.read(path, as_version=4)
for cell in nb.cells:
    if cell.cell_type == 'code':
        cell.outputs = []
        cell.execution_count = None
NotebookClient(nb, timeout=900, kernel_name='telecom-project', resources={'metadata': {'path': str(ROOT)}}).execute()
assert not any(o.output_type == 'error' for c in nb.cells if c.cell_type == 'code' for o in c.outputs)
nbformat.write(nb, path)
exporter = HTMLExporter()
exporter.embed_images = True
body, _ = exporter.from_notebook_node(nb)
(ROOT / 'Telecom_Churn_Report.html').write_text(body, encoding='utf-8')
packages = ['numpy', 'pandas', 'matplotlib', 'seaborn', 'scikit-learn', 'scipy', 'nbformat', 'nbclient', 'nbconvert', 'ipykernel', 'threadpoolctl']
(ROOT / 'requirements.txt').write_text('\n'.join(f'{p}=={version(p)}' for p in packages) + '\n')
print('Fresh execution and HTML export completed.', flush=True)
