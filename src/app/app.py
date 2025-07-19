import customtkinter as ctk
from PIL import Image
import pages

ctk.set_appearance_mode("System")

class App(ctk.CTk):

    currentPage = None

    def __init__(self):
        super().__init__()

        self.title("BeeMacro")
        self.geometry("860x540")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Navigation bar
        self.navbar = ctk.CTkFrame(self, width=50, fg_color="red")
        self.navbar.grid(row=0, column=0, sticky="ns")
        self.navbar.grid_propagate(False)

        gatherIcon = ctk.CTkImage(Image.open("./src/app/img/gather_icon.png"), size=(32, 32))
        self.gatherbutton = ctk.CTkButton(self.navbar, width=38, height=38, image=gatherIcon, bg_color="blue", command=self.show_gather)
        self.gatherbutton.grid(row=0, column=0)

        collectIcon = ctk.CTkImage(Image.open("./src/app/img/collect_icon.png"), size=(32, 32))
        self.collectbutton = ctk.CTkButton(self.navbar, width=38, height=38, image=collectIcon, bg_color="blue", command=self.show_collect)
        self.collectbutton.grid(row=1, column=0)

        # Main content area
        self.main = ctk.CTkFrame(self, fg_color="green")
        self.main.grid(row=0, column=1, sticky="nsew")
        self.main.grid_rowconfigure(0, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        # Initialize the GatherPage
        self.show_gather()

    def clear_main(self):
        for widget in self.main.winfo_children():
            widget.destroy()

    def show_gather(self):
        if self.currentPage != 'gather':
            self.clear_main()
            page = pages.GatherPage(self.main)
            page.grid(row=0, column=0, sticky="nsew")
            self.currentPage = 'gather'

    def show_collect(self):
        if self.currentPage != 'collect':
            self.clear_main()
            page = pages.CollectPage(self.main)
            page.grid(row=0, column=0, sticky="nsew")
            self.currentPage = 'collect'
