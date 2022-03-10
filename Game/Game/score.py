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
        self.add_score(0)

    def add_points(self, points):
        """The sum of the player's points gained.
        
        Args:
            score: The number of points that the player has gained.
        """

        self._score += points
        self.set_text(f"Score: {self._score}")