from gpiozero import RotaryEncoder
import math

enc_l = RotaryEncoder(17, 27, max_steps=0)
enc_r = RotaryEncoder(22, 23, max_steps=0)
# depends on physical motor/wheel specs
wheel_diameter_mm = 32.0
ticks_per_revolution = 360.0

def check_stall(current_pwr):
            """Cross-verification: High power + Zero encoder delta = Stall."""
            if abs(current_pwr) > 40 and enc_l.steps == 0:
                return True
def calculate_mm_from_encoder(steps):
        circumference = math.pi * wheel_diameter_mm
        mm_per_tick = circumference / ticks_per_revolution
        return steps * mm_per_tick

        
