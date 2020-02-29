#!/usr/bin/python
# Made by Utkarsh Gupta!! github@utkarshkg123!!
# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
#
import os  # importing os library so as to communicate with the system
import time  # importing time library to make Rpi wait because its too impatient

os.system ("sudo pigpio") #Launching GPIO library
time.sleep(1)  # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio  # importing GPIO library

import tkinter
from tkinter import *
from tkinter import ttk
import logging
import coloredlogs
import sys
from tkinter.scrolledtext import ScrolledText
import threading

window = Tk()
window.geometry("1240x640")
window.title("Throttle_Set")
window.resizable(True, True)
window["bg"]= '#49A'

left_frame = Frame(window, bg='#49A')
right_frame = Frame(window, bg='#49A')

def main():
    ## left_frame # calibration part
    path = 'C:/Users/utkar/Downloads/instructable_pwm/gpio_pins_pi.gif'
    photo = PhotoImage(file=path)
    pic = Label(right_frame, image=photo)
    pic.image=photo
    pic.grid(row=1, column=0)

    frame00 = Frame(left_frame,bg='light grey')
    label_widget_00_0 = Label(frame00, text="Connect Motor_ESC to\nPWM pin 32(pwm 0)", pady=1, bg="light green",
                              font="Times 12")
    var = DoubleVar(value=200)
    label_widget_00_1 = Spinbox(frame00, from_=0, to=4095.0, width=20, borderwidth=2, justify=RIGHT,
                                validate="all", textvariable=var, font="Times 12 bold")
    label_widget_00_0.grid(row=0, column=0, sticky=W + E + N + S,pady=5)
    label_widget_00_1.grid(row=1, column=0, sticky=N, padx=1,pady=5)

    ##ESC = 32  # Connect the ESC in this GPIO pin
    btn_00 = Button(frame00, text="Calibrate_M1", activeforeground='black',
                   activebackground='green', width=20, bd=4, command=calibrate(32))
    btn_00.grid(row=0, column=1, sticky=W + E + N + S, padx=5, pady=5)
    btn_01 = Button(frame00, text="Arm+Control", activeforeground='black',
                   activebackground='green', width=20, bd=4, command=arm(32))
    btn_01.grid(row=1, column=1, sticky=W + E + N + S, padx=5, pady=5)

    frame00.grid(row=0, column=0, padx=10, pady=15, sticky=E + W + N + S)

    frame01 = Frame(left_frame, bg='light grey')
    label_widget_01_0 = Label(frame01, text="Connect Motor_ESC to\nPWM pin 12(pwm 0)", pady=1, bg="light green",
                              font="Times 12")
    var = DoubleVar(value=200)
    label_widget_01_1 = Spinbox(frame01, from_=0, to=4095.0, width=20, borderwidth=2, justify=RIGHT,
                                validate="all", textvariable=var, font="Times 12 bold")
    label_widget_01_0.grid(row=0, column=0, sticky=W + E + N + S)
    label_widget_01_1.grid(row=1, column=0, sticky=N, padx=1)
    ##ESC = 12  # Connect the ESC in this GPIO pin
    btn_10 = Button(frame01, text="Calibrate_M2", activeforeground='black', activebackground='green', width=20,
                   bd=4, command=calibrate(12))
    btn_10.grid(row=0, column=1, sticky=W + E + N + S, padx=5, pady=5)
    btn_11 = Button(frame01, text="Arm+Control", activeforeground='black', activebackground='green', width=20,
                   bd=4, command=arm(12))
    btn_11.grid(row=1, column=1, sticky=W + E + N + S, padx=5, pady=5)
    frame01.grid(row=1, column=0, padx=10, pady=15, sticky=E + W + N + S)

    frame02 = Frame(left_frame, bg='light grey')
    label_widget_10_0 = Label(frame02, text="Connect Motor_ESC to\nPWM pin 33(pwm 1)", pady=1, bg="light green",
                              font="Times 12")
    var = DoubleVar(value=200)
    label_widget_10_1 = Spinbox(frame02, from_=0, to=4095.0, width=20, borderwidth=2, justify=RIGHT,
                                validate="all", textvariable=var, font="Times 12 bold")
    label_widget_10_0.grid(row=0, column=0, sticky=W + E + N + S)
    label_widget_10_1.grid(row=1, column=0, sticky=N, padx=1)
    ## ESC = 33  # Connect the ESC in this GPIO pin
    btn_20 = Button(frame02, text="Calibrate_M3", activeforeground='black', activebackground='green', width=20,
                   bd=4, command=calibrate(33))
    btn_20.grid(row=0, column=1, sticky=W + E + N + S, padx=5, pady=5)
    btn_21 = Button(frame02, text="Arm+Control", activeforeground='black', activebackground='green', width=20,
                    bd=4, command=arm(33))
    btn_21.grid(row=1, column=1, sticky=W + E + N + S, padx=5, pady=5)
    frame02.grid(row=2, column=0, padx=10, pady=15, sticky=E + W + N + S)
    frame03 = Frame(left_frame, bg='light grey')
    label_widget_11_0 = Label(frame03, text="Connect Motor_ESC to\nPWM pin 35(pwm 1)", pady=1, bg="light green",
                              font="Times 12")
    var = DoubleVar(value=200)
    label_widget_11_1 = Spinbox(frame03, from_=0, to=4095.0, width=20, borderwidth=2, justify=RIGHT,
                                validate="all", textvariable=var, font="Times 12 bold")
    ##ESC = 35  # Connect the ESC in this GPIO pin
    label_widget_11_0.grid(row=0, column=0, sticky=W + E + N + S)
    label_widget_11_1.grid(row=1, column=0, sticky=N, padx=1)
    btn_30 = Button(frame03, text="Calibrate_M4", activeforeground='black', activebackground='green', width=20,
                   bd=4, command=calibrate(35))
    btn_30.grid(row=0, column=1, sticky=W + E + N + S, padx=5, pady=5)
    btn_31 = Button(frame03, text="Arm+Control", activeforeground='black', activebackground='green', width=20,
                   bd=4, command=arm(35))
    btn_31.grid(row=1, column=1, sticky=W + E + N + S, padx=5, pady=5)
    frame03.grid(row=3, column=0, padx=10, pady=15, sticky=E + W + N + S)

    btn4 = Button(left_frame, text="Stop", activeforeground='black', activebackground='orange', width=20,
                   bd=4, command=stop())
    btn4.grid(row=4,column=0,columnspan=2, padx=10, pady=15,sticky=E+W+N+S)
    btn5 = Button(left_frame, text="All_Motors_Control", activeforeground='black', activebackground='light green', width=20,
                  bd=4, command=control_4M())
    btn5.grid(row=5, column=0, columnspan=2, padx=10, pady=15, sticky=E + W + N + S)
    left_frame.grid(row=0, column=0, padx=10, pady=5, sticky=E + W + N + S)


