# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: seer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='seer.proto',
  package='seer',
  syntax='proto3',
  serialized_pb=_b('\n\nseer.proto\x12\x04seer\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x93\x01\n\x06Stream\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06period\x18\x02 \x01(\x01\x12\x33\n\x0flast_event_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x06\x64omain\x18\x04 \x01(\x0e\x32\x0c.seer.Domain\x12\x0b\n\x03min\x18\x05 \x01(\x01\x12\x0b\n\x03max\x18\x06 \x01(\x01\"B\n\x05\x45vent\x12)\n\x05times\x18\x01 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06values\x18\x02 \x03(\x01\"I\n\x08Interval\x12\x13\n\x0bprobability\x18\x01 \x01(\x01\x12\x13\n\x0blower_bound\x18\x02 \x03(\x01\x12\x13\n\x0bupper_bound\x18\x03 \x03(\x01\"h\n\x08\x46orecast\x12)\n\x05times\x18\x01 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06values\x18\x02 \x03(\x01\x12!\n\tintervals\x18\x03 \x03(\x0b\x32\x0e.seer.Interval\"3\n\x13\x43reateStreamRequest\x12\x1c\n\x06stream\x18\x01 \x01(\x0b\x32\x0c.seer.Stream\" \n\x10GetStreamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"#\n\x13\x44\x65leteStreamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"<\n\x12ListStreamsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x13\n\x0bpage_number\x18\x02 \x01(\x05\"4\n\x13ListStreamsResponse\x12\x1d\n\x07streams\x18\x01 \x03(\x0b\x32\x0c.seer.Stream\"?\n\x13UpdateStreamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x05\x65vent\x18\x02 \x01(\x0b\x32\x0b.seer.Event\"-\n\x12GetForecastRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\t\n\x01n\x18\x02 \x01(\x05*r\n\x06\x44omain\x12\x0e\n\nCONTINUOUS\x10\x00\x12\x14\n\x10\x43ONTINUOUS_RIGHT\x10\x01\x12\x17\n\x13\x43ONTINUOUS_INTERVAL\x10\x02\x12\x12\n\x0e\x44ISCRETE_RIGHT\x10\x03\x12\x15\n\x11\x44ISCRETE_INTERVAL\x10\x04\x32\xf7\x02\n\x04Seer\x12\x39\n\x0c\x43reateStream\x12\x19.seer.CreateStreamRequest\x1a\x0c.seer.Stream\"\x00\x12\x33\n\tGetStream\x12\x16.seer.GetStreamRequest\x1a\x0c.seer.Stream\"\x00\x12\x39\n\x0cUpdateStream\x12\x19.seer.UpdateStreamRequest\x1a\x0c.seer.Stream\"\x00\x12\x43\n\x0c\x44\x65leteStream\x12\x19.seer.DeleteStreamRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x44\n\x0bListStreams\x12\x18.seer.ListStreamsRequest\x1a\x19.seer.ListStreamsResponse\"\x00\x12\x39\n\x0bGetForecast\x12\x18.seer.GetForecastRequest\x1a\x0e.seer.Forecast\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_DOMAIN = _descriptor.EnumDescriptor(
  name='Domain',
  full_name='seer.Domain',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTINUOUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINUOUS_RIGHT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINUOUS_INTERVAL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCRETE_RIGHT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCRETE_INTERVAL', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=833,
  serialized_end=947,
)
_sym_db.RegisterEnumDescriptor(_DOMAIN)

Domain = enum_type_wrapper.EnumTypeWrapper(_DOMAIN)
CONTINUOUS = 0
CONTINUOUS_RIGHT = 1
CONTINUOUS_INTERVAL = 2
DISCRETE_RIGHT = 3
DISCRETE_INTERVAL = 4



_STREAM = _descriptor.Descriptor(
  name='Stream',
  full_name='seer.Stream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='seer.Stream.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='seer.Stream.period', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_event_time', full_name='seer.Stream.last_event_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='seer.Stream.domain', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='seer.Stream.min', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='seer.Stream.max', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=230,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='seer.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='times', full_name='seer.Event.times', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='seer.Event.values', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=298,
)


_INTERVAL = _descriptor.Descriptor(
  name='Interval',
  full_name='seer.Interval',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='probability', full_name='seer.Interval.probability', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lower_bound', full_name='seer.Interval.lower_bound', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upper_bound', full_name='seer.Interval.upper_bound', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=373,
)


_FORECAST = _descriptor.Descriptor(
  name='Forecast',
  full_name='seer.Forecast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='times', full_name='seer.Forecast.times', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='seer.Forecast.values', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intervals', full_name='seer.Forecast.intervals', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=479,
)


_CREATESTREAMREQUEST = _descriptor.Descriptor(
  name='CreateStreamRequest',
  full_name='seer.CreateStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream', full_name='seer.CreateStreamRequest.stream', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=532,
)


_GETSTREAMREQUEST = _descriptor.Descriptor(
  name='GetStreamRequest',
  full_name='seer.GetStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='seer.GetStreamRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=534,
  serialized_end=566,
)


_DELETESTREAMREQUEST = _descriptor.Descriptor(
  name='DeleteStreamRequest',
  full_name='seer.DeleteStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='seer.DeleteStreamRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=603,
)


_LISTSTREAMSREQUEST = _descriptor.Descriptor(
  name='ListStreamsRequest',
  full_name='seer.ListStreamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='seer.ListStreamsRequest.page_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_number', full_name='seer.ListStreamsRequest.page_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=665,
)


_LISTSTREAMSRESPONSE = _descriptor.Descriptor(
  name='ListStreamsResponse',
  full_name='seer.ListStreamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='streams', full_name='seer.ListStreamsResponse.streams', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=667,
  serialized_end=719,
)


