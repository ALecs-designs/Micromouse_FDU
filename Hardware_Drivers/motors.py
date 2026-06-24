# Motor Setup
from gpiozero import DigitalOutputDevice, PWMOutputDevice
import time

PWMA_PIN, PWMB_PIN = 12, 13
AIN1_PIN, AIN2_PIN = 15, 14
BIN1_PIN, BIN2_PIN = 16, 25
STBY_PIN = 18

pwmA = PWMOutputDevice(PWMA_PIN, frequency=1000, initial_value=0.0)
pwmB = PWMOutputDevice(PWMB_PIN, frequency=1000, initial_value=0.0)

AIN1 = DigitalOutputDevice(AIN1_PIN, initial_value=False)
AIN2 = DigitalOutputDevice(AIN2_PIN, initial_value=False)
BIN1 = DigitalOutputDevice(BIN1_PIN, initial_value=False)
BIN2 = DigitalOutputDevice(BIN2_PIN, initial_value=False)

STBY = DigitalOutputDevice(STBY_PIN, initial_value=False)


def motor_enable():
    STBY.on()

def motor_disable():
    STBY.off()

def set_motor_direction(l, r):
    """
    #l, r: "F" (forward) or "R" (reverse) or "S" (stop/coast)
    TB6612 truth table:
      Forward: IN1=1 IN2=0
      Reverse: IN1=0 IN2=1
      Coast:   IN1=0 IN2=0
      Brake:   IN1=1 IN2=1
    """
    # Left motor (A channel)
    if l == "F":
        AIN1.on();  AIN2.off()
    elif l == "R":
        AIN1.off(); AIN2.on()
    else:  # "S"
        AIN1.off(); AIN2.off()

    # Right motor (B channel)
    if r == "F":
        BIN1.on();  BIN2.off()
    elif r == "R":
        BIN1.off(); BIN2.on()
    else:  # "S"
        BIN1.off(); BIN2.off()

def set_motor_power(lp, rp):
    """
    lp, rp are duty cycle percentages 0–100.
    gpiozero PWMOutputDevice.value expects 0.0–1.0.
    """
    lp = max(0.0, min(100.0, float(lp))) / 100.0
    rp = max(0.0, min(100.0, float(rp))) / 100.0
    pwmA.value = lp
    pwmB.value = rp

def set_speeds(left_speed, right_speed):
    """
    Takes speeds from -100 to 100.
    Automatically handles reversing the direction pins for negative values.
    """
    # 1. Determine direction based on the sign (+ or -)
    l_dir = "F" if left_speed >= 0 else "R"
    r_dir = "F" if right_speed >= 0 else "R"
    
    # 2. Set the physical direction pins
    set_motor_direction(l_dir, r_dir)
    
    # 3. Strip the negative sign and clamp to a maximum of 100%
    lp_abs = min(100.0, abs(float(left_speed))) / 100.0
    rp_abs = min(100.0, abs(float(right_speed))) / 100.0
    
    # 4. Apply power to the PWM pins
    pwmA.value = lp_abs
    pwmB.value = rp_abs

def stop_motors():
    set_motor_power(0, 0)
    set_motor_direction("S", "S")

def turn_left(t, p=25):
    # left motor reverse, right motor forward (spin left)
    set_motor_direction("R", "F")
    set_motor_power(p, p)
    time.sleep(t)
    stop_motors()

def turn_right(t, p=25):
    # left motor forward, right motor reverse (spin right)
    set_motor_direction("F", "R")
    set_motor_power(p, p)
    time.sleep(t)
    stop_motors()

def forward(t, p): #p = 25
    set_motor_direction("F", "F")
    set_motor_power(p, p)
    time.sleep(t)
    stop_motors()

def brake():
    # brake mode: IN1=IN2=1 for both channels
    AIN1.on(); AIN2.on()
    BIN1.on(); BIN2.on()
    set_motor_power(0, 0)
