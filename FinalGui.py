import tkinter as tk  # import the Tkinter module to create a GUI
from tkinter import font as tkfont  # import the font module for tkinter
from sys import platform  # import the sys module to get platform-specific information
import PIL  # import the PIL module to work with images
from PIL import ImageTk, Image  # import the modules to create images in Tkinter
import os  # import the os module to work with the operating system
from keras.models import load_model  # import a Keras deep learning model
from tensorflow.keras.preprocessing import image  # import the image preprocessing module
import numpy as np  # import the numpy module for numerical computing
from tensorflow.keras.optimizers import Adam  # import the Adam optimizer for the deep learning model
if platform == "darwin":  # check if the operating system is Mac OS
    from tkmacosx import Button  # import the button module for Mac OS

# Define a new app class that extends Tk
class App(tk.Tk):

    # Define the app constructor
    def __init__(self, *args, **kwargs):
        # Call the constructor of the parent class
        tk.Tk.__init__(self, *args, **kwargs)

        # Set up some fonts to use in the app
        self.font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.header_font= tkfont.Font(family='Helvetica', size=30, weight="bold")

        # Create a container to hold the different pages of the app
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create a dictionary to hold the different pages
        self.frames = {}

        # Iterate over the different pages and add them to the dictionary
        for F in (HomePage, Diagnosis, Statistics,Credits):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the home page
        self.show_frame("HomePage")

    # Define a method to show a particular page
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

# Define a class for the home page
class HomePage(tk.Frame):

    # Define the constructor for the home page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#b2d1d4')

        # Add some labels and buttons to the home page
        label = tk.Label(self, text="Home", font=controller.header_font,bg='#b2d1d4')
        label.place(x=10,y=10)
        label1=tk.Label(self,text="wavin",font=controller.font,bg='#b2d1d4')
        label1.place(x=250,y=250)
        button1 = tk.Button(self, text="Diagnosis", command=lambda: controller.show_frame("Diagnosis"),bg='#b2d1d4')
        button2 = tk.Button(self, text="Statistics", command=lambda: controller.show_frame("Statistics"),bg='#b2d1d4')
        button3 = tk.Button(self, text="Credits", command=lambda: controller.show_frame("Credits"),bg='#b2d1d4')
        button1.place(x=10,y=
