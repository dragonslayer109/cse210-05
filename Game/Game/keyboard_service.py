import pyray
from Game import Point


class KeyboardService:
    """Detects the user's input from the keyboard.

    Attr:
        _keys: The key that the user presses on the keyboard.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""

        self._keys = {}
        
        # Player One
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D

        # Player Two
        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L

    def key_up(self, key):
        """Checks to see if the key is up.
        
        Args:
            key: The key being pressed.
        """

        py_key = self._keys[key.lower()]

        return pyray.key_up(py_key)

    def key_down(self, key):
        """Checks to see if the key is down.
        
        Args:
            key: The key being pressed.
        """

        py_key = self._keys[key.lower()]

        return pyray.key_down(py_key)