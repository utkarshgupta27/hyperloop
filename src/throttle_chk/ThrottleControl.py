from pca9685 import PCA_9685
from tkinter import *
PWM_FULL_REVERSE = 204 # 1ms/20ms * 4096
PWM_NEUTRAL = 307      # 1.5ms/20ms * 4096
PWM_FULL_FORWARD = 409 # 2ms/20ms * 4096

currentPWM = float(PWM_NEUTRAL)


def updatePWM():
    global currentPWM
    PCA_9685.set_pwm(channel=0, value=currentPWM)

    if (currentPWM < PWM_FULL_REVERSE) | (currentPWM > PWM_FULL_FORWARD):
        labelframe_widget_0.config(activebackground="red")
    label_widget_0.get()


def on_decrementbutton_clicked():
    global currentPWM
    currentPWM -= 1
    updatePWM()


def on_neutralbutton_clicked():
    global  currentPWM
    currentPWM = PWM_NEUTRAL
    updatePWM()


def on_incrementbutton_clicked():
    global currentPWM
    currentPWM += 1
    updatePWM()

window = Tk()
window.geometry("791x564")
window.title("Throttle_Control_check")
labelframe_widget = LabelFrame(window, text="PWM Duty Cycle",bg = "light green",font = "Times 16")
label_widget=Label(labelframe_widget,
       text="50 Hz, 20ms frame, 12 bit resolution\nFull Reverse:\t1.0 ms - 204(ref)\nNeutral:\t\t1.5 ms - 307(ref)\nFull Forward:\t2.0 ms - 409(ref)",font="14")
labelframe_widget.pack(padx=10, pady=10)
labelframe_widget.place(x=500, y=20)
label_widget.pack()
btn_1 = Button(window, text="Decrement",activeforeground='green',activebackground='green', command = on_decrementbutton_clicked )
btn_1.place(x = 20, y = 190, width = 161, height =71)
btn_2 = Button(window, text="Neutral",activeforeground='green',activebackground='green', command = on_neutralbutton_clicked)
btn_2.place(x = 260, y = 190, width = 161, height = 71)
btn_3 = Button(window, text="Increment",activeforeground='green',activebackground='green', command= on_incrementbutton_clicked)
btn_3.place(x =500, y =190, width = 161, height = 71)
labelframe_widget_0 = LabelFrame(window, text="Set Duty Cycle",bg = "light green",font = "Times 14")
var = DoubleVar(value=PWM_NEUTRAL)
label_widget_0=Spinbox(labelframe_widget_0, from_=0, to=4095.0, width=20, borderwidth=2, justify=RIGHT, validate="all", textvariable=var,  font="Times 16 bold")
labelframe_widget_0.place(x=270, y=300,width=200,height=80)
label_widget_0.pack()

window.mainloop()

