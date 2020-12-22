# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage_mobile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import error_pb2 as error__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='storage_mobile.proto',
  package='storage',
  syntax='proto3',
  serialized_options=b'\n\033network.celer.proto.storageB\rStorageMobileZ+github.com/celer-network/x-proto-go/storage\272\002\007Storage',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14storage_mobile.proto\x12\x07storage\x1a\x0b\x65rror.proto\"\x8b\x01\n\x18RecordInviterInfoRequest\x12\x18\n\x10inviter_username\x18\x01 \x01(\t\x12\x17\n\x0finvitation_code\x18\x02 \x01(\t\x12\x1a\n\x12inviter_avatar_url\x18\x03 \x01(\t\x12 \n\x18inviter_visible_username\x18\x04 \x01(\t\"=\n\x19RecordInviterInfoResponse\x12 \n\x05\x65rror\x18\x01 \x01(\x0b\x32\x11.err.BackendError2f\n\x06Mobile\x12\\\n\x11RecordInviterInfo\x12!.storage.RecordInviterInfoRequest\x1a\".storage.RecordInviterInfoResponse\"\x00\x42\x63\n\x1bnetwork.celer.proto.storageB\rStorageMobileZ+github.com/celer-network/x-proto-go/storage\xba\x02\x07Storageb\x06proto3'
  ,
  dependencies=[error__pb2.DESCRIPTOR,])




_RECORDINVITERINFOREQUEST = _descriptor.Descriptor(
  name='RecordInviterInfoRequest',
  full_name='storage.RecordInviterInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inviter_username', full_name='storage.RecordInviterInfoRequest.inviter_username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invitation_code', full_name='storage.RecordInviterInfoRequest.invitation_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inviter_avatar_url', full_name='storage.RecordInviterInfoRequest.inviter_avatar_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inviter_visible_username', full_name='storage.RecordInviterInfoRequest.inviter_visible_username', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=47,
  serialized_end=186,
)


_RECORDINVITERINFORESPONSE = _descriptor.Descriptor(
  name='RecordInviterInfoResponse',
  full_name='storage.RecordInviterInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='storage.RecordInviterInfoResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=188,
  serialized_end=249,
)

_RECORDINVITERINFORESPONSE.fields_by_name['error'].message_type = error__pb2._BACKENDERROR
DESCRIPTOR.message_types_by_name['RecordInviterInfoRequest'] = _RECORDINVITERINFOREQUEST
DESCRIPTOR.message_types_by_name['RecordInviterInfoResponse'] = _RECORDINVITERINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecordInviterInfoRequest = _reflection.GeneratedProtocolMessageType('RecordInviterInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECORDINVITERINFOREQUEST,
  '__module__' : 'storage_mobile_pb2'
  # @@protoc_insertion_point(class_scope:storage.RecordInviterInfoRequest)
  })
_sym_db.RegisterMessage(RecordInviterInfoRequest)

RecordInviterInfoResponse = _reflection.GeneratedProtocolMessageType('RecordInviterInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECORDINVITERINFORESPONSE,
  '__module__' : 'storage_mobile_pb2'
  # @@protoc_insertion_point(class_scope:storage.RecordInviterInfoResponse)
  })
_sym_db.RegisterMessage(RecordInviterInfoResponse)


DESCRIPTOR._options = None

_MOBILE = _descriptor.ServiceDescriptor(
  name='Mobile',
  full_name='storage.Mobile',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=251,
  serialized_end=353,
  methods=[
  _descriptor.MethodDescriptor(
    name='RecordInviterInfo',
    full_name='storage.Mobile.RecordInviterInfo',
    index=0,
    containing_service=None,
    input_type=_RECORDINVITERINFOREQUEST,
    output_type=_RECORDINVITERINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MOBILE)

DESCRIPTOR.services_by_name['Mobile'] = _MOBILE

# @@protoc_insertion_point(module_scope)
