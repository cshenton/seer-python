# Seer Python Client
The python client for the seer forecasting server.

## Usage
```python
import datetime
import seer

# Input data, parameters
name = "myStream"
period = 3600
times = [...]
values = [...]
forecast_length = 100

# Connect to the server and create a stream
client = seer.Client("localhost:8080")
client.create_stream(name, period)

# Feed in most of the data, generate a forecast
client.update_stream(name, times, values)
f = client.get_forecast(name, forecast_length)

# Graph the forecast against the true result
def graph(times, values, forecast):
    pass

graph(times, values, f)
```

## Generating gRPC stubs

Assuming this repo is stored in `cshenton/seer-python`, next to `cshenton/seer`,
we generate client stubs with:

```bash
# Generates seer_pb2.py and seer_pb2_grpc.py
python -m grpc_tools.protoc -I ../seer/seer --python_out=./seer --grpc_python_out=./seer ../seer/seer/seer.proto
```

Then, because the grpc devs don't care about python 3, we need to change.
```python
# in seer_pb2_grpc.py
# From this
import seer_pb2 as seer__pb2

# To this
from . import seer_pb2 as seer__pb2
```