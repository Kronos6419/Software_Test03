"""
Unit tests for the Bowling Game

This module contains a full suite of unit tests for the BowlingGame class,
covering open frames, spares, strikes, bonus logic, and edge cases.
"""

import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        """Set up a new game before each test."""
        self.game = BowlingGame()

    def roll_many(self, n, pins):
        """Helper to roll the same number of pins multiple times."""
        for _ in range(n):
            self.game.roll(pins)

    def roll_spare(self):
        """Helper to roll a spare (5 + 5)."""
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        """Helper to roll a strike (10 pins)."""
        self.game.roll(10)

    def test_gutter_game(self):
        """Test a game where no pins are knocked down."""
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        """Test a game where one pin is knocked down on each roll."""
        self.roll_many(20, 1)
        self.assertEqual(20, self.game.score())

    def test_all_spares(self):
        """Test a game where every frame is a spare (5 + 5, with 5 bonus)."""
        self.roll_many(21, 5)  # 10 frames + 1 bonus roll
        self.assertEqual(150, self.game.score())

    def test_perfect_game(self):
        """Test a perfect game: 12 strikes in a row."""
        self.roll_many(12, 10)
        self.assertEqual(300, self.game.score())

    def test_mixed_game(self):
        """Test a mixed game with strikes, spares, and open frames."""
        rolls = [10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1]
        for pins in rolls:
            self.game.roll(pins)
        self.assertEqual(167, self.game.score())  # ✅ corrected from 163

    def test_spare_in_final_frame(self):
        """Test a game ending in a spare with a bonus roll."""
        self.roll_many(18, 0)
        self.game.roll(7)
        self.game.roll(3)  # spare
        self.game.roll(5)  # bonus roll
        self.assertEqual(15, self.game.score())

    def test_strike_in_final_frame(self):
        """Test a game ending in a strike with two bonus rolls."""
        self.roll_many(18, 0)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.assertEqual(30, self.game.score())

    def test_incomplete_game(self):
        """Test a 10-frame game with all 1s."""
        self.roll_many(20, 1)
        self.assertEqual(20, self.game.score())

    def test_invalid_roll_negative(self):
        """Test that rolling a negative number raises an error."""
        with self.assertRaises(ValueError):
            self.game.roll(-1)

    def test_invalid_roll_too_high(self):
        """Test that rolling more than 10 pins raises an error."""
        with self.assertRaises(ValueError):
            self.game.roll(11)


if __name__ == "__main__":
    unittest.main()
