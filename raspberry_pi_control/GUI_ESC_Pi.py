# Made by Utkarsh Gupta!! github@utkarshkg123!!
# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
#
import os  # importing os library so as to communicate with the system
import time  # importing time library to make Rpi wait because its too impatient
from tkinter import *
from ESC_Control_Calibrate import *

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

tab_parent = ttk.Notebook(window)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text="Calibration")
tab_parent.add(tab2, text="Control_motion")
tab_parent.pack(expand=1, fill='both')
# btn_0 = Button(window, text="Reset", activeforeground='green', activebackground='red', command=reset)
# btn_1 = Button(window, text="Full Reverse", activeforeground='green', activebackground='red',
#                command=on_reversebutton_clicked)
# btn_1.place(x=20, y=130, width=161, height=71)
# btn_2 = Button(window, text="Neutral", activeforeground='green', activebackground='red',
#                command=on_forwardbutton_clicked)
# btn_2.place(x=260, y=130, width=161, height=71)
# btn_3 = Button(window, text="Full forward", activeforeground='green', activebackground='red',
#                command=on_neutralbutton_clicked)
# btn_3.place(x=500, y=130, width=161, height=71)

window.mainloop()