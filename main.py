# Copyright (c) 2026 Thom Lanjouw
import numpy as np


def add_two_integer_lists(a: list[int], b: list[int]) -> None:
    """Add two lists of integers element-wise and print the result."""
    arr = np.array(a) + np.array(b)
    print(f"My added array: {arr}")


if __name__ == "__main__":
    add_two_integer_lists([1, 2, 3], [4, 5, 6])
