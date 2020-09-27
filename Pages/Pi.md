[![image](https://user-images.githubusercontent.com/34621440/94373930-5ab4e680-00ce-11eb-9140-2131acbb4592.png)](https://utkarshcrazy.github.io/hyperloop/)
# Raspberry Pi

![image](https://user-images.githubusercontent.com/34621440/84532422-374b6480-acb4-11ea-806a-11eff38a77ac.png)

Pi and Motor using I2C:

  - Pi 3V3 to breakout VCC
  - Pi GND to breakout GND
  - Pi SCL to breakout SCL
  - Pi SDA to breakout SDA
  - Servo(BLDC+ESC) orange wire to breakout PWM on channel 0
  - Servo(BLDC+ESC) red wire to breakout V+ on channel 0
  - Servo(BLDC+ESC) brown wire to breakout Gnd on channel 0
For more information visit [i2c communication with pi] (https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/hooking-it-up/)

# New Features with pi!

  - Worked on accelerometer imu sensoor for distance position everything:::: razor 9dof imu
We can work on:
  - Detection of temperature, movement
    with Photoelectric sensor, LIDAR, Camera(Opencv+Deeplearning) : to detect object and temperature sensors

Pre-installed with ROS, with Wifi access point -> perfect for building your Raspberry Pi robots  (https://downloads.ubiquityrobotics.com/pi.html)

### GPIO pins in PI
![image](https://user-images.githubusercontent.com/34621440/84535805-8399a300-acba-11ea-84de-00beaeb6f17b.png)


List of websites helpful for wireless communication:

* [how-to-connect-a-raspberry-pi-to-a-laptop-display](<https://maker.pro/raspberry-pi/tutorial/how-to-connect-a-raspberry-pi-to-a-laptop-display>)

* https://devtalk.nvidia.com/default/topic/1061889/jetson-tx2/connection-via-ssh-to-jetson-tx2/post/5377508/#5377508

* protocol fixing with (https://devtalk.nvidia.com/default/topic/1001017/jetson-tx2/remote-desktoping-into-jetson-tx2-from-windows-10/post/5123184/#5123184)

* [nomachine install on jetson nano](<https://devtalk.nvidia.com/default/topic/1052773/jetson-nano/has-anyone-had-success-installing-nomachine-on-their-nano-/post/5409947/#5409947>)

* https://remote.it/

* https://websiteforstudents.com/access-ubuntu-18-04-lts-beta-desktop-via-vnc-from-windows-machines/

* https://devtalk.nvidia.com/default/topic/1036488/jetson-tx1/remote-control-of-the-jetson-tx1-without-using-an-hdmi-input/post/5265423/#5265423
