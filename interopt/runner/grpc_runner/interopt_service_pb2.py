# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: interopt_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'interopt_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import config_service_pb2 as config__service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16interopt_service.proto\x1a\x14\x63onfig_service.proto\"%\n\x0fGetStudyRequest\x12\x12\n\nstudy_name\x18\x01 \x01(\t\"\xde\x01\n\x10GetStudyResponse\x12\x12\n\nstudy_name\x18\x01 \x01(\t\x12\x14\n\x0cproblem_name\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x03 \x01(\t\x12\x16\n\x0e\x65nable_tabular\x18\x04 \x01(\x08\x12\x14\n\x0c\x65nable_model\x18\x05 \x01(\x08\x12\x17\n\x0f\x65nable_download\x18\x06 \x01(\x08\x12\x19\n\x11\x65nable_objectives\x18\x07 \x03(\t\x12-\n\x12server_connections\x18\x08 \x03(\x0b\x32\x11.ServerConnection\"\xe0\x01\n\x12UpdateStudyRequest\x12\x12\n\nstudy_name\x18\x01 \x01(\t\x12\x14\n\x0cproblem_name\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x03 \x01(\t\x12\x16\n\x0e\x65nable_tabular\x18\x04 \x01(\x08\x12\x14\n\x0c\x65nable_model\x18\x05 \x01(\x08\x12\x17\n\x0f\x65nable_download\x18\x06 \x01(\x08\x12\x19\n\x11\x65nable_objectives\x18\x07 \x03(\t\x12-\n\x12server_connections\x18\x08 \x03(\x0b\x32\x11.ServerConnection\"&\n\x13UpdateStudyResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\xdf\x01\n\x11SetupStudyRequest\x12\x12\n\nstudy_name\x18\x01 \x01(\t\x12\x14\n\x0cproblem_name\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x03 \x01(\t\x12\x16\n\x0e\x65nable_tabular\x18\x04 \x01(\x08\x12\x14\n\x0c\x65nable_model\x18\x05 \x01(\x08\x12\x17\n\x0f\x65nable_download\x18\x06 \x01(\x08\x12\x19\n\x11\x65nable_objectives\x18\x07 \x03(\t\x12-\n\x12server_connections\x18\x08 \x03(\x0b\x32\x11.ServerConnection\"%\n\x12SetupStudyResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"?\n\x10ServerConnection\x12\x16\n\x0eserver_address\x18\x01 \x01(\t\x12\x13\n\x0bserver_port\x18\x02 \x01(\x05\x32\xa7\x02\n\x0fInteroptService\x12\x41\n\x10RunConfiguration\x12\x15.ConfigurationRequest\x1a\x16.ConfigurationResponse\x12/\n\x08Shutdown\x12\x10.ShutdownRequest\x1a\x11.ShutdownResponse\x12\x35\n\nSetupStudy\x12\x12.SetupStudyRequest\x1a\x13.SetupStudyResponse\x12/\n\x08GetStudy\x12\x10.GetStudyRequest\x1a\x11.GetStudyResponse\x12\x38\n\x0bUpdateStudy\x12\x13.UpdateStudyRequest\x1a\x14.UpdateStudyResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'interopt_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETSTUDYREQUEST']._serialized_start=48
  _globals['_GETSTUDYREQUEST']._serialized_end=85
  _globals['_GETSTUDYRESPONSE']._serialized_start=88
  _globals['_GETSTUDYRESPONSE']._serialized_end=310
  _globals['_UPDATESTUDYREQUEST']._serialized_start=313
  _globals['_UPDATESTUDYREQUEST']._serialized_end=537
  _globals['_UPDATESTUDYRESPONSE']._serialized_start=539
  _globals['_UPDATESTUDYRESPONSE']._serialized_end=577
  _globals['_SETUPSTUDYREQUEST']._serialized_start=580
  _globals['_SETUPSTUDYREQUEST']._serialized_end=803
  _globals['_SETUPSTUDYRESPONSE']._serialized_start=805
  _globals['_SETUPSTUDYRESPONSE']._serialized_end=842
  _globals['_SERVERCONNECTION']._serialized_start=844
  _globals['_SERVERCONNECTION']._serialized_end=907
  _globals['_INTEROPTSERVICE']._serialized_start=910
  _globals['_INTEROPTSERVICE']._serialized_end=1205
# @@protoc_insertion_point(module_scope)
