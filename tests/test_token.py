from script.deploy import TOTAL_SUPPLY


def test_token(snek_token):
    snek_token.totalSupply() == TOTAL_SUPPLY
