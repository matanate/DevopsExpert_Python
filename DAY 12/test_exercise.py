import pytest


@pytest.mark.arit
@pytest.mark.usefixtures("setup")
class TestExample:
    def test_add(self, setup):
        assert 1 + 1 == 2, "Failed"
        assert -1 + 1 == -2, "Failed"
        assert 100 + 1000 == 11000, "Failed"
        print("Passed")

    def test_multiply(self, setup):
        assert 1 * 1 == 1, "Failed"
        assert 0 * 1 == 0, "Failed"
        assert -1 * 1 == -1, "Failed"
        print("Passed")
