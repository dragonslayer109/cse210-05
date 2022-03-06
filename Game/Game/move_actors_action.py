from Game import Action


class MoveActorsAction(Action):
    """
    This class moves all of the Actors on the screen according to their velocity.
    """

    def execute(self, cast, script):
        """Executes the new actions of the Actors.

        Args:
            cast: A collection of Actors.
            script: A script of Actions.
        """

        actors = cast.get_collection()

        for actor in actors:

            actor.next_move()