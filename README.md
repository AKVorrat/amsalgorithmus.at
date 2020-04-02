# amsalgorithmus.at

The code for the petition module closely resembles that of
istkicklschonweg.at. Go to [AKVorrat/istkicklschonweg.at](https://github.com/AKVorrat/istkicklschonweg.at)
for a more detailed commit history.

## Setup

```bash
virtualenv .venv 
source .venv/bin/activate

pip install .[dev]

python ./manage.py migrate
```

## Running

```bash
python ./manage.py runserver
```

## Scss

Scss source files are located in `ams/static/scss`.
