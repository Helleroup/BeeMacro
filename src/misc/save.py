import sqlite3
import tkinter
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
#customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("BeeMacro")
        self.geometry(f"{960}x{540}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)  # Don't expand column 0
        self.grid_columnconfigure(1, weight=1)

        self.navbar = customtkinter.CTkFrame(self, width=50, fg_color="red")
        self.navbar.grid(row=0, column=0, sticky="ns")
        self.navbar.grid_propagate(False)  # Prevent the frame from shrinking to fit its contents

        gatherIcon = customtkinter.CTkImage(Image.open("./src/app/img/gather_icon.png"), size=(32, 32))  # Adjust the path to your icon
        self.gatherbutton = customtkinter.CTkButton(self.navbar, width=38, height=38, image=gatherIcon, bg_color="blue", command=self.gather)
        self.gatherbutton.grid(row=0, column=0)

        self.main = customtkinter.CTkFrame(self, fg_color="green")
        self.main.grid(row=0, column=1, sticky="nsew")
        self.main.grid_rowconfigure(0, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

    def gather(self):
        self.clearMain()

        self.scrollFrame = customtkinter.CTkScrollableFrame(self.main, fg_color="#0D1B2A")
        self.scrollFrame.grid(row=0, column=0, sticky="nsew")

        self.addGatherTaskButton = customtkinter.CTkButton(self.scrollFrame, height=120, border_width=2, fg_color='transparent', border_color='#314458', text_color='#314458', text='➕', font=("Arial", 32), command=self.addGatherTask)
        self.addGatherTaskButton.pack(pady=15, padx=15, fill='x')

    def addGatherTask(self):
        print("Gathering tasks...")
        task = customtkinter.CTkFrame(self.scrollFrame, height=120, fg_color="lightblue")

        self.addGatherTaskButton.pack_forget()  # Hide the button after adding a task
        task.pack(pady=15, padx=15, fill='x')
        self.addGatherTaskButton.pack(pady=15, padx=15, fill='x')

    def clearMain(self):
        for widget in self.main.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
