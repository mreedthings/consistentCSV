import unittest
from concsv import check_fields

class TestCheckFields(unittest.TestCase):

    def test_check_fields_failure(self):
        result = check_fields('test_inconsistent.csv')
        self.assertFalse(result)

    def test_check_fields_success(self):
        result = check_fields('test_consistent.csv')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
