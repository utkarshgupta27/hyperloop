import time
import sys
from pca9685 import PCA_9685
from tkinter import *

THROTTLE_NEUTRAL = 307  # 1.5ms /  20ms  *  4096
THROTTLE_FULL_FORWARD = 409  # 2ms / 20ms * 4096
THROTTLE_FULL_REVERSE = 204  # 1ms / 20ms * 4096
window = Tk()
window.geometry("745x447")
window.title("Throttle_Set")
labelframe_widget = LabelFrame(window,
                               text="PWM Duty Cycle", bg="light green", font="Times 16")
label_widget = Label(labelframe_widget,
                     text="Full Reverse: 1.0 ms\nNeutral:\t1.5 ms\nFull Forward:2.0 ms")
labelframe_widget.pack(padx=10, pady=10)
labelframe_widget.place(x=20, y=10)
label_widget.pack()


def reset():
    try:
        PCA_9685.__init__()
    except:
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)
    PCA_9685.init(frequency=50)
    time.sleep(1)
    PCA_9685.set_pwm(channel=0, value=THROTTLE_NEUTRAL)


def on_reversebutton_clicked():
    PCA_9685.set_pwm(channel=0, value=THROTTLE_FULL_REVERSE)


def on_forwardbutton_clicked():
    PCA_9685.set_pwm(channel=0, value=THROTTLE_FULL_FORWARD)


def on_neutralbutton_clicked():
    PCA_9685.set_pwm(channel=0, value=THROTTLE_NEUTRAL)


btn_0 = Button(window, text="Reset", activeforeground='green', activebackground='red', command=reset)
btn_1 = Button(window, text="Full Reverse", activeforeground='green', activebackground='red',
               command=on_reversebutton_clicked)
btn_1.place(x=20, y=130, width=161, height=71)
btn_2 = Button(window, text="Neutral", activeforeground='green', activebackground='red',
               command=on_forwardbutton_clicked)
btn_2.place(x=260, y=130, width=161, height=71)
btn_3 = Button(window, text="Full forward", activeforeground='green', activebackground='red',
               command=on_neutralbutton_clicked)
btn_3.place(x=500, y=130, width=161, height=71)
window.mainloop()
