import os
import random
import time

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 14
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Python Python Revolution"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


set_list = [
    [1, "down", 1], [3, "down", 1], [5, "down", 1], 
    [7, "left", 1], [9, "left", 1], [11, "left", 1], 
    [13, "down", 1], [15, "down", 1], [17, "down", 1],
    [19, "right", 1], [21, "right", 1], [23, "right", 1], 

    [25, "down", 1], [27, "down", 1], [29, "down", 1], 
    [31, "left", 1], [33, "left", 1], [35, "left", 1],
    [37, "down", 1], [39, "down", 1], [41, "down", 1], 
    [43, "right", 1], [45, "right", 1], [47, "right", 1], 

    [49, "down", 1], [51, "left", 1], [52, "down", 1], [53, "left", 1], 
    [55, "right", 1], [57, "down", 1], [59, "left", 1], 
    [61, "down", 1], [63, "left", 1], [64, "down", 1], [65, "left", 1], [66, "down", 1], 
    [67, "down", 1],  [69, "right", 1],  [70, "down", 1],  [71, "right", 1],  [72, "down", 1],  
    
    [73, "down", 1],  [75, "right", 1],  [76, "down", 1],  [77, "left", 1],  
    [79, "down", 1],  [81, "right", 1],  [83, "down", 1],  
    [85, "right", 1],  [87, "down", 1],  [88, "left", 1],  [89, "down", 1],  [90, "right", 1],
    [91, "right", 1],  [93, "down", 1],  [95, "left", 1],

    [97, "down", 1],  [98, "down", 1],  [99, "down", 1],  [100, "down", 1],  [101, "down", 1],  [102, "down", 1],  
    [103, "right", 1],  [104, "right", 1],  [105, "right", 1], [106, "right", 1],  [107, "right", 1],  [108, "right", 1],
    [109, "down", 1],  [110, "down", 1],  [111, "down", 1],  [112, "down", 1],  [113, "down", 1],  [114, "down", 1],  
    [115, "left", 1],  [116, "left", 1],  [117, "left", 1], [118, "left", 1],  [119, "left", 1],  [120, "left", 1],

    [121, "down", 1],  [122, "down", 1],  [123, "left", 1],  [124, "left", 1],  [125, "down", 1],  [126, "down", 1],  
    [127, "right", 1],  [128, "right", 1],  [129, "down", 1], [130, "down", 1],  [131, "left", 1],  [132, "left", 1],
    [133, "down", 1],  [134, "down", 1],  [135, "right", 1],  [136, "right", 1],  [137, "down", 1],  [138, "down", 1],  
    [139, "left", 1],  [140, "left", 1],  [141, "down", 1], [142, "down", 1],  [143, "right", 1],  [144, "right", 1],


    [145, "down", 1], 
    [151, "down", 1], [154, "right", 1], 
    [157, "right", 1], 
    [163, "right", 1], [166, "down", 1], 

    [169, "down", 1],   [171, "right", 1], [172, "down", 1], [173, "right", 1], 
    [175, "left", 1],   [177, "down", 1], [178, "right", 1], [179, "down", 1], 
    [181, "right", 1],   [183, "down", 1], [184, "down", 1], [185, "down", 1], 
    [187, "right", 1], [189, "down", 1], [191, "left", 1], 


    [193, "down", 1],  [194, "left", 1],  [195, "down", 1],  [196, "left", 1],  [197, "down", 1],  [198, "left", 1],  
    [199, "down", 1],  [200, "left", 1],  [201, "down", 1], [202, "left", 1],  [203, "down", 1],  [204, "left", 1],
    [205, "down", 1],  [206, "left", 1],  [207, "down", 1],  [208, "left", 1],  [209, "down", 1],  [210, "left", 1],  
    [211, "down", 1],  [212, "right", 1],  [213, "down", 1], [214, "right", 1],  [215, "down", 1],  [216, "right", 1],

    [217, "down", 1],  [218, "left", 1],  [219, "down", 1],  [220, "left", 1],  [221, "down", 1],  [222, "left", 1],  
    [223, "down", 1],  [224, "left", 1],  [225, "down", 1], [226, "left", 1],  [227, "down", 1],  [228, "right", 1],
    [229, "down", 1],  [230, "left", 1],  [231, "down", 1],  [232, "left", 1],  [233, "down", 1],  [234, "left", 1],  
    [235, "down", 1],  [236, "right", 1],  [237, "down", 1], [238, "right", 1],  [239, "down", 1],  [240, "right", 1],


    [241, "down", 1],  [243, "down", 1], [244, "down", 1], [245, "down", 1], 
    [247, "left", 1], [249, "down", 1], [251, "right", 1], 
    [253, "down", 1],  [255, "left", 1], [256, "down", 1], [257, "left", 1], [258, "down", 1], 
    [259, "down", 1],  [261, "right", 1], [262, "down", 1], [263, "right", 1], [264, "down", 1], 

    [265, "down", 1],  [267, "down", 1], [268, "down", 1], [269, "down", 1],
    [271, "left", 1], [273, "down", 1], [275, "right", 1],
    [277, "down", 1],  [279, "left", 1], [280, "down", 1], [281, "left", 1], [282, "down", 1],
    [283, "left", 1], [285, "down", 1], [287, "right", 1],

    [289, "down", 1],
    [295, "left", 1], [297, "left", 1], [299, "left", 1], 
    [301, "left", 1], 
    [307, "right", 1], [309, "right", 1], [311, "right", 1], 

    [313, "down", 1],
    [319, "left", 1], [321, "down", 1], [323, "left", 1], 
    [325, "down", 1], 
    [331, "right", 1],

    [337, "down", 1],

    [361, "down", 1]


]

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("Score: ")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(Color(255, 165, 214))
    robot.set_position((Point(450,200)))
    cast.add_actor("robots", robot)


    dot = Actor()
    dot.set_text("@")
    dot.set_font_size(FONT_SIZE)
    dot.set_color(WHITE)
    dot.set_position(position)
    cast.add_actor("dot", dot)

    reference = Actor()
    reference.set_text("_ _ _ _ _ _ _ _ _ _ _ _ _")
    reference.set_font_size(FONT_SIZE)
    reference.set_color(WHITE)
    reference.set_position(Point(367, 205))
    cast.add_actor("referenceTop", reference)
    
    reference = Actor()
    reference.set_text("|\n|\n|\n|\n|\n")
    reference.set_font_size(FONT_SIZE)
    reference.set_color(WHITE)
    reference.set_position(Point(545, 220))
    cast.add_actor("referenceRight", reference)
        
    reference = Actor()
    reference.set_text("|\n|\n|\n|\n|\n")
    reference.set_font_size(FONT_SIZE)
    reference.set_color(WHITE)
    reference.set_position(Point(363, 220))
    cast.add_actor("referenceLeft", reference)

    reference = Actor()
    reference.set_text("_ _ _ _ _ _ _ _ _ _ _ _ _")
    reference.set_font_size(FONT_SIZE)
    reference.set_color(WHITE)
    reference.set_position(Point(367, 320))
    cast.add_actor("referenceBottom", reference)
    
    # create the artifacts
    for n in range(set_list.__len__()):
        text = "0"

        location = set_list[n][0]
        direction = set_list[n][1]
        velocity_num = set_list[n][2]

        if direction == "down":
            color = Color(255, 105, 180)
            if velocity_num == 0:
                y = location
            else:
                y = 12 - ((location - 1) * 2)
            x = 30
            position = Point(x, y)
            position = position.scale(CELL_SIZE)
            velocity = Point(0,10)
        
        if direction == "up":
            color = Color(255, 105, 180)
            x = 30
            if velocity_num == 0:
                y = location
            else:
                y = 28 - ((location - 1) * -2)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)
            velocity = Point(0, -10)

        if direction == "left":
            color = Color(25, 116, 210)
            if velocity_num == 0:
                x = location
            else:
                x = 38 - ((location - 1) * -2)
            y = 20
            position = Point(x, y)
            position = position.scale(CELL_SIZE)
            velocity = Point(-10, 0)
        
        if direction == "right":
            color = Color(25, 116, 210)
            if velocity_num == 0:
                x = location
            else:
                x = 22 - ((location - 1) * 2)
            y = 20
            position = Point(x, y)
            position = position.scale(CELL_SIZE)
            velocity = Point(10, 0)
        

        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_actor("artifacts", artifact)
        artifact.set_velocity(velocity) 
        

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()
