import pytest

from utils import arrs


@pytest.fixture
def array():
    return [1, 2, 3]


def test_get(array):
    assert arrs.get(array, 1, "test") == 2
    assert arrs.get(["test"], -1, "test") == "test"


def test_slice(array):
    assert arrs.my_slice(array, 1, 3) == [2, 3]
    assert arrs.my_slice(array, 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(array, -4) == [1, 2, 3]
    assert arrs.my_slice(array, -3) == [1, 2, 3]
