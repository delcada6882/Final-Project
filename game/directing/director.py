from time import sleep
from game.shared.color import Color
from game.shared.point import Point
import pygame


CELL_SIZE = 15

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._total_score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        alreadyPlay = False

        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
            alreadyPlay = self._start_music(alreadyPlay)
        self._video_service.close_window()

    def _start_music(self, alreadyPlay):
        if alreadyPlay == False:
            pygame.mixer.init()
            pygame.mixer.music.load("/Users/adamdelcastillo-call/Documents/CSE 121/PPR/PPR/game/services/evil.wav")
            pygame.mixer.music.play()


    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction(robot)
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        dot = cast.get_first_actor("dot")
        artifacts = cast.get_actors("artifacts")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        
        for artifact in artifacts:
            artifact.move_next(max_x * 20, max_y * 20)
            if robot.get_position().equals(artifact.get_position()):
                self._total_score += artifact.get_points("plus")
                cast.remove_actor("artifacts", artifact)
            elif dot.get_position().equals(artifact.get_position()):
                self._total_score += artifact.get_points("minus")
                cast.remove_actor("artifacts", artifact)

            # if artifact.get_position().equals(Point(450, 600)):
            #     artifact.move_next(0, 0)

        
                
        banner.set_text("Score: " + str(self._total_score))

        


        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()