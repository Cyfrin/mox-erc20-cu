import pytest
from boa.test.strategies import strategy
from hypothesis import HealthCheck, given, settings

from contracts.sub_lesson import stateless_fuzz_solvable


@pytest.fixture
def contract():
    return stateless_fuzz_solvable.deploy()


@settings(
    max_examples=1000, suppress_health_check=[HealthCheck.function_scoped_fixture]
)
@given(input_number=strategy("uint256"))
def test_always_returns_input_number_property_any_bounds(contract, input_number):
    """
    Property test to verify the core behavior of always_returns_input_number
    """
    result = int(contract.always_returns_input_number(input_number))
    assert result == input_number, f"Expected {input_number}, got {result}"
