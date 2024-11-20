from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShutdownRequest(_message.Message):
    __slots__ = ("shutdown",)
    SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
    shutdown: bool
    def __init__(self, shutdown: bool = ...) -> None: ...

class ShutdownResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ConfigurationRequest(_message.Message):
    __slots__ = ("configurations", "output_data_file", "study_name", "fidelities")
    CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DATA_FILE_FIELD_NUMBER: _ClassVar[int]
    STUDY_NAME_FIELD_NUMBER: _ClassVar[int]
    FIDELITIES_FIELD_NUMBER: _ClassVar[int]
    configurations: Configuration
    output_data_file: str
    study_name: str
    fidelities: Fidelities
    def __init__(self, configurations: _Optional[_Union[Configuration, _Mapping]] = ..., output_data_file: _Optional[str] = ..., study_name: _Optional[str] = ..., fidelities: _Optional[_Union[Fidelities, _Mapping]] = ...) -> None: ...

class Configuration(_message.Message):
    __slots__ = ("parameters",)
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Parameter
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Parameter, _Mapping]] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.MessageMap[str, Parameter]
    def __init__(self, parameters: _Optional[_Mapping[str, Parameter]] = ...) -> None: ...

class Fidelities(_message.Message):
    __slots__ = ("parameters",)
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Parameter
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Parameter, _Mapping]] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.MessageMap[str, Parameter]
    def __init__(self, parameters: _Optional[_Mapping[str, Parameter]] = ...) -> None: ...

class Parameter(_message.Message):
    __slots__ = ("integer_param", "real_param", "categorical_param", "ordinal_param", "string_param", "permutation_param")
    INTEGER_PARAM_FIELD_NUMBER: _ClassVar[int]
    REAL_PARAM_FIELD_NUMBER: _ClassVar[int]
    CATEGORICAL_PARAM_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_PARAM_FIELD_NUMBER: _ClassVar[int]
    STRING_PARAM_FIELD_NUMBER: _ClassVar[int]
    PERMUTATION_PARAM_FIELD_NUMBER: _ClassVar[int]
    integer_param: IntegerParam
    real_param: RealParam
    categorical_param: CategoricalParam
    ordinal_param: OrdinalParam
    string_param: StringParam
    permutation_param: PermutationParam
    def __init__(self, integer_param: _Optional[_Union[IntegerParam, _Mapping]] = ..., real_param: _Optional[_Union[RealParam, _Mapping]] = ..., categorical_param: _Optional[_Union[CategoricalParam, _Mapping]] = ..., ordinal_param: _Optional[_Union[OrdinalParam, _Mapping]] = ..., string_param: _Optional[_Union[StringParam, _Mapping]] = ..., permutation_param: _Optional[_Union[PermutationParam, _Mapping]] = ...) -> None: ...

class IntegerParam(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class RealParam(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class CategoricalParam(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class OrdinalParam(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class StringParam(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class PermutationParam(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class ConfigurationResponse(_message.Message):
    __slots__ = ("metrics", "timestamps", "feasible")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    FEASIBLE_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[Metric]
    timestamps: Timestamp
    feasible: Feasible
    def __init__(self, metrics: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., timestamps: _Optional[_Union[Timestamp, _Mapping]] = ..., feasible: _Optional[_Union[Feasible, _Mapping]] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ("values", "name")
    VALUES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    name: str
    def __init__(self, values: _Optional[_Iterable[float]] = ..., name: _Optional[str] = ...) -> None: ...

class Timestamp(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ...) -> None: ...

class Feasible(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...
