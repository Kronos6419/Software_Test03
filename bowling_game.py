"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""

class BowlingGame:
    """
    A class to represent a 10-pin bowling game and calculate scores according to official rules.
    """

    def __init__(self):
        """
        Initialize a new bowling game with an empty list of rolls.
        """
        self.rolls = []

    def roll(self, pins):
        """
        Record a roll in the game.

        Args:
            pins (int): Number of pins knocked down in the roll.

        Raises:
            ValueError: If pins is less than 0 or greater than 10.
        """
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10.")
        self.rolls.append(pins)

    def score(self):
        """
        Calculates the total score for the game using the frame scoring helper.

        The method loops through each of the 10 frames and calls the
        _calculate_frame_score() method to compute the score for that frame.
        Handles strikes and spares using helper bonus methods.

        Returns:
            int: The final score for the bowling game.
        """
        score = 0
        roll_index = 0

        for frame in range(10):
            score += self._calculate_frame_score(roll_index)
            roll_index += 1 if self._is_strike(roll_index) else 2

        return score

    def _calculate_frame_score(self, roll_index):
        """
        Calculate the score for a single frame.

        Args:
            roll_index (int): Index of the first roll in the frame.

        Returns:
            int: Score for the current frame including bonuses.
        """
        if self._is_strike(roll_index):
            return 10 + self._strike_bonus(roll_index)
        elif self._is_spare(roll_index):
            return 10 + self._spare_bonus(roll_index)
        else:
            return self.rolls[roll_index] + self.rolls[roll_index + 1]

    def _is_strike(self, frame_index):
        """
        Check if the roll at the given index is a strike.

        Args:
            frame_index (int): Index of the roll to check.

        Returns:
            bool: True if the roll is a strike, False otherwise.
        """
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, roll_index):
        """
        Check if the two rolls at the given index form a spare.

        Args:
            roll_index (int): Index of the first roll in the frame.

        Returns:
            bool: True if it's a spare, False otherwise.
        """
        return (roll_index + 1 < len(self.rolls) and
                self.rolls[roll_index] + self.rolls[roll_index + 1] == 10)

    def _strike_bonus(self, roll_index):
        """
        Calculate the bonus for a strike.

        Args:
            roll_index (int): Index of the strike roll.

        Returns:
            int: The value of the next two rolls after the strike.
        """
        return self._bonus(roll_index, 2)

    def _spare_bonus(self, roll_index):
        """
        Calculate the bonus for a spare.

        Args:
            roll_index (int): Index of the first roll in a spare.

        Returns:
            int: The value of the roll after the spare.
        """
        return self.rolls[roll_index + 2] if roll_index + 2 < len(self.rolls) else 0

    def _bonus(self, roll_index, count):
        """
        Generic helper method to calculate a bonus after a strike or spare.

        Args:
            roll_index (int): Index of the frame.
            count (int): Number of rolls to sum after the frame.

        Returns:
            int: Sum of the next 'count' rolls or 0 if not enough rolls.
        """
        return sum(self.rolls[roll_index + 1: roll_index + 1 + count])
