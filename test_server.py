import asyncio
import ast
import logging
from typing import Any

from interopt.study import Study
from interopt.definition import ProblemDefinition
from interopt.search_space import SearchSpace, Metric, Objective
from interopt.parameter import Param, Real, String, Ordinal, Integer, Categorical, Permutation, get_param_type
from interopt.runner.grpc_runner.server import Server


def setup_logging():
    """Configure logging with proper format and level"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('server.log'),
            logging.StreamHandler()  # Also print to console
        ]
    )
    # Suppress noisy logs from libraries
    logging.getLogger('asyncio').setLevel(logging.INFO)
    logging.getLogger('grpc').setLevel(logging.INFO)

def create_test_definition():
    # Define parameters based on the data
    params = [
        Integer(
            name="chunk_size",
            default=16,
            bounds=(2, 64)
        ),
        Integer(
            name="unroll_factor",
            default=2,
            bounds=(1, 8)
        ),
        Integer(
            name="omp_chunk_size",
            default=8,
            bounds=(1, 64)
        ),
        Integer(
            name="omp_num_threads",
            default=8,
            bounds=(4, 16)
        ),
        Integer(
            name="omp_scheduling_type",
            default=0,
            bounds=(0, 2)
        ),
        Integer(
            name="omp_monotonic",
            default=0,
            bounds=(0, 1)
        ),
        Integer(
            name="omp_dynamic",
            default=1,
            bounds=(0, 1)
        ),
        Integer(
            name="omp_proc_bind",
            default=0,
            bounds=(0, 1)
        ),
        Permutation(
            name="permutation",
            default="(0, 1, 2, 3, 4)",
            length=5
        )
    ]

    metrics = [
        Metric('compute_time', 0, True),
        Metric('energy', 1, True)
    ]

    objectives = [
        Objective('compute_time', metrics[0], True),
        Objective('energy', metrics[1], True)
    ]

    search_space = SearchSpace(
        params=params,
        metrics=metrics,
        objectives=objectives
    )

    return ProblemDefinition("spmm", search_space)

# Example of how to replace ParamType enum usage
def value_to_param(value: Any, param: Param) -> dict:
    """Convert a value to the appropriate parameter format based on its type"""
    param_type = get_param_type(param)

    if isinstance(param, Integer):
        return {"integer_param": {"value": int(value)}}
    elif isinstance(param, Real):
        return {"real_param": {"value": float(value)}}
    elif isinstance(param, Categorical):
        return {"categorical_param": {"value": int(value)}}
    elif isinstance(param, String):
        return {"string_param": {"value": str(value)}}
    elif isinstance(param, Permutation):
        # Assuming value is a string representation of a tuple
        tuple_value = ast.literal_eval(value)
        return {"permutation_param": {"values": list(tuple_value)}}
    elif isinstance(param, Ordinal):
        return {"ordinal_param": {"value": int(value)}}
    else:
        raise ValueError(f"Unknown parameter type: {param_type}")

def main():
# Setup logging first
    setup_logging()

    logger = logging.getLogger(__name__)
    logger.info("Starting server initialization")
    study = Study(
        benchmark_name="spmm",
        definition=create_test_definition(),
        enable_tabular=True,
        dataset="10k",
        enabled_objectives=['compute_time', 'energy'],
        server_addresses=["localhost"],
        port=50051,
        enable_model=True,
        enable_download=False
    )

    server = Server({"test": study}, {}, grpc_port=50051)
    print("Starting server on port 50051...")
    server.start()

if __name__ == "__main__":
    main()
