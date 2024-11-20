import pytest
from interopt.parameter import (
    ParamType, Param, Categorical, Integer, Real, Permutation,
    String, Ordinal, IntExponential, Constraint
)

class TestParameters:
    def test_categorical_param(self):
        param = Categorical(
            name="test_cat",
            default=0,
            categories=[0, 1, 2]
        )
        assert param.param_type_enum == ParamType.CATEGORICAL
        assert param.name == "test_cat"
        assert param.default == 0
        assert param.categories == [0, 1, 2]

    def test_integer_param(self):
        param = Integer(
            name="test_int",
            default=5,
            bounds=(0, 10)
        )
        assert param.param_type_enum == ParamType.INTEGER
        assert param.name == "test_int"
        assert param.default == 5
        assert param.bounds == (0, 10)

    def test_real_param(self):
        param = Real(
            name="test_real",
            default=0.5,
            bounds=(0.0, 1.0)
        )
        assert param.param_type_enum == ParamType.REAL
        assert param.bounds == (0.0, 1.0)

    def test_invalid_bounds(self):
        with pytest.raises(ValueError):
            Real(
                name="test_real",
                default=0.5,
                bounds=(0.0,)  # Invalid bounds
            )

