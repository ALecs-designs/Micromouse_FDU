from enum import Enum
class MouseState(Enum): 
    wait_signal_standby = 1 # Waiting for hand signal to start. Changes to "search_goal" when the hand signal is given.
    search_goal =         2 # Exploring the maze to find the center. Changes to "return_to_start" when one of the goal cells is reached i.e. when current cell = goal[].  
    return_to_start =     3 # Returns to the start cell. Changes to "speed_run" when starting cell is reached i.e. when current cell = (0,0)
    speed_run_moving =    4 # Speedruns to the goal. Changes to "wait_signal_standby" when the goal is reached again. 
    fault =               5 # This state is only triggered when a fault happens. 
    moving_forward =      6 # When the  mouse is moving forward
    turning =             7 # When the mouse is turning
    speed_run_turning =   8 
"""There are different states the mouse can be in. Each state will cause its own piece of code to be executed
The states are: 
- wait_signal_standby // wait signal pseudo reset mode
- search goal
- return to start (which the same as searching for the goal except the goal coordinates are changed to the origin.)
- speed run 
- fault = stall, crash, kills motors
"""