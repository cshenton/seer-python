# Seer Python Client
The python client for the seer forecasting server.


## Generating gRPC stubs

Assuming this repo is stored in `cshenton/seer-python`, next to `cshenton/seer`,
we generate client stubs with:

```bash
# Generates seer_pb2.py and seer_pb2_grpc.py
python -m grpc_tools.protoc -I ../seer/seer --python_out=./seer --grpc_python_out=./seer ../seer/seer/seer.proto
```