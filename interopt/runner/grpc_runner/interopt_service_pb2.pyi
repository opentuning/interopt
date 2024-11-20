import config_service_pb2 as _config_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetStudyRequest(_message.Message):
    __slots__ = ("study_name",)
    STUDY_NAME_FIELD_NUMBER: _ClassVar[int]
    study_name: str
    def __init__(self, study_name: _Optional[str] = ...) -> None: ...

class GetStudyResponse(_message.Message):
    __slots__ = ("study_name", "problem_name", "dataset", "enable_tabular", "enable_model", "enable_download", "enable_objectives", "server_connections")
    STUDY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TABULAR_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MODEL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    SERVER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    study_name: str
    problem_name: str
    dataset: str
    enable_tabular: bool
    enable_model: bool
    enable_download: bool
    enable_objectives: _containers.RepeatedScalarFieldContainer[str]
    server_connections: _containers.RepeatedCompositeFieldContainer[ServerConnection]
    def __init__(self, study_name: _Optional[str] = ..., problem_name: _Optional[str] = ..., dataset: _Optional[str] = ..., enable_tabular: bool = ..., enable_model: bool = ..., enable_download: bool = ..., enable_objectives: _Optional[_Iterable[str]] = ..., server_connections: _Optional[_Iterable[_Union[ServerConnection, _Mapping]]] = ...) -> None: ...

class UpdateStudyRequest(_message.Message):
    __slots__ = ("study_name", "problem_name", "dataset", "enable_tabular", "enable_model", "enable_download", "enable_objectives", "server_connections")
    STUDY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TABULAR_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MODEL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    SERVER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    study_name: str
    problem_name: str
    dataset: str
    enable_tabular: bool
    enable_model: bool
    enable_download: bool
    enable_objectives: _containers.RepeatedScalarFieldContainer[str]
    server_connections: _containers.RepeatedCompositeFieldContainer[ServerConnection]
    def __init__(self, study_name: _Optional[str] = ..., problem_name: _Optional[str] = ..., dataset: _Optional[str] = ..., enable_tabular: bool = ..., enable_model: bool = ..., enable_download: bool = ..., enable_objectives: _Optional[_Iterable[str]] = ..., server_connections: _Optional[_Iterable[_Union[ServerConnection, _Mapping]]] = ...) -> None: ...

class UpdateStudyResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class SetupStudyRequest(_message.Message):
    __slots__ = ("study_name", "problem_name", "dataset", "enable_tabular", "enable_model", "enable_download", "enable_objectives", "server_connections")
    STUDY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TABULAR_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MODEL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    SERVER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    study_name: str
    problem_name: str
    dataset: str
    enable_tabular: bool
    enable_model: bool
    enable_download: bool
    enable_objectives: _containers.RepeatedScalarFieldContainer[str]
    server_connections: _containers.RepeatedCompositeFieldContainer[ServerConnection]
    def __init__(self, study_name: _Optional[str] = ..., problem_name: _Optional[str] = ..., dataset: _Optional[str] = ..., enable_tabular: bool = ..., enable_model: bool = ..., enable_download: bool = ..., enable_objectives: _Optional[_Iterable[str]] = ..., server_connections: _Optional[_Iterable[_Union[ServerConnection, _Mapping]]] = ...) -> None: ...

class SetupStudyResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ServerConnection(_message.Message):
    __slots__ = ("server_address", "server_port")
    SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    server_address: str
    server_port: int
    def __init__(self, server_address: _Optional[str] = ..., server_port: _Optional[int] = ...) -> None: ...
