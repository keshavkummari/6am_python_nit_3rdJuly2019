# GUI Programming (Tkinter) :

"""
Python provides various options for developing graphical user interfaces (GUIs). 

Tkinter: Tkinter is the Python interface to the Tk GUI toolkit shipped with Python. 

wxPython: This is an open-source Python interface for wxWidgets GUI toolkit. 

PyQt:This is also a Python interface for a popular cross-platform Qt GUI library. 

JPython: JPython is a Python port for Java which gives Python scripts seamless
access to Java class libraries on the local machine http://www.jython.org

There are many other interfaces available
"""

"""
# Tkinter Programming :

Tkinter is the standard GUI library for Python. 

Python when combined with Tkinter provides a fast and easy way to create GUI applications. 

Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

Creating a GUI application using Tkinter is an easy task. 

	1. Import the Tkinter module.

	2. Create the GUI application main window.

	3. Add one or more of the widgets to the GUI application.

	4. Enter the main event loop to take action against each event triggered by the user.

"""

# Button Creation :

from Tkinter import *
from Tkinter import messagebox
#from Tkinter import Messagebox

top = Tk()

top.geometry("500x500")

def helloCallBack():
    msg = messagebox.showinfo("Home", "Welcome to Python World")

b = Button(top, text="Clic to Login", command=helloCallBack)
b.place(x=10,y=10)

top.mainloop()
