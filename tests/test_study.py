import pytest
import pandas as pd
from interopt.study import Study, TabularDataset
from interopt.definition import ProblemDefinition
from interopt.search_space import SearchSpace, Metric, Objective
from interopt.parameter import Integer, Categorical

class TestStudy:
    @pytest.fixture
    def sample_definition(self):
        params = [
            Integer(name="param1", default=5, bounds=(0, 10)),
            Categorical(name="param2", default=0, categories=[0, 1, 2])
        ]
        metrics = [Metric('compute_time', 0, True)]
        objectives = [Objective('compute_time', metrics[0], True)]
        search_space = SearchSpace(params=params, metrics=metrics, objectives=objectives)
        return ProblemDefinition("test_problem", search_space)

    @pytest.fixture
    def sample_study(self, sample_definition):
        return Study(
            benchmark_name="test_benchmark",
            definition=sample_definition,
            enable_tabular=True,
            dataset="test_dataset",
            enabled_objectives=['compute_time'],
            enable_model=False,
            enable_download=False
        )

    def test_study_initialization(self, sample_study):
        assert sample_study.benchmark_name == "test_benchmark"
        assert sample_study.enable_tabular == True
        assert sample_study.enable_model == False
        assert len(sample_study.parameters) == 2

    @pytest.mark.asyncio
    async def test_study_query(self, sample_study, mocker):
        # Mock the necessary components
        mock_result = pd.DataFrame({
            'compute_time': [1.0]
        }, index=pd.MultiIndex.from_tuples([(5, 0)], names=['param1', 'param2']))
        
        # Mock the software query
        mocker.patch.object(
            sample_study.software_query,
            'query_software',
            return_value=mock_result
        )

        result = await sample_study.query_async(
            {'param1': 5, 'param2': 0},
            {}
        )
        assert 'compute_time' in result
        assert result['compute_time'] == 1.0
