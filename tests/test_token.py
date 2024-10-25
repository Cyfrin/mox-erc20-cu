from script.deploy import INITIAL_SUPPLY


def test_token_supply(snek_token):
    snek_token.totalSupply() == INITIAL_SUPPLY
    snek_token._storage.initialSupply.get() == INITIAL_SUPPLY
