import pytest
from pyzabbix.client import Host

@pytest.fixture(scope='session')
def host():
    return Host()

