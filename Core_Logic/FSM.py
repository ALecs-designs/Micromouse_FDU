from enum import Enum
class MouseState(Enum): 
    wait_signal_standby = 1 
    search_goal =         2   
    return_to_start =     3 
    speed_run_moving =    4  
    fault =               5  
    moving_forward =      6 
    turning =             7 
    speed_run_turning =   8 

# Waiting for hand signal to start. Changes to "search_goal" when the hand signal is given.
# Exploring the maze to find the center. Changes to "return_to_start" when one of the goal cells is reached i.e. when current cell = goal[].
# Returns to the start cell. Changes to "speed_run" when starting cell is reached i.e. when current cell = (0,0)
# Speedruns to the goal. Changes to "wait_signal_standby" when the goal is reached again.
# This state is only triggered when a fault happens.
# When the  mouse is moving forward
# When the mouse is turning