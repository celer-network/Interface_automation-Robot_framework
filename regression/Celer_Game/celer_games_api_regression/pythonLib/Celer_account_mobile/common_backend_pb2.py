# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common_backend.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_mobile_pb2 as common__mobile__pb2
# from Celer_Game.celer_games_api_regression.pythonLib.Celer_invitation_mobile import common_mobile_pb2 as \
#   common__mobile__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common_backend.proto',
  package='common',
  syntax='proto3',
  serialized_options=b'\n\032network.celer.proto.commonB\016CommonInternalZ*github.com/celer-network/x-proto-go/common\272\002\006Common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x63ommon_backend.proto\x12\x06\x63ommon\x1a\x13\x63ommon_mobile.proto\"R\n\x06\x41mount\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12)\n\ntoken_type\x18\x03 \x01(\x0e\x32\x15.common.TokenTypeEnum\"P\n\x16PrizeDistributionChunk\x12\x11\n\tfrom_rank\x18\x01 \x01(\r\x12\x0f\n\x07to_rank\x18\x02 \x01(\r\x12\x12\n\npercentage\x18\x03 \x01(\x01\"/\n\tBasicAuth\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\tBa\n\x1anetwork.celer.proto.commonB\x0e\x43ommonInternalZ*github.com/celer-network/x-proto-go/common\xba\x02\x06\x43ommonb\x06proto3'
  ,
  dependencies=[common__mobile__pb2.DESCRIPTOR,])




_AMOUNT = _descriptor.Descriptor(
  name='Amount',
  full_name='common.Amount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='common.Amount.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='common.Amount.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token_type', full_name='common.Amount.token_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=135,
)


_PRIZEDISTRIBUTIONCHUNK = _descriptor.Descriptor(
  name='PrizeDistributionChunk',
  full_name='common.PrizeDistributionChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_rank', full_name='common.PrizeDistributionChunk.from_rank', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_rank', full_name='common.PrizeDistributionChunk.to_rank', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='percentage', full_name='common.PrizeDistributionChunk.percentage', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=217,
)


_BASICAUTH = _descriptor.Descriptor(
  name='BasicAuth',
  full_name='common.BasicAuth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='common.BasicAuth.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='common.BasicAuth.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=266,
)

_AMOUNT.fields_by_name['token_type'].enum_type = common__mobile__pb2._TOKENTYPEENUM
DESCRIPTOR.message_types_by_name['Amount'] = _AMOUNT
DESCRIPTOR.message_types_by_name['PrizeDistributionChunk'] = _PRIZEDISTRIBUTIONCHUNK
DESCRIPTOR.message_types_by_name['BasicAuth'] = _BASICAUTH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Amount = _reflection.GeneratedProtocolMessageType('Amount', (_message.Message,), {
  'DESCRIPTOR' : _AMOUNT,
  '__module__' : 'common_backend_pb2'
  # @@protoc_insertion_point(class_scope:common.Amount)
  })
_sym_db.RegisterMessage(Amount)

PrizeDistributionChunk = _reflection.GeneratedProtocolMessageType('PrizeDistributionChunk', (_message.Message,), {
  'DESCRIPTOR' : _PRIZEDISTRIBUTIONCHUNK,
  '__module__' : 'common_backend_pb2'
  # @@protoc_insertion_point(class_scope:common.PrizeDistributionChunk)
  })
_sym_db.RegisterMessage(PrizeDistributionChunk)

BasicAuth = _reflection.GeneratedProtocolMessageType('BasicAuth', (_message.Message,), {
  'DESCRIPTOR' : _BASICAUTH,
  '__module__' : 'common_backend_pb2'
  # @@protoc_insertion_point(class_scope:common.BasicAuth)
  })
_sym_db.RegisterMessage(BasicAuth)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