_UPDATESTREAMREQUEST = _descriptor.Descriptor(
  name='UpdateStreamRequest',
  full_name='seer.UpdateStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='seer.UpdateStreamRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='seer.UpdateStreamRequest.event', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=721,
  serialized_end=784,
)


_GETFORECASTREQUEST = _descriptor.Descriptor(
  name='GetForecastRequest',
  full_name='seer.GetForecastRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='seer.GetForecastRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n', full_name='seer.GetForecastRequest.n', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=786,
  serialized_end=831,
)

_STREAM.fields_by_name['last_event_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STREAM.fields_by_name['domain'].enum_type = _DOMAIN
_EVENT.fields_by_name['times'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FORECAST.fields_by_name['times'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FORECAST.fields_by_name['intervals'].message_type = _INTERVAL
_CREATESTREAMREQUEST.fields_by_name['stream'].message_type = _STREAM
_LISTSTREAMSRESPONSE.fields_by_name['streams'].message_type = _STREAM
_UPDATESTREAMREQUEST.fields_by_name['event'].message_type = _EVENT
DESCRIPTOR.message_types_by_name['Stream'] = _STREAM
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['Interval'] = _INTERVAL
DESCRIPTOR.message_types_by_name['Forecast'] = _FORECAST
DESCRIPTOR.message_types_by_name['CreateStreamRequest'] = _CREATESTREAMREQUEST
DESCRIPTOR.message_types_by_name['GetStreamRequest'] = _GETSTREAMREQUEST
DESCRIPTOR.message_types_by_name['DeleteStreamRequest'] = _DELETESTREAMREQUEST
DESCRIPTOR.message_types_by_name['ListStreamsRequest'] = _LISTSTREAMSREQUEST
DESCRIPTOR.message_types_by_name['ListStreamsResponse'] = _LISTSTREAMSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateStreamRequest'] = _UPDATESTREAMREQUEST
DESCRIPTOR.message_types_by_name['GetForecastRequest'] = _GETFORECASTREQUEST
DESCRIPTOR.enum_types_by_name['Domain'] = _DOMAIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Stream = _reflection.GeneratedProtocolMessageType('Stream', (_message.Message,), dict(
  DESCRIPTOR = _STREAM,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.Stream)
  ))
_sym_db.RegisterMessage(Stream)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.Event)
  ))
_sym_db.RegisterMessage(Event)

Interval = _reflection.GeneratedProtocolMessageType('Interval', (_message.Message,), dict(
  DESCRIPTOR = _INTERVAL,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.Interval)
  ))
_sym_db.RegisterMessage(Interval)

Forecast = _reflection.GeneratedProtocolMessageType('Forecast', (_message.Message,), dict(
  DESCRIPTOR = _FORECAST,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.Forecast)
  ))
_sym_db.RegisterMessage(Forecast)

CreateStreamRequest = _reflection.GeneratedProtocolMessageType('CreateStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESTREAMREQUEST,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.CreateStreamRequest)
  ))
_sym_db.RegisterMessage(CreateStreamRequest)

GetStreamRequest = _reflection.GeneratedProtocolMessageType('GetStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSTREAMREQUEST,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.GetStreamRequest)
  ))
_sym_db.RegisterMessage(GetStreamRequest)

DeleteStreamRequest = _reflection.GeneratedProtocolMessageType('DeleteStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETESTREAMREQUEST,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.DeleteStreamRequest)
  ))
_sym_db.RegisterMessage(DeleteStreamRequest)

ListStreamsRequest = _reflection.GeneratedProtocolMessageType('ListStreamsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTSTREAMSREQUEST,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.ListStreamsRequest)
  ))
_sym_db.RegisterMessage(ListStreamsRequest)

ListStreamsResponse = _reflection.GeneratedProtocolMessageType('ListStreamsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTSTREAMSRESPONSE,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.ListStreamsResponse)
  ))
_sym_db.RegisterMessage(ListStreamsResponse)

UpdateStreamRequest = _reflection.GeneratedProtocolMessageType('UpdateStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATESTREAMREQUEST,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.UpdateStreamRequest)
  ))
_sym_db.RegisterMessage(UpdateStreamRequest)

GetForecastRequest = _reflection.GeneratedProtocolMessageType('GetForecastRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFORECASTREQUEST,
  __module__ = 'seer_pb2'
  # @@protoc_insertion_point(class_scope:seer.GetForecastRequest)
  ))
_sym_db.RegisterMessage(GetForecastRequest)



_SEER = _descriptor.ServiceDescriptor(
  name='Seer',
  full_name='seer.Seer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=950,
  serialized_end=1325,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateStream',
    full_name='seer.Seer.CreateStream',
    index=0,
    containing_service=None,
    input_type=_CREATESTREAMREQUEST,
    output_type=_STREAM,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStream',
    full_name='seer.Seer.GetStream',
    index=1,
    containing_service=None,
    input_type=_GETSTREAMREQUEST,
    output_type=_STREAM,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateStream',
    full_name='seer.Seer.UpdateStream',
    index=2,
    containing_service=None,
    input_type=_UPDATESTREAMREQUEST,
    output_type=_STREAM,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteStream',
    full_name='seer.Seer.DeleteStream',
    index=3,
    containing_service=None,
    input_type=_DELETESTREAMREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListStreams',
    full_name='seer.Seer.ListStreams',
    index=4,
    containing_service=None,
    input_type=_LISTSTREAMSREQUEST,
    output_type=_LISTSTREAMSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetForecast',
    full_name='seer.Seer.GetForecast',
    index=5,
    containing_service=None,
    input_type=_GETFORECASTREQUEST,
    output_type=_FORECAST,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEER)

DESCRIPTOR.services_by_name['Seer'] = _SEER

# @@protoc_insertion_point(module_scope)