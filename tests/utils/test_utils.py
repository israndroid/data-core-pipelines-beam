import unittest
from src.utils.core import get_total_elapsed_time_in_seconds, get_elapsed_time, format_elapsed_time

class TestElapsedTime(unittest.TestCase):

    def test_get_total_elapsed_time_in_seconds(self):
        start_time = 1622548800.0
        end_time = 1622548800.0 + 3610  # 1 hour and 10 seconds
        self.assertEqual(get_total_elapsed_time_in_seconds(start_time, end_time), 3610)
    def test_format_elapsed_time(self):
        self.assertEqual(format_elapsed_time(3661), "1h 1m 1s")
        self.assertEqual(format_elapsed_time(61), "0h 1m 1s")
        self.assertEqual(format_elapsed_time(0), "0h 0m 0s")
        with self.assertRaises(ValueError):
            format_elapsed_time(-1)

if __name__ == '__main__':
    unittest.main()