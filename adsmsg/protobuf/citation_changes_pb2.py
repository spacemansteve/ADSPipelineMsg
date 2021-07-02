# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: citation_changes.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import status_pb2 as status__pb2
from . import citation_changes_content_type_pb2 as citation__changes__content__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='citation_changes.proto',
  package='adsmsg',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16\x63itation_changes.proto\x12\x06\x61\x64smsg\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0cstatus.proto\x1a#citation_changes_content_type.proto\":\n\x0f\x43itationChanges\x12\'\n\x07\x63hanges\x18\x01 \x03(\x0b\x32\x16.adsmsg.CitationChange\"\xda\x01\n\x0e\x43itationChange\x12\x0e\n\x06\x63iting\x18\x01 \x01(\t\x12\r\n\x05\x63ited\x18\x02 \x01(\t\x12\x37\n\x0c\x63ontent_type\x18\x03 \x01(\x0e\x32!.adsmsg.CitationChangeContentType\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x10\n\x08resolved\x18\x05 \x01(\x08\x12\x1e\n\x06status\x18\x06 \x01(\x0e\x32\x0e.adsmsg.Status\x12-\n\ttimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestampb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,status__pb2.DESCRIPTOR,citation__changes__content__type__pb2.DESCRIPTOR,])




_CITATIONCHANGES = _descriptor.Descriptor(
  name='CitationChanges',
  full_name='adsmsg.CitationChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='changes', full_name='adsmsg.CitationChanges.changes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=118,
  serialized_end=176,
)


_CITATIONCHANGE = _descriptor.Descriptor(
  name='CitationChange',
  full_name='adsmsg.CitationChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='citing', full_name='adsmsg.CitationChange.citing', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cited', full_name='adsmsg.CitationChange.cited', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='adsmsg.CitationChange.content_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='adsmsg.CitationChange.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolved', full_name='adsmsg.CitationChange.resolved', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.CitationChange.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='adsmsg.CitationChange.timestamp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=179,
  serialized_end=397,
)

_CITATIONCHANGES.fields_by_name['changes'].message_type = _CITATIONCHANGE
_CITATIONCHANGE.fields_by_name['content_type'].enum_type = citation__changes__content__type__pb2._CITATIONCHANGECONTENTTYPE
_CITATIONCHANGE.fields_by_name['status'].enum_type = status__pb2._STATUS
_CITATIONCHANGE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['CitationChanges'] = _CITATIONCHANGES
DESCRIPTOR.message_types_by_name['CitationChange'] = _CITATIONCHANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CitationChanges = _reflection.GeneratedProtocolMessageType('CitationChanges', (_message.Message,), {
  'DESCRIPTOR' : _CITATIONCHANGES,
  '__module__' : 'citation_changes_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.CitationChanges)
  })
_sym_db.RegisterMessage(CitationChanges)

CitationChange = _reflection.GeneratedProtocolMessageType('CitationChange', (_message.Message,), {
  'DESCRIPTOR' : _CITATIONCHANGE,
  '__module__' : 'citation_changes_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.CitationChange)
  })
_sym_db.RegisterMessage(CitationChange)


# @@protoc_insertion_point(module_scope)
