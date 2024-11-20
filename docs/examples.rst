====================================
Examples
====================================

Basic Optimization
----------------
.. code-block:: python

    # Example of basic parameter optimization
    from interopt.study import Study
    from interopt.definition import ProblemDefinition
    # ... rest of example code

Hardware Integration
------------------
.. code-block:: python

    # Example of hardware backend integration
    study = Study(
        benchmark_name="hw_benchmark",
        definition=definition,
        server_addresses=["localhost"],
        port=50051
    )
    # ... rest of example code
