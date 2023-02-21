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


# Define a class called "App" which inherits from the "tk.Tk" class in tkinter library
class App(tk.Tk):
    # The "__init__" method is used to initialize the class and set up the GUI.
    def __init__(self, *args, **kwargs):
        # Call the parent class constructor with the "*args" and "**kwargs" arguments
        tk.Tk.__init__(self, *args, **kwargs)
        # Create a Font object for regular text
        self.font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        # Create a Font object for a header
        self.header_font= tkfont.Font(family='Helvetica', size=30, weight="bold")
        # Create a Frame widget, which is a container for other widgets
        container = tk.Frame(self)
        # Pack the container widget to the top, fill the available space in both directions, and expand to fill the window
        container.pack(side="top", fill="both", expand=True)
        # Configure the first row of the container to have a weight of 1, which allows it to expand to fill the available vertical space
        container.grid_rowconfigure(0, weight=1)
        # Configure the first column of the container to have a weight of 1, which allows it to expand to fill the available horizontal space
        container.grid_columnconfigure(0, weight=1)

        # Create an empty dictionary to hold the frames for each page of the application
        self.frames = {}
        # For each page of the application (HomePage, Diagnosis, Statistics, Credits), create a frame and add it to the dictionary
        for F in (HomePage, Diagnosis, Statistics, Credits):
            # Get the name of the current page
            page_name = F.__name__
            # Create a new instance of the page's frame, passing in the container widget and the main controller (self) as arguments
            frame = F(parent=container, controller=self)
            # Add the new frame to the dictionary using the page name as the key
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise() #frames

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#b2d1d4') #background colour
        label = tk.Label(self, text="Home", font=controller.header_font,bg='#b2d1d4')
        label.place(x=10,y=10) #Home label
        label1=tk.Label(self,text="wavin",font=controller.font,bg='#b2d1d4')
        label1.place(x=250,y=250) #placement of label
        button1 = tk.Button(self, text="Diagnosis", # Diagnosis button
                            command=lambda: controller.show_frame("Diagnosis"),bg='#b2d1d4')
        button2 = tk.Button(self, text="Statistics", # Statistics button
                            command=lambda: controller.show_frame("Statistics"),bg='#b2d1d4')

        button3 = tk.Button(self, text="Credits", # Credits button
                            command=lambda: controller.show_frame("Credits"),bg='#b2d1d4')
        
        button1.place(x=10,y=60)# positions of buttons 1,2 and 3
        button2.place(x=10,y=90)
        button3.place(x=10,y=120)
        # quit button
        quit_button = tk.Button(self, text="Quit",
                            command=lambda: controller.destroy())
        quit_button.place(x=10,y=400)


class Diagnosis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#b2d1d4')
        label = tk.Label(self, text="Diagnosis", font=controller.header_font,bg='#b2d1d4')
        label.place(x=10,y=10)
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        button.place(x=10,y=60)
        entrytext = tk.StringVar()
        entry = tk.Entry(self,bg='#b2d1d4')
        entry.place(x=100,y=100)
        entry1 = tk.Entry(self,state='readonly', readonlybackground="white",textvariable=entrytext,width=30).place(x=100,y=160)
 
        def check():
            global resized_image1
            x = str(entry.get())
            img = image.load_img(x, target_size=(200, 200))
            img = img.convert("L")
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            img /= 255.0
            pred = model.predict(img)
            binary_pred = 1 if pred >= 0.5 else 0
            y = f'Pneumonia: {not binary_pred}'
            
            return entrytext.set(y)
            # Display or use the binary prediction as needed
        button1 = tk.Button(self,text='check',command=check)
        button1.place(x=100,y=130)
        model = load_model('pneumonia_detection_ai_version_3.h5')
        #adam = Adam(learning_rate=0.0001)
        '''model.compile(loss='binary_crossentropy',
              optimizer=adam,
              metrics=['acc'])'''

        
        #quit button
        quit_button = tk.Button(self, text="Quit",
                            command=lambda: controller.destroy())
        quit_button.place(x=10,y=400)

