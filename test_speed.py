import pytest
from speed import calculate_speed

def test_speed():
    assert calculate_speed(100, 2) == 50
    assert calculate_speed(50, 1) == 50
