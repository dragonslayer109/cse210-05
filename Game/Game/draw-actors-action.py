from action import Action

class DrawActorsAction(Action):
    """
    Output group action that draws all actors(objects)
    """
    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script):
        """
        Execute the draw actions. Note points must be defined in the
        objects classes to display in the correct area.
        """
        score_player_1 = cast.get_first_actor("scores")
        score_player_2 = cast.get_first_actor("scores")
        player_1 = cast.get_first_actor("player 1")
        player_2 = cast.get_first_actor("player 2")
        tail_1 = player_1.get_tail()
        tail_2 = player_2.get_tail()
        messages = cast.get_actors("messages")

        self._video_service.first_buffer()
        self._video_service.display_actors(tail_1)
        self._video_service.display_actors(tail_2)
        self._video_service.display_actor(score_player_1)
        self._video_service.display_actor(score_player_2)
        self._video_service.display_actors(messages, True)
        self._video_service.second_buffer()