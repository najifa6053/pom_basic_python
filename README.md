Step 1: Clone the project
Open Terminal:
git clone https://github.com/najifa6053/POM_BASIC_PYTHON-.git

Step 2: Create and Activate a Virtual Environment
py -m venv venv
source venv/scripts/activate


Step 3: Install Selenium and WebDriver Manager
pip install selenium webdriver-manager


Step 4: Install pytest and pytest html
pip install pytest
pip install pytest-html
pip install pytest-dependency
pip install pytest-order


Step 5: Run the Script
In Terminal: To run a specific file

pytest <file_name> --html=reports/report.html --self-contained-html
In Terminal: To run a all testcases

pytest --html=reports/report.html --self-contained-html
Notes:
Tests use pytest-order to control execution order. Install with pip install pytest-order if needed.
After a run the HTML report will be created at reports/report.html.