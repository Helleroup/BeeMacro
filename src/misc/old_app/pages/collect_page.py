import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
import sqlitedict as sqld  # Adjust the import based on your project structure

class CollectPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color="#0D1B2A")
