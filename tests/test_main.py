# tests/test_main.py
import sys
import os
# Thêm thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from simple_sum import add_two_numbers

def test_add_two_numbers():
    assert add_two_numbers(3, 4) == 7
    assert add_two_numbers(-1, 1) == 0
    assert add_two_numbers(-2, -3) == -5
