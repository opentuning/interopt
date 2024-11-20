from dataclasses import dataclass, field
from typing import List
from interopt.parameter import (
    Param, Constraint
)

@dataclass
class Metric:
    """Represents a metric to be measured"""
    name: str
    index: int
    singular: bool

@dataclass
class Objective:
    """Represents an optimization objective"""
    name: str
    metric: Metric
    minimize: bool

@dataclass
class SearchSpace:
    """Defines the search space for optimization"""
    params: List[Param]
    metrics: List[Metric]
    objectives: List[Objective]
    constraints: List[Constraint] = field(default_factory=list)
    fidelity_params: List[Param] = field(default_factory=list)
