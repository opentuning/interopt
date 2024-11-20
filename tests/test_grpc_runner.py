import pytest
import grpc
import asyncio
from interopt.runner.grpc_runner.main import run_config
from interopt.parameter import Integer, ParamType
from interopt.runner.grpc_runner import config_service_pb2 as cs

class TestGRPCRunner:
    @pytest.fixture
    def sample_parameters(self):
        return [
            Integer(name="param1", default=5, bounds=(0, 10))
        ]

    @pytest.mark.asyncio
    async def test_run_config(self, sample_parameters, mocker):
        # Mock the gRPC stub and response
        mock_response = mocker.Mock()
        mock_response.metrics = [
            mocker.Mock(name="compute_time", values=[1.0])
        ]

        # Mock the gRPC channel and stub
        mock_stub = mocker.AsyncMock()
        mock_stub.RunConfigurationsClientServer.return_value = mock_response
        mock_channel = mocker.AsyncMock()
        mock_channel.__aenter__.return_value = mocker.Mock()

        with mocker.patch('grpc.aio.insecure_channel', return_value=mock_channel):
            result = await run_config(
                {"param1": "5"},
                sample_parameters,
                {},
                [],
                "dummy_url"
            )

        assert "compute_time" in result
        assert result["compute_time"] == [1.0]

    def test_value_to_param_conversion(self):
        from interopt.runner.grpc_runner.main import value_to_param
        
        # Test integer conversion
        int_param = value_to_param("42", ParamType.INTEGER)
        assert isinstance(int_param, cs.Parameter)
        assert int_param.integer_param.value == 42

        # Test invalid type
        with pytest.raises(ValueError):
            value_to_param("42", "INVALID_TYPE")
