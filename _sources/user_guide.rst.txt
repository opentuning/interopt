====================================
User Guide
====================================

Core Concepts
------------

Problem Definition
~~~~~~~~~~~~~~~~
The core of InterOpt is the ``ProblemDefinition`` class, which defines your optimization problem through:

- Parameters to optimize
- Metrics to measure
- Objectives to optimize

Search Space
~~~~~~~~~~~
The ``SearchSpace`` class defines the valid parameter combinations through:

- Parameter definitions (type, bounds, constraints)
- Metric definitions
- Objective definitions

Studies
~~~~~~~
The ``Study`` class manages the optimization process:

- Handles communication with hardware/software backends
- Manages tabular datasets
- Integrates surrogate models
- Provides unified query interface

Parameter Types
-------------
InterOpt supports several parameter types:

- Integer: Discrete integer values within bounds
- Real: Continuous real values within bounds
- Categorical: Discrete categories
- Permutation: Ordered sequences
- String: Text values
- Ordinal: Ordered discrete values