from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    def __init__(self):
        super().__init__()
        self._points = 0

    def get_points(self, operator):
        if (operator == "plus"):
            self._points = 1
        else:
            self._points = -1

        return self._points