# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: net.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='net.proto',
  package='glove.net',
  serialized_pb='\n\tnet.proto\x12\tglove.net\"s\n\x07Request\x12,\n\x04type\x18\x01 \x02(\x0e\x32\x1e.glove.net.Request.RequestType\":\n\x0bRequestType\x12\r\n\tJOIN_GAME\x10\x00\x12\r\n\tGET_STATE\x10\x01\x12\r\n\tQUIT_GAME\x10\x02\"\x93\x01\n\x08Response\x12.\n\x04type\x18\x01 \x02(\x0e\x32 .glove.net.Response.ResponseType\x12\x1f\n\x05state\x18\x02 \x01(\x0b\x32\x10.glove.net.State\"6\n\x0cResponseType\x12\x08\n\x04OKAY\x10\x00\x12\x08\n\x04NOPE\x10\x01\x12\x07\n\x03\x42\x41\x44\x10\x02\x12\t\n\x05STATE\x10\x04\"h\n\x05State\x12-\n\tgameState\x18\x01 \x02(\x0e\x32\x1a.glove.net.State.GameState\"0\n\tGameState\x12\x0b\n\x07INITIAL\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\t\n\x05\x45NDED\x10\x02')



_REQUEST_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='glove.net.Request.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JOIN_GAME', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_STATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUIT_GAME', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=81,
  serialized_end=139,
)

_RESPONSE_RESPONSETYPE = _descriptor.EnumDescriptor(
  name='ResponseType',
  full_name='glove.net.Response.ResponseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OKAY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOPE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=235,
  serialized_end=289,
)

_STATE_GAMESTATE = _descriptor.EnumDescriptor(
  name='GameState',
  full_name='glove.net.State.GameState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INITIAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENDED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=347,
  serialized_end=395,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='glove.net.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='glove.net.Request.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUEST_REQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=24,
  serialized_end=139,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='glove.net.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='glove.net.Response.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='glove.net.Response.state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSE_RESPONSETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=142,
  serialized_end=289,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='glove.net.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameState', full_name='glove.net.State.gameState', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATE_GAMESTATE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=291,
  serialized_end=395,
)

_REQUEST.fields_by_name['type'].enum_type = _REQUEST_REQUESTTYPE
_REQUEST_REQUESTTYPE.containing_type = _REQUEST;
_RESPONSE.fields_by_name['type'].enum_type = _RESPONSE_RESPONSETYPE
_RESPONSE.fields_by_name['state'].message_type = _STATE
_RESPONSE_RESPONSETYPE.containing_type = _RESPONSE;
_STATE.fields_by_name['gameState'].enum_type = _STATE_GAMESTATE
_STATE_GAMESTATE.containing_type = _STATE;
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['State'] = _STATE

class Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST

  # @@protoc_insertion_point(class_scope:glove.net.Request)

class Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSE

  # @@protoc_insertion_point(class_scope:glove.net.Response)

class State(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATE

  # @@protoc_insertion_point(class_scope:glove.net.State)


# @@protoc_insertion_point(module_scope)
