import customtkinter as ctk
from PIL import Image, ImageTk
import sys
import os
import random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
import sqlitedict as sqld  # Adjust the import based on your project structure

class GatherPage(ctk.CTkScrollableFrame):

    fieldTable = sqld.get('game', 'fields')
    fields = []
    for index, data in fieldTable.items():
        fields.append(data['display_name'])

    def __init__(self, parent):
        super().__init__(parent, fg_color="#0D1B2A")

        self.addNewTaskButton = ctk.CTkButton(
            self, height=120, border_width=2,
            fg_color='transparent', border_color='#314458',
            text_color='#314458', text='➕', font=("Arial", 32),
            command=self.addTask
        )
        self.addNewTaskButton.pack(pady=15, padx=15, fill='x')
        self.reloadTasks()

    def reloadTasks(self):
        self.clear_frame()
        tasks = sqld.get('user', 'tasks')
        for index, data in tasks.items():
            field = data['field']
            taskContainer = ctk.CTkFrame(self, height=120, fg_color="#314458")
            taskContainer.pack_propagate(False)

            # Create the dropdown and store it in a variable
            fieldDropdown = ctk.CTkOptionMenu(taskContainer, values=self.fields, command=lambda value, rowid=data['rowid']: self.editTask(rowid=rowid, field=value))
            fieldDropdown.set(field)  # Set to current field
            fieldDropdown.pack(side='left', padx=8, pady=8)

            # Use a lambda that gets the CURRENT value from fieldDropdown when clicked
            patternButton = ctk.CTkButton(
                taskContainer,
                border_width=1,
                fg_color='transparent',
                border_color='red',
                text_color='red',
                text='pattern',
                command=lambda dropdown=fieldDropdown: self.editPattern(dropdown.get())
            )
            patternButton.pack(side='left', padx=8, pady=8)

            deleteButton = ctk.CTkButton(taskContainer, text='❌', font=("Arial", 32), width=104, height=104, command=lambda rowid=data['rowid']: self.removeTask(rowid))
            deleteButton.pack(anchor="e", padx=8, pady=8)

            self.addNewTaskButton.pack_forget()
            taskContainer.pack(pady=15, padx=15, fill='x')
            self.addNewTaskButton.pack(pady=15, padx=15, fill='x')

            print(f'added {index} for field {field}')

    def addTask(self, field='Sunflower Field', pattern=None,  shiftLock=False):

        taskTable = {
            'field': field,
            'pattern': pattern,
            'shift_lock': shiftLock
        }

        sqld.addRow('user', 'tasks', taskTable)
        self.reloadTasks()

    def editTask(self, rowid, field=None, pattern=None, shiftLock=None):
        if field:
            sqld.editRow('user', 'tasks', rowid, 'field', field)
        if pattern:
            sqld.editRow('user', 'tasks', rowid, 'pattern', pattern)
        if shiftLock is not None:
            sqld.editRow('user', 'tasks', rowid, 'shift_lock', shiftLock)
        #self.reloadTasks()

    def removeTask(self, rowid):
        sqld.removeRow('user', 'tasks', rowid)
        self.reloadTasks()

    def clear_frame(self):
        for widget in self.winfo_children():
            if widget != self.addNewTaskButton:  # Don't destroy the add button
                widget.destroy()

    def editPattern(self, field):
        fieldData = None
        for index, data in self.fieldTable.items():
            if data['display_name'] == field:
                fieldData = data
                break

        temp_window = ctk.CTkToplevel()
        temp_window.title(fieldData['display_name'])

        temp_window.geometry(f"{(fieldData['width'] * 23)  + (50 * 2)}x{(fieldData['height'] * 23) + (50 * 2) + 50}")
        temp_window.grab_set()
        temp_window.resizable(False, False)

        # Create the container first
        fieldContainer = ctk.CTkFrame(temp_window, fg_color='transparent', width=fieldData['width'] * 23, height=fieldData['height'] * 23, corner_radius=0)
        fieldContainer.pack_propagate(False)  # ← This prevents the frame from shrinking
        fieldContainer.pack(pady=50, padx=50, side='top')

        # Create the image with explicit size to match container dimensions
        fieldImage = ctk.CTkImage(
            Image.open(f"./src/app/img/fields/{fieldData['name']}.png"),
            size=(fieldData['width'] * 23, fieldData['height'] * 23)
        )
        fieldLabel = ctk.CTkLabel(fieldContainer, image=fieldImage, text="")
        fieldLabel.pack(fill='both', expand=True)  # This makes the image fill the entire container

        print(f"Field width: {fieldData['width']}, height: {fieldData['height']}")
        print(f"Window geometry: {temp_window.winfo_width()}x{temp_window.winfo_height()}")

        for r in range(fieldData['height']):
            fieldContainer.grid_rowconfigure(r, minsize=23)
        for c in range(fieldData['width']):
            fieldContainer.grid_columnconfigure(c, minsize=23)

        for r in range(fieldData['height']):
            for c in range(fieldData['width']):
                cell = ctk.CTkButton(fieldContainer, fg_color='transparent', text="", width=23, height=23, corner_radius=0)
                cell.grid(row=r, column=c)
