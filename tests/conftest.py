import pytest

from script.deploy import deploy


@pytest.fixture
def snek_token():
    return deploy()
