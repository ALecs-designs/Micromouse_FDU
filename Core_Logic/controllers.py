class PIDController:
    def __init__(self, kp, ki, kd, setpoint=0, limit=50):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0
        self.limit = limit

    def update(self, measurement, dt):
        if dt <= 0: return 0
        error = self.setpoint - measurement
        self.integral += error * dt
        # Simple anti-windup
        self.integral = max(-20, min(20, self.integral))
        d_term = (error - self.prev_error) / dt
        self.prev_error = error
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * d_term)
        return max(-self.limit, min(self.limit, output))
