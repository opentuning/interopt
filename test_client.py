import asyncio
import logging

from interopt.study import Study
from interopt.definition import ProblemDefinition
from interopt.search_space import SearchSpace, Metric, Objective
from interopt.parameter import Integer, Categorical, Permutation

def setup_logging():
    """Configure logging with proper format and level"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('client.log'),
            logging.StreamHandler()  # Also print to console
        ]
    )
    # Suppress noisy logs from libraries
    logging.getLogger('asyncio').setLevel(logging.WARNING)
    logging.getLogger('grpc').setLevel(logging.WARNING)

def create_test_definition():
    # Define parameters based on the data
    params = [
        Integer(name="chunk_size", default=16, bounds=(2, 64)),
        Integer(name="unroll_factor", default=2, bounds=(1, 8)),
        Integer(name="omp_chunk_size", default=8, bounds=(1, 64)),
        Integer(name="omp_num_threads", default=8, bounds=(4, 16)),
        Integer(name="omp_scheduling_type", default=0, bounds=(0, 2)),
        Integer(name="omp_monotonic", default=0, bounds=(0, 1)),
        Integer(name="omp_dynamic", default=1, bounds=(0, 1)),
        Integer(name="omp_proc_bind", default=0, bounds=(0, 1)),
        Permutation(name="permutation", default="(0, 1, 2, 3, 4)", length=5)
    ]
    
    # Define metrics and objectives
    metrics = [
        Metric('compute_time', 0, True),
        Metric('energy', 1, True)
    ]
    
    objectives = [
        Objective('compute_time', metrics[0], True),
        Objective('energy', metrics[1], True)
    ]
    
    # Create search space
    search_space = SearchSpace(
        params=params,
        metrics=metrics,
        objectives=objectives,
        fidelity_params=[]
    )
    return ProblemDefinition("spmm", search_space)

async def main():
    # Setup logging first
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("Starting client initialization")
    # Create the same definition as the server
    definition = create_test_definition()
    
    # Create a client study
    study = Study(
        benchmark_name="spmm",
        definition=definition,
        enable_tabular=False,
        dataset="10k",
        enabled_objectives=['compute_time', 'energy'],
        server_addresses=["localhost"],
        port=50051,
        enable_model=False,
        enable_download=False
    )
    
    # Test configuration (using one from your data)
    config = {
        "chunk_size": 16,
        "unroll_factor": 2,
        "omp_chunk_size": 8,
        "omp_num_threads": 16,
        "omp_scheduling_type": 2,
        "omp_monotonic": 0,
        "omp_dynamic": 1,
        "omp_proc_bind": 0,
        "permutation": "(1, 0, 2, 3, 4)"
    }
    
    print(f"Testing configuration: {config}")
    result = await study.query_async(config)
    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
