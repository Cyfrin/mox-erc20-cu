from boa.test.strategies import strategy
from hypothesis import settings
from hypothesis.stateful import RuleBasedStateMachine, rule

from contracts.sub_lesson import stateful_fuzz_solvable


class StatefulFuzzer(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.contract = stateful_fuzz_solvable.deploy()

    @rule(new_number=strategy("uint256"))
    def change_number(self, new_number):
        self.contract.change_number(new_number)

    # ------------------------------------------------------------------
    #                           INVARIANTS
    # ------------------------------------------------------------------
    @rule(input_number=strategy("uint256"))
    def input_number_returns_itself(self, input_number):
        result = int(self.contract.always_returns_input_number(input_number))
        assert result == input_number, f"Expected {input_number}, got {result}"


TestStatefulFuzzing = StatefulFuzzer.TestCase
TestStatefulFuzzing.settings = settings(max_examples=10000, stateful_step_count=50)
