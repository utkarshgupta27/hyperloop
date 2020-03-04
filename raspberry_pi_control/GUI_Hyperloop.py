#!/usr/bin/python
""" Made by Utkarsh Gupta!! github@utkarshkg123!!"""
import tkinter
import threading
import os  # importing os library so as to communicate with the system
import time  # importing time library to make Rpi wait because its too impatient
os.system("sudo pigpiod")  # Launching GPIO library
import pigpio  # importing GPIO library
from tkinter import *
import logging
from tkinter.scrolledtext import ScrolledText

print = lambda *tup: logging.getLogger(__name__).info(str(" ".join([str(x) for x in tup])))
logger = logging.getLogger(__name__)
speed = 1200
max_value = 2400  # change this if your ESC's max value is different or leave it be
min_value = 650
freq=None
esc=18
class hyperloop_control(tkinter.Frame):
    logger = logging.getLogger(__name__)

    def __init__(self, master=None):
        self.pi = pigpio.pi()
        self.max_value = 2400
        self.min_value=650
        self.esc=18
        Frame.__init__(self, master)
        self.logger.info("For first time launch, first do calibration")

        self.left_frame = Frame(window, width=200, height=400, bg='light grey')
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)

        self.tool_bar = Frame(self.left_frame, width=180, height=185)
        self.tool_bar.grid(row=3, column=0, padx=5, pady=5)

        self.label1 = Label(self.left_frame,
                            text="Connect Motor_ESC to\nPWM pin 12(pwm 0)\nDanger: Dont click run before calibration",
                            pady=1, bg="light green",
                            font="Times 12")
        self.label1.grid(row=0, column=0)

        self.B_calibrate = Button(self.left_frame, text="Calibrate", width=25, height=2, activeforeground='black',
                                  activebackground='green',
                                  command=lambda: threading.Thread(target=ButtonFunc.onCalibration, args=(2,)).start())
        self.B_calibrate.grid(row=1, column=0, padx=15, pady=15)

        self.B_arm_control = Button(self.left_frame, text="run(arm_control)", width=25, height=2,
                                    activeforeground='black', activebackground='green',
                                    command=lambda: threading.Thread(target=ButtonFunc.onRun, args=(2,)).start())
        self.B_arm_control.grid(row=2, column=0, padx=15, pady=15)

        self.B_right = Button(self.tool_bar, text=">", width=10, height=2, activeforeground='black',
                              activebackground='green', command=ButtonFunc.onArrowRight)
        self.B_right.grid(row=0, column=1, padx=5, pady=5)

        self.B_left = Button(self.tool_bar, text="<", width=10, height=2, activeforeground='black',
                             activebackground='green', command=ButtonFunc.onArrowLeft)
        self.B_left.grid(row=0, column=0, padx=5, pady=5)
        #var = DoubleVar(value=self.pi.get_servo_pulsewidth(self.esc))
