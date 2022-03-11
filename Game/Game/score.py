from Game import Actor

class Score(Actor):
    """
    This class keeps track of the player's score which will be used to decide who wins or loses the game.

    Attr:
        _score: The points the user has gained.
    """

    def __init__(self):

        super().__init__()

        self._score = 0

    def is_winner(self, points):
        """The sum of the player's points gained.
        
        Args:
            score: The number of points that the player has gained.
        """

        self._score += points

        if self._score == 0:
            self.set_text("You lose! Try again next time.")
        elif self._score != 0:
            self.set_text("Congratulations! You win!")