import unittest
from src.utils.core import get_total_elapsed_time_in_seconds, get_elapsed_time, format_elapsed_time

class TestElapsedTime(unittest.TestCase):

    def test_get_total_elapsed_time_in_seconds(self):
        start_time = 1622548800.0
        end_time = 1622548800.0 + 3610  # 1 hour and 10 seconds
        self.assertEqual(get_total_elapsed_time_in_seconds(start_time, end_time), 3610)

if __name__ == '__main__':
    unittest.main()