##        #self.spinbox = Spinbox(self.tool_bar, from_=0, to=2395.0, width=20, borderwidth=2, justify=RIGHT,
##                               validate="all", textvariable=var, font="Times 12 bold")
##        self.spinbox.grid(row=1, column=0, columnspan=2)

        self.B_right_frequent = Button(self.tool_bar, text=">>>>", width=10, activeforeground='black',
                                       activebackground='green', command=ButtonFunc.onAcceleration)
        self.B_right_frequent.grid(row=2, column=1, padx=5, pady=5)

        self.B_left_frequent = Button(self.tool_bar, text="<<<<", width=10, activeforeground='black',
                                      activebackground='green', command=ButtonFunc.onDeceleration)
        self.B_left_frequent.grid(row=2, column=0, padx=5, pady=5)

        self.B_stop = Button(self.left_frame, text="Stop", width=25, height=2, activeforeground='black',
                             activebackground='green',
                             command=lambda: threading.Thread(target=ButtonFunc.onSpaceBar, args=(2,)).start())
        self.B_stop.grid(row=4, column=0, padx=15, pady=15)
        self.method=Label(window, bg='light grey',font=12,text="for calibration first Disconnect the battery and then press calibration\n for arming connect the batteries and then press arm_control\n Controls - \nleft (<) key to decrease speed & \nright (>) key to increase speed OR \n'd' or (<<<<) to decrease a lot of speed & \n'a' or (>>>>) to increase a lot of speed or \n'spacebar' to stop")
        self.method.grid(row=1,column=0,columnspan=2,padx=15,pady=15,sticky="NSEW")
        self.tool_bar = Frame(right_frame)
        self.tool_bar.grid(row=1, column=0, padx=2, pady=2,sticky="NSEW")
        self.freq=Label(self.tool_bar,bg='light grey',text="Frequency in GPIO")
        self.freq.grid(row=0,column=0,padx=1,pady=1,sticky="NSEW")
        self.freq_get = Message(self.tool_bar, bg='white',
                                 text=int(self.pi.get_PWM_frequency(self.esc)))
        self.freq_get.grid(row=0, column=1, padx=1, pady=1, sticky="NSEW")
        #self.duty_cycle = Label(self.tool_bar, bg='light grey',
        #                         text="duty_cycle")
        #self.duty_cycle.grid(row=0, column=2, padx=1, pady=1, sticky="NSEW")
        #self.duty_cycle_get = Message(self.tool_bar, bg='white',
        #                         text=int(self.pi.get_PWM_dutycycle(self.esc)))
        #self.duty_cycle_get.grid(row=0, column=3, padx=1, pady=1, sticky="NSEW")
    def updateSpeed(self):
        global speed
        self.pi.set_servo_pulsewidth(self.esc, speed)

        if (speed < min_value) | (speed > max_value):
            self.spinbox.config(activebackground="red")
        #self.spinbox.get()

    def calibrate(self):
        """
        This trains the ESC on the full scale (max - min range) of the controller / pulse generator.
        This only needs to be done when changing controllers, transmitters, etc. not upon every power-on.
        NB: if already calibrated, full throttle will be applied (briefly)!  Disconnect propellers, etc.
        """
        self.pi.set_servo_pulsewidth(self.esc, 0)
        self.logger.info("I hope battery is disconnected")
        self.pi.set_servo_pulsewidth(self.esc, self.max_value)
        self.logger.info(
            "Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone")
        self.pi.set_servo_pulsewidth(self.esc, self.min_value)
        self.logger.info("Wierd eh! Special tone")
        time.sleep(7)
        self.logger.info("Wait for it ....")
        time.sleep(5)
        self.logger.info("Finished calibration....")
        self.pi.set_servo_pulsewidth(self.esc, 0)
        time.sleep(2)
        self.logger.info("Now you can arm it....")

    def arm_control(self):
        """
            Arms the ESC. Required upon every power cycle.
        """
        self.logger.info("I hope batteries are connected")
        self.logger.info("Arming....")
        self.pi.set_servo_pulsewidth(self.esc, 0)
        time.sleep(2)
        self.pi.set_servo_pulsewidth(self.esc, 650)
        time.sleep(2)
        self.logger.info("Armed.....")
        self.pi.set_servo_pulsewidth(self.esc, 1200)
        self.logger.info(
            "I'm Starting the motor, I hope its calibrated and armed, if not stop this program by giving 'x'")
        time.sleep(1)
        self.logger.info(
            "Controls - \nleft (<) key to decrease speed & \nright (>) key to increase speed OR \n'd' or (<<<<) to decrease a lot of speed & \n'a' or (>>>>) to increase a lot of speed or \n'spacebar' to stop")

    def stop(self):
        """
        Switch of the GPIO, and un-arm the ESC.
        Ensure this runs, even on unclean shutdown.
        """
        self.logger.info("slowing......")
        self.pi.set_servo_pulsewidth(self.esc, 1200)
        time.sleep(1)
        #self.logger.info("Failsafe...")
        self.pi.set_servo_pulsewidth(self.esc, 0)
        #self.logger.info("Disabling GPIO.")
        #self.pi.stop()
        self.logger.info("Halted.")


class ButtonFunc():

    def __init__(self, master=None):
        self.onArrowLeft()
        self.onArrowRight()
        self.onSpaceBar()
        self.onAcceleration()
        self.onDeceleration()
        self.onRun()
        self.onCalibration()

    def onEnter(event=None):
        logger.info("Enter")

    def onRun(event=None):
        hyperloop_control().arm_control()
        logger.info("run clicked")

    def onCalibration(event=None):
        hyperloop_control().calibrate()
        logger.info("calibration clicked")

    def onArrowLeft(event=None):
        global speed
        speed -= 1
        hyperloop_control().updateSpeed()
        logger.info("speed set to = %d" % speed)

    def onAcceleration(event=None):
        global speed
        speed += 50
        hyperloop_control().updateSpeed()
        logger.info("speed set to = %d" % speed)

    def onDeceleration(event=None):
        global speed
        speed -= 50
        hyperloop_control().updateSpeed()
        logger.info("speed set to = %d" % speed)

    def onArrowRight(event=None):
        global speed
        speed += 1
        hyperloop_control().updateSpeed()
        logger.info("speed set to = %d" % speed)

    def onSpaceBar(event=None):
        global speed
        hyperloop_control().stop()
        logger.info("speed = 0")
        # speed = 0
        # hyperloop_control().spinbox.get()

    # def Keyboard_Interrupt(self):
    #    self.pi.set_servo_pulsewidth(self.esc, 0)


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
    window = tkinter.Tk()
    window.title("Motor Control GUI")
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth() / 3 - windowWidth / 2)
    positionDown = int(window.winfo_screenheight() / 4 - windowHeight / 2)

    # Position the window
    window.geometry("950x650+{}+{}".format(positionRight, positionDown))

    window.resizable(False, False)
    # window.config(bg="#7F7F7F")
    # Keyboard Input
    window.bind('<Left>', ButtonFunc.onArrowLeft)
    window.bind('<Right>', ButtonFunc.onArrowRight)
    window.bind('<Return>', ButtonFunc.onEnter)
    window.bind('<space>', ButtonFunc.onSpaceBar)
    window.bind('a', ButtonFunc.onAcceleration)
    window.bind('d', ButtonFunc.onDeceleration)
    window.focus()
    # Keyboard Input End

    right_frame = Frame(window, bg='light grey')
    right_frame.grid(row=0, column=1, sticky="nsew")
    st = ScrolledText(right_frame, state='disabled')
    st.configure(font='TkFixedFont')
    st.grid(row=0, column=0, sticky=NE + SE, padx=5, pady=1)
    # Create textLogger
    text_handler = TextHandler(st)
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(message)s')
    # coloredlogs.install(level='DEBUG', logger=logger)
    logger.addHandler(text_handler)
    logger.critical("Log_data")
    app = hyperloop_control(master=window)
    window.mainloop()
