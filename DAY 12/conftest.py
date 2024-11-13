import pytest


@pytest.fixture()
def setup(scope="class"):
    data = [1, 2, 3, 4, 5, 6]
    return data
