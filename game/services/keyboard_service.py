import pyray
from game.shared.color import Color
from game.shared.point import Point

class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size

    def get_direction(self, actor):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """

        if pyray.is_key_down(pyray.KEY_UP):
            actor.set_position(Point(450,200))
            actor.set_color(Color(255, 165, 214))

        if pyray.is_key_down(pyray.KEY_RIGHT):
            actor.set_position(Point(550,300))
            actor.set_color(Color(102, 153, 204))

        if pyray.is_key_down(pyray.KEY_LEFT):
            actor.set_position(Point(350,300))
            actor.set_color(Color(102, 153, 204))

        if pyray.is_key_down(pyray.KEY_W):
            actor.set_position(Point(450,200))
            actor.set_color(Color(255, 165, 214))

        if pyray.is_key_down(pyray.KEY_D):
            actor.set_position(Point(550,300))
            actor.set_color(Color(102, 153, 204))

        if pyray.is_key_down(pyray.KEY_A):
            actor.set_position(Point(350,300))
            actor.set_color(Color(102, 153, 204))
            
        dx = 0
        dy = 0
        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction