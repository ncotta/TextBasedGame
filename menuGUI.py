from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open("background_image.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        text = Label(self, text="Dragons & Dungeons", fg="red", bg="gray", font=("Times", 20, "bold"))
        text.pack(fill=BOTH, pady=2, padx=2)

        # START BUTTON
        startButton = Button(self, text="Start", font="Times", command=self.clickStartButton)
        startButton.place(x=280, y=350)

        # HELP BUTTON
        helpButton = Button(self, text="Help", font="Times", command=self.clickHelpButton)
        helpButton.place(x=380, y=350)

        # EXIT BUTTON
        exitButton = Button(self, text="Exit", font="Times", command=self.clickExitButton)
        exitButton.place(x=480, y=350)

    def clickStartButton(self):
        print("Starting!")

    def clickHelpButton(self):
        pass

    def clickExitButton(self):
        exit()


root = Tk()
app = Window(root)
root.wm_title("Dragons & Dungeons")
root.geometry("800x600")
root.mainloop()
