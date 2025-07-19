import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Dynamic Scrollable List")
        self.geometry("400x500")

        # Scrollable frame to hold list items and the Add button
        self.list_frame = ctk.CTkScrollableFrame(self, width=350, height=400)
        self.list_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # List to keep track of label widgets
        self.items = []

        # Add entry field outside
        self.entry = ctk.CTkEntry(self, placeholder_text="Type item here")
        self.entry.pack(pady=5)

        # Add button INSIDE the scrollable list
        self.add_button = ctk.CTkButton(self.list_frame, text="➕ Add Item", command=self.add_item)
        self.add_button.pack(pady=5)

    def add_item(self):
        text = self.entry.get()
        if text:
            # Insert new label BEFORE the add button
            label = ctk.CTkLabel(self.list_frame, text=text)

            # Repack the add_button to be below the new label
            self.add_button.pack_forget()
            label.pack(pady=5, anchor="w")
            self.add_button.pack(pady=5)

            self.items.append(label)
            self.entry.delete(0, "end")

app = App()
app.mainloop()
