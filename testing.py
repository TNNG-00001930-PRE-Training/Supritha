import unittest
import string_operations

class string_operationstest(unittest.TestCase):
    def test_concatenation(self):
        self.assertEqual(string_operations.concatenate("hey", "guys"), "hey guys")

    def test_slicing(self):
        self.assertEqual(string_operations.slice_string("hello world", 0, 5), "hello")

    def test_formatting(self):
        self.assertEqual(string_operations.format_string("Hello, {}!", "everyone"), "Hello, everyone!")

    def test_uppercase(self):
        self.assertEqual(string_operations.uppercase("supritha"), "SUPRITHA")

    def test_lowercase(self):
        self.assertEqual(string_operations.lowercase("SUPRITHA"), "supritha")

    def test_strip_whitespace(self):
        self.assertEqual(string_operations.strip_whitespace("  hello  "), "hello")

    def test_replace_string(self):
        self.assertEqual(string_operations.replace_string("hello world", "world", "everyone"), "hello everyone")

if __name__ == '__main__':
    unittest.main()