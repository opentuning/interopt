import pytest
from interopt.search_space import SearchSpace, Metric, Objective

class TestSearchSpace:
    @pytest.fixture
    def sample_params(self):
        return [
            {
                'name': 'param1',
                'type': 'INTEGER',
                'default': 5,
                'bounds': (0, 10)
            },
            {
                'name': 'param2',
                'type': 'CATEGORICAL',
                'default': 0,
                'categories': [0, 1, 2]
            }
        ]

    @pytest.fixture
    def sample_metrics(self):
        return [Metric('compute_time', 0, True)]

    @pytest.fixture
    def sample_objectives(self, sample_metrics):
        return [Objective('compute_time', sample_metrics[0], True)]

    def test_search_space_creation(self, sample_params, sample_metrics, sample_objectives):
        space = SearchSpace(
            params=sample_params,
            metrics=sample_metrics,
            objectives=sample_objectives
        )
        assert len(space.params) == 2
        assert space.params[0].name == 'param1'
        assert space.params[1].name == 'param2'

    def test_invalid_param_type(self):
        with pytest.raises(ValueError):
            SearchSpace(
                params=[{'name': 'test', 'type': 'INVALID_TYPE'}],
                metrics=[],
                objectives=[]
            )
