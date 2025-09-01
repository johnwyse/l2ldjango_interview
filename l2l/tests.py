from django.test import TestCase
from datetime import datetime
from l2l.templatetags.l2l_extras import l2l_dt


class L2LDateTimeFilterTests(TestCase):
    """
    Test cases for the l2l_dt custom template filter.
    
    The filter should handle:
    - datetime objects
    - ISO date strings
    - Invalid inputs gracefully
    """
    
    def setUp(self):
        self.test_datetime = datetime(2025, 9, 1, 14, 30, 0)  # Sept 1, 2025 at 2:30 PM
        self.test_iso_string = "2025-09-01T14:30:00"
        self.test_invalid_date = "Sptmbr 1nd, 20252"
        self.test_invalid_string = "hello world"
        self.test_none = None
        self.test_empty_string = ""
        
        self.expected_format = "2025-09-01 14:30:00"

        # Note: No need to test invalid datetime object such as datetime(2025, 13, 1, 14, 30, 0)
        # Causes the test itself to error out while constructing the test case.

    def test_filter_with_datetime_object(self):
        # Test that the filter correctly handles datetime objects
        result = l2l_dt(self.test_datetime)
        self.assertEqual(result, self.expected_format)

    def test_filter_with_iso_string(self):
        # Test that the filter correctly handles ISO date strings
        result = l2l_dt(self.test_iso_string)
        self.assertEqual(result, self.expected_format)
    
    def test_filter_with_invalid_input(self):
        # Test with invalid inputs like None, empty string, invalid date format, invalid datetime object
        for invalid_input in [self.test_none, self.test_empty_string, self.test_invalid_date, self.test_invalid_string]:
            result = l2l_dt(invalid_input)
            self.assertEqual(result, invalid_input)

    def test_filter_consistency(self):
        # Test that datetime object and equivalent ISO string produce same result
        result_dt = l2l_dt(self.test_datetime)
        result_str = l2l_dt(self.test_iso_string)
        self.assertEqual(result_dt, result_str)
