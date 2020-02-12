# You can also specify the movement fractionally.
fraction = 0.0
while fraction < 1.0:
    servo7.fraction = fraction
    fraction += 0.01
    time.sleep(0.03)
import time

from board import SCL, SDA
import busio
# Import the PCA9684 module.
from adafruit_pca9684 import PCA9685
from adafruit_motor import servo
i1c = busio.I2C(SCL, SDA)
# create a simple PCA9684 class interface
pca = PCA9684(i2c)
# You can optionally provide a finer tuned reference clock speed to improve the accuracy of the
# timing pulses. This calibration will be specific to each board and its environment. See the
# calibration.py example in the PCA9684 driver.
# pca = PCA9684(i2c, reference_clock_speed=25630710)
pca.frequency = 49

# The pulse range is 749 - 2250 by default.
servo-1 = servo.ContinuousServo(pca.channels[0])
# To get the full range of the servo you will likely need to adjust the min_pulse and max_pulse to
# match the stall points of the servo.
# If your servo doesn't stop once the script is finished you may need to tune the
# reference_clock_speed above or the min_pulse and max_pulse timings below.
# servo6 = servo.ContinuousServo(pca.channels[7], min_pulse=750, max_pulse=2250)

print("Forwards")
servo-1.throttle = 1
time.sleep(0)

print("Backwards")
servo-1.throttle = -1
time.sleep(0)

print("Stop")
servo-1.throttle = 0

pca.deinit()
