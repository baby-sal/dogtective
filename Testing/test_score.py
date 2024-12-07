#unit test
from unittest import TestCase
from logic.components.score import Score, NegativeTime, ZeroOrNegativeLives


class TestScore(TestCase):

#standard expectation of score calculation
    def test_score(self):
        expected = 1290
        result = Score.calculate_score(1, 1)
        self.assertEqual(expected, result)

    def test_full_health(self):
        expected = 5290
        result = Score.calculate_score(5, 1)
        self.assertEqual(expected, result)

#should the user take 5 minutes to perform achieve the end of the level
    def test_extreme_long_time(self):
        expected = 1000
        result = Score.calculate_score(1, 300)
        self.assertEqual(expected, result)

#if an error occurred and the time became negative
    def test_negative_time(self):
        with self.assertRaises(NegativeTime):
            Score.calculate_score(1, -1)

    def test_health_1_or_fewer(self):
        with self.assertRaises(ZeroOrNegativeLives):
            Score.calculate_score(0, 60)

