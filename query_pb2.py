# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bquery.proto\x12\nscorequery\"8\n\x0cqueryRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06lesson\x18\x03 \x01(\t\"\x1e\n\rqueryResponse\x12\r\n\x05score\x18\x01 \x01(\t2L\n\nqueryScore\x12>\n\x05query\x12\x18.scorequery.queryRequest\x1a\x19.scorequery.queryResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUERYREQUEST._serialized_start=27
  _QUERYREQUEST._serialized_end=83
  _QUERYRESPONSE._serialized_start=85
  _QUERYRESPONSE._serialized_end=115
  _QUERYSCORE._serialized_start=117
  _QUERYSCORE._serialized_end=193
# @@protoc_insertion_point(module_scope)