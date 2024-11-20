import argparse

from interopt.study import Study
from interopt.runner.grpc_runner.server import Server

from bacobench.benchmarks.spmm import get_spmm_definition


def main():
    parser = argparse.ArgumentParser(description="Run a benchmark")
    parser.add_argument('--servers', type=str, help='Benchmark to use', default="spmm")

    args = parser.parse_args()

    study = Study(benchmark_name='spmm', definition=get_spmm_definition(),
                  enable_tabular=True, enable_model=True, dataset='10k',
                  objectives=['compute_time'], server_addresses=args.servers)
    server = Server(study, port=50050)
    server.start()

    #print(study.query({
    #    'tuned_sp0': 4096,
    #    'tuned_gs0': 16,
    #    'tuned_stride': 2,
    #    'tuned_sp1': 1024,
    #    'tuned_ls0': 16
    #}))

if __name__ == "__main__":
    main()
