# bestTariff
[![Build Status](https://travis-ci.org/oriolpiera/bestTariff.svg?branch=master)](https://travis-ci.org/oriolpiera/bestTariff)
[![Coverage Status](https://coveralls.io/repos/github/oriolpiera/bestTariff/badge.svg)](https://coveralls.io/github/oriolpiera/bestTariff)

Best electrical tariff based on your hourly consumption

### Quick start

Clone de repository an install using pip:

    pip install -e .

### Usage

You can use as a Python package or as a CLI interface

CLI usage:

    python besttariff/besttariff.py ~/Downloadss/curves.csv '2.0_A'

Python package:

```python
from besttarariff import *

tc = TariffCalculator()
cu = CurveUtils()
curves = cu.loadCurveFile(curves_file)
result, allResults = tc.calculator(tariff, curves)
```

### File format of curves.csv

You can see an example in /besttariff/tests/sample_curve_file.csv

|CUPS|Fecha|Hora|Consumo_kWh|Metodo_obtencion|
|---|---|---|---|---|
|ES3577725301912137LC|01/01/2020|1|1,308|R|
|ES3577725301912137LC|01/01/2020|2|0,455|R|
|ES3577725301912137LC|01/01/2020|3|0,42|R|
