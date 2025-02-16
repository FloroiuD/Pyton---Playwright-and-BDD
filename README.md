# automated-regression-tests
Automated regression tests suite

### Setup Requirements
1. Start virtual environment
```shell
python3 -m venv ./venv && source venv/bin/activate
````
2. Install Requirements
```shell
pip install -r requirements.txt
playwright install
pip install pytest-playwright
pip install pytest-bdd
```
Notes: Make sure you have installed the all extensions mentioned in SS. 


3. Set environment variables
```shell
cp .env.example .env
```
### Run feature tests
```shell
pytest tests/*
```

### Run all tests
```shell
pytest
```

### Run linter
```shell
flake8
```
### Run autoformatter
```shell
autopep8 .
```
