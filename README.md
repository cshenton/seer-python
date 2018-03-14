# Seer Python Client
[![Build Status](https://travis-ci.org/cshenton/seer-python.svg?branch=master)](https://travis-ci.org/cshenton/seer-python)
[![Python Version](https://img.shields.io/pypi/pyversions/seer.svg)](https://pypi.org/project/seer/)

The python client for the seer forecasting server.


## Installation

The seer python client is available on PyPi, so just `pip install seer` to get the latest release.


## Usage

If you don't have a running instance of seer, then run the docker image:
```bash
docker run -d -p 8080:8080 cshenton/seer
```

Then, to interact over localhost
```python
import datetime
import seer

# Input data, parameters
host = "localhost:8080"
name = "myStream"
period = 3600
times = [...]
values = [...]
forecast_length = 100

# Connect to the server and create a stream
client = seer.Client(host)
client.create_stream(name, period)

# Feed in most of the data, generate a forecast
client.update_stream(name, times, values)
f = client.get_forecast(name, forecast_length)

# Graph the forecast against the true result
def graph(times, values, forecast):
    pass

graph(times, values, f)
```

## (For Contributors) Generating gRPC stubs

Assuming this repo is stored in `cshenton/seer-python`, next to `cshenton/seer`,
we generate client stubs with:

```bash
# Generates seer_pb2.py and seer_pb2_grpc.py
python -m grpc_tools.protoc -I ../seer/seer --python_out=./seer --grpc_python_out=./seer ../seer/seer/seer.proto
```

Then, because the grpc devs don't care about python 3, we need to fix the relative imports.
```python
# in seer_pb2_grpc.py
# From this
import seer_pb2 as seer__pb2

# To this
from . import seer_pb2 as seer__pb2
```