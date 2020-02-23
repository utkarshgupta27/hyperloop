#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define MIN_PULSE_WIDTH 650
#define MAX_PULSE_WIDTH 2350
#define DEFAULT_PULSE_WIDTH 1500
#define FREQUENCY 50

uint8_t servonum = 0;

void setup() 
{
Serial.begin(9600);
Serial.println("16 channel Servo test!");
pwm.begin();
pwm.setPWMFreq(FREQUENCY);
}
int pulseWidth(int angle)
{
int pulse_wide, analog_value;
pulse_wide = map(angle, 0, 180, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
analog_value = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
Serial.println(analog_value);
return analog_value;
}

void loop() {
pwm.setPWM(0, 0, pulseWidth(0));
delay(1000);
pwm.setPWM(0, 0, pulseWidth(120));
delay(500);
pwm.setPWM(0, 0, pulseWidth(90));
delay(1000);

}
