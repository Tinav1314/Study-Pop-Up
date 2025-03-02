import inputQs
import time
# module for the gui
import tkinter as tk

import PIL 
from PIL import Image, ImageTk

# module for random
import random

# base application window
root = tk.Tk()



taskCompleted = False  # Flag to track task completion
def main():
    taskCompleted = False
    root.protocol("WM_DELETE_WINDOW", close)
    f = open('Questions.txt', 'r')
    questionFile = f.readlines()
    f.close()

    f = open('Answers.txt', 'r')
    answerFile = f.readlines()
    f.close()

    randomInt = random.randint(1, inputQs.getIndex())
    question = ""

    cq = 0
    for x in questionFile:
        cq += 1
        if(randomInt == cq):
            question = x
            break

    ca = 0
    for x in answerFile:
        ca += 1
        if(randomInt == ca):
            answer = x
            break



    root.title("STUDY TIME!!")

    # gets the size of the screen of the device
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # gets the middle of the screen
    x = (screen_width - 800) // 2
    y = (screen_height - 600) // 2
    root.geometry(f"{800}x{600}+{x}+{y}")

    root.resizable(False, False)

    # Load the image
    image = Image.open("q.png")  # Replace with your image path
    image = image.resize((300, 150))  # Resize if necessary
    photo = ImageTk.PhotoImage(image)

    imageLabel = tk.Label(root, image=photo)
    imageLabel.place(x=250, y=20)

    questionLabel = tk.Label(root, text = "", font=("Calibri", 13))
    questionLabel.config(text="")
    questionLabel.config(text=question)
    questionLabel.pack(pady=(10, 10))
    questionLabel.place(x = 300, y=250)



    imageB = Image.open("a.png")  # Replace with your image path
    imageB = imageB.resize((300, 150))  # Resize if necessary
    photoB = ImageTk.PhotoImage(imageB)

    imageBLabel = tk.Label(root, image=photoB)
    imageBLabel.place(x=250, y=300)

    inputAns = tk.Entry(root, width=30)
    inputAns.pack(pady=5, padx=10)
    inputAns.place(x = 300, y=500)

    
    correctLabel = tk.Label(root, text="", font=("Arial", 13)) 
    correctLabel.config(text = "")
    correctLabel.pack(pady=(10, 10))
    correctLabel.update()
    correctLabel.place(x = 350, y=375)

    
    textValue = inputAns.get()  
    def get_text(event=None): 
        textValue = inputAns.get()  
        if(textValue.lower().strip() == answer.lower().strip()):
            correctLabel.config(text="Correct Answer")
            taskCompleted == True
            root.after(2000, lambda: (hideWindow(), correctLabel.destroy(), questionLabel.destroy()))
        else:
            correctLabel.config(text="Incorrect Answer")

    inputAns.bind("<Return>", get_text)

# Function to keep the window always on top
def keepOnTop():
    """Re-enforce the 'Always on Top' attribute every second"""
    root.attributes("-topmost", True)
    root.after(1000, lambda: keepOnTop)    

# Function to prevent manual closing of the window until task is done
def close():
    if taskCompleted:
        hideWindow()
    else:
        print("❌ Task not completed, cannot close the window!")

def hideWindow():
    """Hide the application window temporarily."""
    root.withdraw()  # Hide window
    root.after(random.randint(3000,5000), showWindow)  # Schedule reappearance
    # the time should be changed but just for ease of testing

def showWindow():
    """Show the application window again."""
    preventMinimize()
    main()
    root.deiconify()  # Restore window

def preventMinimize():
    """Detect if the window is minimized and restore it"""
    if root.state() == "iconic":  # If minimized, restore
        root.deiconify()
    root.after(1000, preventMinimize)  # Check every second

hideWindow()
keepOnTop()
# Prevent window from being manually closed until task is done
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()

