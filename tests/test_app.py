# tests/test_app.py

# Import functions from app.py
from app import add, subtract

# Test for add function
def test_add():
    assert add(2, 3) == 5

# Test for subtract function
def test_subtract():
    assert subtract(5, 2) == 3
