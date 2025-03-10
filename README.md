# automated-tests
Automated tests suite

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
_Notes_: Make sure you have installed the all extensions mentioned in SS. 
![Screenshot from 2025-02-17 00-00-40](https://github.com/user-attachments/assets/1504645c-1e49-4910-9cd5-a166c83c2aa7)


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
