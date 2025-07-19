import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Dynamic List Example")
        self.geometry("400x400")

        # Frame to contain list items
        self.list_frame = ctk.CTkFrame(self)
        self.list_frame.pack(pady=20, fill="both", expand=True)

        # Entry + Add button
        self.entry = ctk.CTkEntry(self, placeholder_text="Add item")
        self.entry.pack(pady=5)

        self.add_button = ctk.CTkButton(self, text="Add to list", command=self.add_item)
        self.add_button.pack(pady=5)

        # Internal list to track UI elements
        self.items = []

    def add_item(self):
        text = self.entry.get()
        if text:
            # Create a label for the new item
            label = ctk.CTkLabel(self.list_frame, text=text)
            label.pack(anchor="w", padx=10, pady=2)

            # Save it in the items list
            self.items.append(label)

            # Clear the entry
            self.entry.delete(0, "end")

app = App()
app.mainloop()
