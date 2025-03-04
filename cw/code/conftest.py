import pytest
from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://target-sandbox.my.com/')


@pytest.fixture(scope='session')
def url_config(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='session')
def browser_config(request):
    return request.config.getoption('--browser')