class Statistics(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#b2d1d4')
        label = tk.Label(self, text="Statistics", font=controller.header_font,bg='#b2d1d4')
        label.place(x=10,y=10)
        button = tk.Button(self, text="Home",bg='blue', #button
                           command=lambda: controller.show_frame("HomePage"))
        button.place(x=10,y=60)
        image1 = Image.open('stats1.png')#stats img1
        image2 = Image.open('stats2.png')#stats img2
        #resizing images
        resized_image1= image1.resize((350,255), Image.ANTIALIAS)
        resized_image2= image2.resize((350,255), Image.ANTIALIAS)
        #display resized images
        test2 = ImageTk.PhotoImage(resized_image2)
        test1 = ImageTk.PhotoImage(resized_image1)
        label2 = tk.Label(self,image=test2)
        label2.image = test2
        label1 = tk.Label(self,image=test1)
        label1.image=test1
        #place images
        label1.place(x=0,y=100)
        label2.place(x=350,y=100)
        
        
        #quit button
        quit_button = tk.Button(self, text="Quit",
                            command=lambda: controller.destroy())
        quit_button.place(x=10,y=400)
class Credits(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#b2d1d4')
        #credits
        label = tk.Label(self, text="Credits", font=controller.header_font,bg='#b2d1d4')
        label.place(x=10,y=10)
        button = tk.Button(self, text="Home",bg='blue',
                           command=lambda: controller.show_frame("HomePage"))
        button.place(x=10,y=60)
        label2 = tk.Label(self,text='AI coder lol:Ravin Nagpal\nNeo Gao En \nDarius Toh',font=controller.font,bg='#b2d1d4',anchor="e", justify='left')
        label2.place(x=10,y=120)
        #quit button
        quit_button = tk.Button(self, text="Quit",
                            command=lambda: controller.destroy())
        quit_button.place(x=10,y=400)
'''
class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

# Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
class Camera(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#30D5C8')
        label = tk.Label(self, text="Camera", font=controller.header_font,bg='#30D5C8')
        label.place(x=10,y=10)
        button = tk.Button(self, text="Home",bg='blue',
                           command=lambda: controller.show_frame("HomePage"))
        button.place(x=10,y=60)
        
         
        
        def open_camera():
            # intialize the webcam and pass a constant which is 0
            cam = cv2.VideoCapture(0)

            # title of the app
            cv2.namedWindow('python webcam screenshot app')

            #    let's assume the number of images gotten is 0
            img_counter = 0

            # while loop
            while True:
                # intializing the frame, ret
                ret, frame = cam.read()
                # if statement
                if not ret:
                    print('failed to grab frame')
                    break
                # the frame will show with the title of test
                cv2.imshow('test', frame)
                #to get continuous live video feed from my laptops webcam
                k  = cv2.waitKey(1)
                # if the escape key is been pressed, the app will stop
                if k%256 == 27:
                    print('escape hit, closing the app')
                    break
                # if the spacebar key is been pressed
                # screenshots will be taken
                elif k%256  == 32:
                # the format for storing the images scrreenshotted
                    img_name = f'testingimage_{img_counter}.png'
                    # saves the image as a png file
                    cv2.imwrite(img_name, frame)
                    print('screenshot taken')
                    break
                    # the number of images automaticallly increases by 1
                    img_counter += 1

            # release the camera
            cam.release()

            # stops the camera window
            cv2.destroyAllWindows()
        # Create a button to open the camera in GUI app
        button1 = tk.Button(self,text="open camera",command=open_camera)
        button1.place(x=10,y=300)
        #quit button
        quit_button = tk.Button(self, text="Quit",
                            command=lambda: controller.destroy())
        quit_button.place(x=10,y=400)


'''
if __name__ == "__main__":
    app = App()
    app.minsize(700,500)
    app.mainloop()
