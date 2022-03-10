import constants

from Game import Color
from Game import Point


class Actor:
    """The visual appearance of the player in the game.

    Attr:
        _text: The visual appearance of the Actor.
        _font_size: The size of the Actor.
        _color: The color of the Actor.
        _position: The current coordinates of the Actor on the screen.
        _velocity: The speed and direction of the Actor..
    """

    def __init__(self):
        """Constructs a new Actor."""

        self._text = ""
        self._font_size = 10
        self._color = Color(2, 205, 250)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_text(self):
        """Gets the visual representation of the Actor.
        
        Returns:
            The visual representation of the Actor.
        """

        return self._text

    def get_font_size(self):
        """Gets the size of the Actor represented as a font size.
        
        Returns:
            The size of the Actor.
        """

        return self._font_size

    def get_color(self):
        """Gets the Actor's color in rgb format.
        
        Returns:
            The color of the Actor.
        """

        return self._color

    def get_position(self):
        """Gets the current position of the Actor.
        
        Returns:
            The current coordinates on the screen of the Actor's position.
        """

        return self._position

    def get_velocity(self):
        """Gets the direction and speed (velocity) of the Actor.
        
        Returns:
            The velocity of the Actor.
        """

        return self._velocity

    def set_text(self, text):
        """Updates the visual representation of the Actor.
        
        Args:
            text: The chosen visual representation of the Actor.
        """

        self._text = text

    def set_font_size(self, font_size):
        """Updates the size of the Actor.
        
        Args:
            font_size: The chosen size of the Actor.
        """

        self._font_size = font_size

    def set_color(self, color):
        """Updates the Actor's color.
        
        Args:
            color: The chosen color of the Actor.
        """

        self._color = color

    def set_position(self, position):
        """Updates the Actor's position.
        
        Args:
            position: The new position of the Actor.
        """

        self._position = position

    def set_velocity(self, velocity):
        """Updates the Actor's velocity.
        
        Args:
            velocity: The new speed and direction of the Actor.
        """

        self._velocity = velocity

    def next_move(self):
        """Calculates the next position of the Actor according to its velocity.
        
        Args:
            max_x: The maximum x (horizontal) value.
            max_y: The maximum y (vertical) value.
        """

        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y

        self._position = Point(x, y)