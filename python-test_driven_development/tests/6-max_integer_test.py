#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        """Test with a list of ordered integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when max is at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_end(self):
        """Test when max is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_one_negative_number(self):
        """Test with one negative number."""
        self.assertEqual(max_integer([-5, 0, 5]), 5)

    def test_only_negative_numbers(self):
        """Test with only negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        """Test with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_identical_elements(self):
        """Test with all identical elements."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_duplicates(self):
        """Test with duplicate values."""
        self.assertEqual(max_integer([1, 2, 2, 1]), 2)

    def test_floats(self):
        """Test with float numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_int_float(self):
        """Test with mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_large_list(self):
        """Test with a large list."""
        self.assertEqual(max_integer(list(range(1000))), 999)

    def test_default_empty(self):
        """Test default parameter (empty list)."""
        self.assertIsNone(max_integer())

    def test_negative_and_positive(self):
        """Test with mixed negative and positive numbers."""
        self.assertEqual(max_integer([-10, 10, -5, 5, 0]), 10)

    def test_all_zeros(self):
        """Test with all zeros."""
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_single_negative(self):
        """Test with a single negative number."""
        self.assertEqual(max_integer([-5]), -5)


if __name__ == '__main__':
    unittest.main()
