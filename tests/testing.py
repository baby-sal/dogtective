from unittest import TestCase, main



"""from tests.test1 import raise_custom_error_if_hit, water_volume_warning

#NEED TO UPDATE
class TestWaterVolume(TestCase):
    # individual tests cases go here
    def test_case_one(self):
        result = raise_custom_error_if_hit(radius=3, water_height=4)  # when entering in an input
        expected_result = 113.09733552923255  # this is what the output should be
        self.assertEqual(result, expected_result)  # what is the current result like compared to what it should be?

    def test_case_two(self):
        result = water_volume_warning(radius=3.4, water_height="")
        self.assertTrue(any("water_height has to be a number."))

    def test_case_three(self):
        result = water_volume_warning(radius="", water_height=6.34)
        self.assertTrue(any("Radius has to be a number."))
        #shows message as expected but doesn't show fatal error due to any within assertTrue built in function

    def test_case_four(self):
        result = raise_custom_error_if_hit(radius=-1, water_height=4)  # when entering in an input
        expected_result = "radius or water_height must be more than 0"  # this is what the output should be
        self.assertEqual(result, expected_result)  # what is the current result like compared to what it should be?


if __name__ == '__main__':
    main()"""