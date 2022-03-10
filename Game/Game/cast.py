class Cast:
    """Creates and manages a collection of Actors.

    Attr:
        _actors: A collection of Actors.
    """

    def __init__(self):
        """Constructs a new collection of Actors."""

        self._actors = {}
        
    def get_collection(self):
        """Gets all of the Actors within the collection.
        
        Returns:
            All of the Actors within the collection.
        """

        actors = []

        for collection in self._actors:
        
            actors.extend(self._actors[collection])
        
        return actors

    def get_actors(self, collection):
        """Gets the Actors within the collection.
        
        Args:
            collection: The name of the collection.

        Returns:
            The Actors within the collection.
        """

        actors = []

        if collection in self._actors.keys():
            
            actors = self._actors[collection].copy()
        
        return actors


    def get_first_actor(self, collection):
        """Gets the first Actor within the collection.
        
        Args:
            collection: The name of the collection.
            
        Returns:
            The first Actor in the collection.
        """

        actors = None

        if collection in self._actors.keys():
            
            actors = self._actors[collection][0]

        return actors

    def new_actor(self, collection, actor):
        """Adds an actor to the collection.
        
        Args:
            collection: The name of the collection.
            actor: The actor that needs to be added to the collection.
        """

        if not collection in self._actors.keys():
            
            self._actors[collection] = []
            
        if not actor in self._actors[collection]:

            self._actors[collection].append(actor)

    def delete_actor(self, collection, actor):
        """Deletes an Actor from the collection.
        
        Args:
            collection: The name of the collection.
            actor: The Actor that needs to be deleted.
        """

        if collection in self._actors:

            self._actors[collection].remove(actor)
