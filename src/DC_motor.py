##"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from board import SCL,SDA
import busio
class DCMotor:
    """DC motor driver. ``positive_pwm`` and ``negative_pwm`` can be swapped if the motor runs in
       the opposite direction from what was expected for "forwards".
       :param ~pulseio.PWMOut positive_pwm: The motor input that causes the motor to spin forwards
         when high and the other is low.
       :param ~pulseio.PWMOut negative_pwm: The motor input that causes the motor to spin backwards
         when high and the other is low."""
    def __init__(self, positive_pwm, negative_pwm):
        self._positive = positive_pwm
        self._negative = negative_pwm
        self._throttle = None

    @property
    def throttle(self):
        """Motor speed, ranging from -1.0 (full speed reverse) to 1.0 (full speed forward),
        or ``None``.
        If ``None``, both PWMs are turned full off. If ``0.0``, both PWMs are turned full on.
        """
        return self._throttle

    @throttle.setter
    def throttle(self, value):
        if value is not None and (value > 1.0 or value < -1.0):
            raise ValueError("Throttle must be None or between -1.0 and 1.0")
        self._throttle = value
        if value is None:
            self._positive.duty_cycle = 0
            self._negative.duty_cycle = 0
        elif value == 0:
            self._positive.duty_cycle = 0xffff
            self._negative.duty_cycle = 0xffff
        else:
            duty_cycle = int(0xffff * abs(value))
            if value < 0:
                self._positive.duty_cycle = 0
                self._negative.duty_cycle = duty_cycle
            else:
                self._positive.duty_cycle = duty_cycle
                self._negative.duty_cycle = 0

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.throttle = None

    def deinit(self):
        """Stop using the motor."""
        self.throttle = None
        
from adafruit_pca9685 import PCA9685

from adafruit_motor import motor

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance for the Motor FeatherWing's default address.
pca = PCA9685(i2c, address=0x40)
pca.frequency = 60

# Motor 1 is channels 9 and 10 with 8 held high.
# Motor 2 is channels 11 and 12 with 13 held high.
# Motor 3 is channels 3 and 4 with 2 held high.
# Motor 4 is channels 5 and 6 with 7 held high.

# DC Motors generate electrical noise when running that can reset the microcontroller in extreme
# cases. A capacitor can be used to help prevent this. The demo uses motor 4 because it worked ok
# in testing without a capacitor.
# See here for more info: https://learn.adafruit.com/adafruit-motor-shield-v2-for-arduino/faq#faq-13
pca.channels[7].duty_cycle = 0xffff
motor4 = motor.DCMotor(pca.channels[0], pca.channels[1])

print("Forwards slow")
motor4.throttle = 0.5
print("throttle:", motor4.throttle)
time.sleep(1)

print("Forwards")
motor4.throttle = 1
print("throttle:", motor4.throttle)
time.sleep(1)

print("Backwards")
motor4.throttle = -1
print("throttle:", motor4.throttle)
time.sleep(1)

print("Backwards slow")
motor4.throttle = -0.5
print("throttle:", motor4.throttle)
time.sleep(1)

print("Stop")
motor4.throttle = 0
print("throttle:", motor4.throttle)
time.sleep(1)

print("Spin freely")
motor4.throttle = None
print("throttle:", motor4.throttle)

pca.deinit()
