import logging
import serial
import os
import RPi.GPIO as GPIO
import time

class IMULogger(object):
    """Logs Vectornav VN-200 IMU serial data"""

    def __init__(self):
        self.initialize_logger_settings()
        self.start()

    def initialize_logger_settings(self):
        """Set logger configuration settings"""
        
        self.initialize_log_directory()
        logging.basicConfig(filename= self.path + self.filename, 
                            filemode='w', 
                            level=logging.INFO, 
                            format='%(asctime)s.%(msecs)03d,%(message)s',
                            datefmt='%d-%b-%y,%H:%M:%S')
        logging.info('Successfully loaded logger configuration settings')
    
    def initialize_log_directory(self):
        """Create IMU directory and IMU file"""

        self.path = '/home/pi/IMU_pi_logger/logs/'

        if not os.path.exists(self.path):
            os.makedirs(self.path)
            self.filename = 'IMU0000.log'
        else:
            self.filename = self.get_next_log_file_name()

    def initialize_LED(self):
        """Set GPIO settings"""

        self.LED_PIN = 40
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.LED_PIN, GPIO.OUT, initial=GPIO.LOW)
        
    def initialize_IMU_serial_port(self):
        """Attempt to connect to IMU serial port
        Scans dev directory for USB ports and attempts to connect to serial port
        """
        
        self.dev_ports = ['/dev/' + f for f in os.listdir('/dev') if 'ttyAMA' in f]
        if not self.dev_ports:
            return False

        for port in self.dev_ports:
            try:
                logging.info('Attempting to connect to {}'.format(port))
                self.ser = serial.Serial(port)
                self.ser.timeout = 5
                self.ser.baudrate = 230400
                logging.info('Successfully connected to {}'.format(port))
                return True
            except serial.serialutil.SerialException:
                logging.info('Failed to connect to {}'.format(port))
                pass

    def get_next_log_file_name(self):
        """Scans log directory for latest log file and returns a new filename"""

        def extract_digits(filename):
            s = ''
            for char in filename:
                if char.isdigit():
                    s += char
            return int(s)
        
        l = [extract_digits(filename) for filename in os.listdir(self.path)]
        # Directory is empty
        if not l:
            return 'IMU0000.log'
        # Directory has files so find latest
        else:
            latest_file_number = max(l)
            return 'IMU' + '{0:04d}'.format(latest_file_number + 1) + '.log'
    
    def blink_LED(self):
        GPIO.output(self.LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.LED_PIN, GPIO.LOW)
        time.sleep(1)

    def log_data(self):
        """Reads IMU data from serial port
        If no data on port, turns LED off
        If able to read data, turns LED on and writes to log file
        """

        data = self.ser.readline().rstrip()
        if not data:
            GPIO.output(self.LED_PIN, GPIO.LOW)
        else:
            GPIO.output(self.LED_PIN, GPIO.HIGH)
            # print(data)
            if data[:6] == '$VNACC' and len(data) == 33:
                logging.info(data)

    def connect(self):
        """Attempt to connect/reconnect to IMU
        Continiously blink LED until connected
        """

        while not self.initialize_IMU_serial_port():
            logging.info('Attempting to connect...')
            self.initialize_LED()
            self.blink_LED()

    def start(self):
        """Set status LED and start logger"""

        self.initial_startup = True
        while True:
            try:
                self.initialize_LED()
                if self.initial_startup:
                    self.connect()
                    self.initial_startup = False
                while True:
                    self.log_data()
            except KeyboardInterrupt:
                logging.info('ERROR: KeyboardInterrupt')
                logging.info('Cleanup GPIO ports')
                GPIO.cleanup()
                exit(1)
            # IMU disconnected
            except Exception as e:
                logging.info('IMU unplugged/disconnected')
                logging.info('ERROR: ' + str(e))
                self.ser.close()
                self.connect()
            GPIO.cleanup()

if __name__ == '__main__':
    logger = IMULogger()
