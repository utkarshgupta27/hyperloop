This folder contains all of the setup information for the Pi. Device tree overlays, pinout information, kernel modules, and some setup scripts
# PI OS Setup
  * Using this [Debian 9.4 image](http://debian.beagleboard.org/images/bone-debian-9.4-iot-armhf-2018-06-17-4gb.img.xz), follow the SD card installation steps at the bottom of this README.
    * This guide is specific to just this version of Debian, with the 4.14 kernel. There have been big, breaking changes from previous kernel versions. uEnv.txt is different. Device overlays are different.
  * To connect when plugged directly into your personal computer, I like having a static ethernet port. SSHing over USB is slower, and sometimes drops
    * Setup network by editing `/etc/network/interfaces` and adding:
  ```
  allow-hotplug eth0
  iface eth0 inet static
    address 192.168.137.100
    netmask 255.255.255.0
    gateway 192.168.137.0
    network 129.168.137.1
  ```
# Steps to get Pi configured:
1. Do the above to make sure the following will work
2. Run `copyAll` to move over all necessary files to Pi. Password is `temppwd`, which is the default for the user `debian`
3. `ssh` into the Pi using `debian@192.168.137.100` with password `temppwd`
4. Run `sudo ./setupOverlay`. Change the permissions of this file if necessary
5. Restart the Pi and check the `dmesg` for success/ errors of overlays
6. Run `sudo ./initPRU` to load the PRU firmware, and `sudo ./initCAN` to start the CAN interface, and `./initGPIO` to 'export' the gpio pins (any ordering works), and `sudo ./initADC` to setup the internal ADC read buffer (see the `adc_testing/` folder for more information). **This must be run every time the BBB is restarted**
