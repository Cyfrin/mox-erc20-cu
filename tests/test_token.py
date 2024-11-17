import boa

from script.deploy import INITIAL_SUPPLY

RANDOM = boa.env.generate_address("non-owner")

def test_token_supply(snek_token):
    assert snek_token.totalSupply() == INITIAL_SUPPLY


def test_token_emits_event(snek_token):
    with boa.env.prank(snek_token.owner()):
        snek_token.transfer(RANDOM, INITIAL_SUPPLY)
        log_owner = snek_token.get_logs()[0].topics[0]
        assert log_owner == snek_token.owner()
    assert snek_token.balanceOf(RANDOM) == INITIAL_SUPPLY