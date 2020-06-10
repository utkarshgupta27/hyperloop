# Electronic Speed Controllers (ESC)
(Jeti Spin 200 Opto)

[![JETISPIN-200O-2T](https://user-images.githubusercontent.com/34621440/84303077-5dda9580-ab24-11ea-8219-874201845eca.jpg)](https://shop.jetiusa.com/Jeti-Spin-Pro-200-Opto-Brushless-ESC-p/jetispin-200o.htm)

(Turnigy Fatboy V2 300A ESC 4~15S (OPTO))

[![25608](https://user-images.githubusercontent.com/34621440/84303404-e822f980-ab24-11ea-976f-0cee645da2b6.jpg)](https://hobbyking.com/en_us/turnigy-fatboy-v2-300a-esc-4-15s-opto.html)

ESC  (ESC+BLDC/BDC act like a servo)
- is a brushless motor controller which creates tri-phase AC power from the onboard DC battery.
-  A remote radio transmitter controlled by a user is the source for the receiver signals. PWM stands for Pulse-Width Modulation, a modulation technique used to encode a message into a pulsing signal. So, analog signal by digital means
-  to control ESC, a PWM signal is sent to the device as repeating pulses of variable width.
-  contains a micro controller which interprets the supplied PWM signal and appropriately controls the car motor using built-in firmware.
- The pulses are defined by the frame size, which is the frequency of the pulse and the PWM duty cycle which is the ON vs. OFF time of the signal.
- For a servo or ESC, the device expects to see a frame every 20 milliseconds, but this can vary from device to device 50Hz (50 cycles per second) which is a 20ms frame,
-The device expects a pulse between 1.0 and 2.0 ms. For a servo the pulse width represents the position of the servo motor, 1.0ms represents -90 degrees, 1.5ms represents 0 degrees (center), and 2.0 ms represents +90 degrees. For an ESC the pulse width represents throttle position, 1.0 ms represents full reverse (or the lowest throttle setting, depending on the interpretation of the ESC), 1.5ms is neutral, and 2.0 represents full throttle.
- has three performance modes, regular, race, and training.

# New Features!

  - 


> An electronic speed control or ESC is an electronic circuit that controls and regulates the speed of an electric motor(BLDC here). It may also provide reversing of the motor and dynamic braking.

### Tech

 The PCA9685 is a 12 bit device, which means basically that you can think of each frame as being split into 2^12 slots (4096). To calculate throttle pulses:
1.0ms/20ms*4096 = 204 full reverse
1.5ms/20ms*4096 = 307 neutral
2.0ms/20ms*4096 = 409 full forward
