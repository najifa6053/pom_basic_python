import os
import glob
import pytest

os.makedirs("reports", exist_ok=True)

test_files = sorted(glob.glob("tests/test_*.py"))

num_workers = len(test_files)

import multiprocessing
cpu_cores = multiprocessing.cpu_count()
if num_workers > cpu_cores:
    num_workers = cpu_cores
       
pytest.main([
    *test_files,
    "-n", str(num_workers),
    "--dist=loadscope",
    "--html=reports/report.html",
    "--self-contained-html"
])