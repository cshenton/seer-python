"""Seer Client implementation"""
import grpc
import seer.seer_pb2 as seer_pb2
import seer.seer_pb2_grpc as seer_pb2_grpc


class Client(object):
    """Client manages the connection to your seer instance.

    Attributes:
        address (string): The address of the server.
        stub (seer_pb2_grpc.SeerStub): The seer server stub.
    """

    def __init__(self, address):
        """Constructs an instance of Client.

        Args:
            address (string): The address of the server to connect to.
        """
        chan = grpc.insecure_channel(address)
        self.stub = seer_pb2_grpc.SeerStub(chan)
        self.address = address

    def create_stream(self, name, period):
        """Creates a new stream with the given name and periodicity.

        Args:
            name (string): The unique name for the stream.
            period (float): The number of seconds between observations.

        Returns:
            Stream: The newly created stream.
        """
        req = seer_pb2.CreateStreamRequest(
            stream=seer_pb2.Stream(
                name=name,
                period=period,
            )
        )
        stream = self.stub.CreateStream(req)
        return stream

    def get_stream(self, name):
        """Gets the stream from the server with the given name.

        Args:
            name (string): The unique name of the stream.

        Returns:
            Stream: The requested stream.
        """
        req = seer_pb2.GetStreamRequest(name=name)
        stream = self.stub.GetStream(req)
        return stream

    def list_streams(self, page_size, page_number):
        """Gets a list of streams from the server.

        Args:
            page_num (int): The page number >= 1.
            page_size (int): The max number of streams to return.

        Returns:
            List of Streams: The retrieved streams.
        """
        req = seer_pb2.ListStreamsRequest(
            page_size=page_size,
            page_number=page_number,
        )
        resp = self.stub.ListStreams(req)
        return resp.streams

    def update_stream(self, name, times, values):
        """Updates the specified stream with the newly observed data.

        Args:
            name (string): The name of the stream to update.
            times (list of datetime): The times at which new vaues were observed.
            values (list of floats): The newly observed values.

        Returns:
            Stream: The updated stream.
        """
        req = seer_pb2.UpdateStreamRequest(
            name=name,
            event=seer_pb2.Event(
                times=times,
                values=values,
            ),
        )
        stream = self.stub.UpdateStream(req)
        return stream

    def get_forecast(self, name, length):
        """Generates a forecast from the specified stream.

        Args:
            name (string): The name of the stream to forecast from.
            length (int): The number of periods to forecast ahead.

        Returns:
            Forecast: The generated forecast.
        """
        req = seer_pb2.GetForecastRequest(
            name=name,
            n=length,
        )
        forecast = self.stub.GetForecast(req)
        return forecast