class TextHandler(logging.Handler):
    """This class allows you to log to a Tkinter Text or ScrolledText widget"""

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state='normal')
            self.text.insert(tkinter.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tkinter.END)

        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)


if __name__ == '__main__':
    st = ScrolledText(right_frame, state='disabled')
    st.configure(font='TkFixedFont')
    st.grid(row=0, column=0, sticky=E + N + S, padx=1, pady=1)
    right_frame.grid(row=0, column=1, padx=10, pady=5, sticky=E + W + N + S)
    # Create textLogger
    text_handler = TextHandler(st)
    # Add the handler to logger
    logging.getLogger().setLevel(logging.DEBUG)
    logger = logging.getLogger()
    coloredlogs.install(level='DEBUG', logger=logger)
    logger.addHandler(text_handler)
    # Log some messages
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

pi = pigpio.pi()

max_value = 2000  # change this if your ESC's max value is different or leave it be
min_value = 700  # change this if your ESC's min value is different or leave it be
logger.info("For first time launch, first do calibration")

def calibrate(ESC):  # This is the auto calibration procedure of a normal ESC
    pi.set_servo_pulsewidth(ESC, 0)
    logger.info("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        logger.info(
            "Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if inp == '':
            pi.set_servo_pulsewidth(ESC, min_value)
            logger.info("Wierd eh! Special tone")
            time.sleep(7)
            logger.info("Wait for it ....")
            time.sleep(5)
            logger.info("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            logger.info("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            logger.info("See.... uhhhhh")
            control(ESC)  # You can change this to any other function you want

def control(ESC):
    logger.info("I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
    time.sleep(1)
    speed = 1500  # change your speed if you want to.... it should be between 700 - 2000
    logger.info(
        "Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed or x to stop or z to arm again")
    logger.warning(
        "Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed or x to stop or z to arm again")
    while True:
        pi.set_servo_pulsewidth(ESC, speed)
        inp = input()

        if inp == "q":
            speed -= 100  # decrementing the speed like hell
            logger.info("speed = %d" % speed)
        elif inp == "e":
            speed += 100  # incrementing the speed like hell
            logger.info("speed = %d" % speed)
        elif inp == "d":
            speed += 10  # incrementing the speed
            logger.info("speed = %d" % speed)
        elif inp == "a":
            speed -= 10  # decrementing the speed
            logger.info("speed = %d" % speed)
        elif inp == "x":
            stop(ESC)  # going for the stop function
            break
        elif inp == "z":
            arm(ESC)
            break
        else:
            logger.warning("WHAT DID I SAID!! Press a,q,d,e or x for stop or z for arm")


def arm(ESC):  # This is the arming procedure of an ESC
    logger.info("Connect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, 0)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, max_value)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, min_value)
        time.sleep(1)
        control(ESC)


def stop(ESC):  # This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()

def control_4M():
    logger.warning("I hope you did calibration of all motors")
    logger.info("Connect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(32, 0)
        pi.set_servo_pulsewidth(12, 0)
        pi.set_servo_pulsewidth(33, 0)
        pi.set_servo_pulsewidth(35, 0)
        time.sleep(1)
        pi.set_servo_pulsewidth(32, max_value)
        pi.set_servo_pulsewidth(12, max_value)
        pi.set_servo_pulsewidth(33, max_value)
        pi.set_servo_pulsewidth(35, max_value)
        time.sleep(1)
        pi.set_servo_pulsewidth(32, min_value)
        pi.set_servo_pulsewidth(12, min_value)
        pi.set_servo_pulsewidth(33, min_value)
        pi.set_servo_pulsewidth(35, min_value)
        time.sleep(1)
        logger.info("I'm Starting the motor, I hope its calibrated and armed")
        time.sleep(1)
        speed = 1300  # change your speed if you want to.... it should be between 700 - 2000
        logger.info(
            "USER Controls like - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed or x to stop or z to arm again")
        while True:
            pi.set_servo_pulsewidth(32, speed)
            pi.set_servo_pulsewidth(12, speed)
            pi.set_servo_pulsewidth(33, speed)
            pi.set_servo_pulsewidth(35, speed)
            inp = input()

            if inp == "q":
                speed -= 100  # decrementing the speed like hell
                logger.info("speed = %d" % speed)
            elif inp == "e":
                speed += 100  # incrementing the speed like hell
                logger.info("speed = %d" % speed)
            elif inp == "d":
                speed += 10  # incrementing the speed
                logger.info("speed = %d" % speed)
            elif inp == "a":
                speed -= 10  # decrementing the speed
                logger.info("speed = %d" % speed)
            elif inp == "x":
                stop(32)  # going for the stop function
                stop(12)
                stop(33)
                stop(35)
                break
            elif inp == "z":
                arm(32)
                arm(12)
                arm(33)
                arm(35)
                break
            else:
                logger.warning("WHAT DID I SAID!! Press a,q,d,e or x for stop or z for arm")

main()
window.mainloop()
