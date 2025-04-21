from eth_utils import to_wei, to_bytes
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network

from contracts import snek_token


def moccasin_main():
    contract_addy = "0x60074aD7A8e789d4fDeebB40Eb04B5000d6fE6eE"
    snek = snek_token.at(contract_addy)
    snek.constructor_calldata = to_bytes(
        hexstr="0x00000000000000000000000000000000000000000000003635c9adc5dea00000"
    )

    active_network = get_active_network()
    result = active_network.moccasin_verify(snek)
    result.wait_for_verification()
