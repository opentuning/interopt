from dataclasses import dataclass
from interopt.search_space import SearchSpace

@dataclass
class ProblemDefinition:
    name: str
    search_space: SearchSpace
