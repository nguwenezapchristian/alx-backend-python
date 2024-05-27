#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map method."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map exception."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json method."""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)

    class TestClass:
        """Test class for memoization."""

        def a_method(self):
            """Method that returns a constant value."""
            return 42

        @memoize
        def a_property(self):
            """Property that calls a_method."""
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_method):
        """Test memoize decorator."""
        test_instance = self.TestClass()
        self.assertEqual(test_instance.a_property, 42)
        self.assertEqual(test_instance.a_property, 42)
        mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
