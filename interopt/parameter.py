# interopt/parameter.py
from dataclasses import dataclass, field
from typing import Any, Union, List, Optional, Tuple, Callable

@dataclass
class Param:
    """Base parameter class"""
    name: str
    default: Any

@dataclass
class Categorical(Param):
    """Categorical parameter with discrete categories"""
    categories: List[Any]

@dataclass
class Permutation(Param):
    """Permutation parameter with fixed length"""
    length: int

@dataclass
class Boolean(Param):
    """Boolean parameter"""
    pass

@dataclass
class Numeric(Param):
    """Base class for numeric parameters"""
    bounds: Tuple[Union[int, float], Union[int, float]]
    transform: Optional[str] = None

    def __post_init__(self):
        if len(self.bounds) != 2:
            raise ValueError('Bounds must have exactly 2 elements')

@dataclass
class Real(Numeric):
    """Real-valued parameter"""
    pass

@dataclass
class Integer(Numeric):
    """Integer-valued parameter"""
    pass

@dataclass
class IntExponential(Param):
    """Integer parameter with exponential scaling"""
    name: str
    default: Any
    bounds: Tuple[int, int]
    base: int
    transform: Optional[str] = None

@dataclass
class Ordinal(Numeric):
    """Ordinal parameter with discrete ordered values"""
    pass

@dataclass
class String(Param):
    """String parameter"""
    pass

@dataclass
class Constraint:
    """Constraint on parameter values"""
    constraint: Union[Callable[[Any], bool], str]
    dependent_params: List[str]

# Helper functions
def is_numeric(param: Param) -> bool:
    """Check if parameter is numeric type"""
    return isinstance(param, Numeric)

def is_categorical(param: Param) -> bool:
    """Check if parameter is categorical type"""
    return isinstance(param, Categorical)

def is_permutation(param: Param) -> bool:
    """Check if parameter is permutation type"""
    return isinstance(param, Permutation)

def get_param_type(param: Param) -> str:
    """Get string representation of parameter type"""
    return param.__class__.__name__.upper()
