# pragma version 0.4.0
"""
@title snek_token
@license MIT
"""
# @dev We import and implement the `IERC20` interface,
# which is a built-in interface of the Vyper compiler.
from ethereum.ercs import IERC20
implements: IERC20

from ethereum.ercs import IERC20Detailed
implements: IERC20Detailed

# @dev We import and initialise the `ownable` module.
from snekmate.auth import ownable as ow
initializes: ow

# @dev We import and initialise the `erc20` module.
from snekmate.tokens import erc20
initializes: erc20[ownable := ow]

exports: erc20.__interface__

initialSupply: public(uint256)

NAME: constant(String[25]) = "snek_token"
SYMBOL: constant(String[5]) = "SNEK"
DECIMALS: constant(uint8) = 18
EIP712_VERSOIN: constant(String[20]) = "1"

@deploy
def __init__(initial_supply: uint256):
    ow.__init__()
    erc20.__init__(NAME, SYMBOL, DECIMALS, NAME, EIP712_VERSOIN)

    # The following line premints an initial token
    # supply to the `msg.sender`, which takes the
    # underlying `decimals` value into account.
    erc20._mint(msg.sender, initial_supply * 10 ** convert(DECIMALS, uint256))

    # We assign the initial token supply required by
    # the Echidna external harness contract.
    self.initialSupply = erc20.totalSupply