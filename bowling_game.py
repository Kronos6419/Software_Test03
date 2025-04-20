"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    """
    A class to simulate a ten-pin bowling game and calculate the total score.
    """
    
    def __init__(self):
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """
        Records a roll in the game.

        Args:
            pins (int): Number of pins knocked down in this roll (0 to 10).

        Raises:
            ValueError: If pins is less than 0 or greater than 10.
        """
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10.")
        self.rolls.append(pins)

    def score(self):
        """
        Calculates the total score for the game based on recorded rolls.

        Returns:
            int: Total score for the game.
        """
        score = 0
        roll_index = 0

        for frame in range(10):
            if self._is_strike(roll_index):
                score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
        return score

    def _calculate_frame_score(self, roll_index):
        if self._is_strike(roll_index):
            return 10 + self._strike_bonus(roll_index)
        elif self._is_spare(roll_index):
            return 10 + self._spare_bonus(roll_index)
        else:
            return self.rolls[roll_index] + self.rolls[roll_index + 1]

    def _is_strike(self, frame_index):
        """
        Check if the roll at frame_index is a strike.

        Args:
            frame_index: Index of the roll to check

        Returns:
            True if the roll is a strike, False otherwise
        """
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """
        Check if the rolls at frame_index and frame_index + 1 form a spare.

        Args:
            frame_index: Index of the first roll in a frame

        Returns:
            True if the rolls form a spare, False otherwise
        """
        return frame_index + 1 < len(self.rolls) and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _bonus(self, roll_index, count):
        return sum(
            self.rolls[i] if i < len(self.rolls) else 0
            for i in range(roll_index + 1, roll_index + 1 + count)
        )

    def _strike_bonus(self, roll_index):
        return self._bonus(roll_index, 2)
    
        """
        Calculate the bonus for a strike.

        Args:
            frame_index: Index of the strike roll

        Returns:
            The value of the next two rolls after the strike
        """

    def _spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2] if roll_index + 2 < len(self.rolls) else 0

        """
        Calculate the bonus for a spare.

        Args:
            frame_index: Index of the first roll in a spare

        Returns:
            The value of the roll after the spare
        """