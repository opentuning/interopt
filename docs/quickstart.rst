====================================
Quickstart Guide
====================================

Basic Usage
----------

Here's a simple example of using InterOpt:

.. code-block:: python

    from interopt.study import Study
    from interopt.definition import ProblemDefinition
    from interopt.search_space import SearchSpace, Metric, Objective
    from interopt.parameter import Integer

    # Define your optimization problem
    params = [
        Integer(name="chunk_size", default=16, bounds=(2, 64)),
        Integer(name="unroll_factor", default=2, bounds=(1, 8))
    ]

    metrics = [Metric('compute_time', 0, True)]
    objectives = [Objective('compute_time', metrics[0], True)]
    
    search_space = SearchSpace(params=params, metrics=metrics, objectives=objectives)
    definition = ProblemDefinition("my_problem", search_space)

    # Create a study
    study = Study(
        benchmark_name="my_benchmark",
        definition=definition,
        enable_tabular=True,
        dataset="test",
        enabled_objectives=['compute_time']
    )

    # Query configurations
    result = study.query({
        "chunk_size": 16,
        "unroll_factor": 2
    })