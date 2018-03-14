# seer-python
The python client for seer

## Generating gRPC stubs

We use the following command to generate stubs.
```
python -m grpc_tools.protoc -I ../seer/seer --python_out=. --grpc_python_out=. ../seer/seer/seer.proto
```