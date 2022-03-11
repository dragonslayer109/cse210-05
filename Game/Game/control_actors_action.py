import constants
from action import Action
from point import Point

class ControlActorsAction(Action):
    """
    Input actions that control the players movements and actions
    """
    def __init__(self, keyboard_service):
        """
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """
        Gets the input from the actors(players) controls and updates direction
        """
        """
        Movement for player 1 keyboard controls
        """
        # left player 1
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right player 1
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up player 1
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down player 1
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        """
        Movement for player 2 keyboard controls
        """
        # left player 2
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right player 2
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up player 2
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down player 2
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        player_1 = cast.get_first_actor("player 1")
        player_1.turn_head(self._direction)

        player_2 = cast.get_first_actor("player 2")
        player_2.turn_head(self._direction)