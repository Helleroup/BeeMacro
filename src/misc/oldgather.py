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

            fieldDropdown = ctk.CTkOptionMenu(taskContainer, values=self.fields, command=lambda value, rowid=data['rowid']: self.editTask(rowid=rowid, field=value))
            fieldDropdown.set(field)  # Set to current field
            fieldDropdown.pack(side='left', padx=8, pady=8)

            patternButton = ctk.CTkButton(taskContainer, border_width=1, fg_color='transparent', border_color='red', text_color='red', text='pattern', command=lambda field=field: self.savePatternAsImage(field))
            patternButton.pack(side='left', padx=8, pady=8)

            deleteButton = ctk.CTkButton(taskContainer, text='❌', font=("Arial", 32), width=104, height=104, command=lambda rowid=data['rowid']: self.removeTask(rowid))
            deleteButton.pack(anchor="e", padx=8, pady=8)

            self.addNewTaskButton.pack_forget()
            taskContainer.pack(pady=15, padx=15, fill='x')
            self.addNewTaskButton.pack(pady=15, padx=15, fill='x')

            print(f'added {index} for field {field}')

    def addTask(self, field='Sunflower', pattern=None,  shiftLock=False):

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

        icon_image = Image.open(f"./src/app/img/fields/{fieldData['name']}.png")
        icon_image = icon_image.resize((32, 32))  # Resize if needed
        icon_photo = ImageTk.PhotoImage(icon_image)
        temp_window.iconphoto(False, icon_photo)

        temp_window.geometry(f"{fieldData['width'] * 23}x{(fieldData['height'] * 23) + 50}")
        temp_window.grab_set()
        temp_window.resizable(False, False)

        fieldContainer = ctk.CTkFrame(temp_window, fg_color="#6A7F96", width=fieldData['width'] * 23, height=fieldData['height'] * 23, corner_radius=0)
        print(f"Field width: {fieldData['width']}, height: {fieldData['height']}")
        print(f"Window geometry: {temp_window.winfo_width()}x{temp_window.winfo_height()}")
        fieldContainer.pack(fill='both', expand=False)

        flowerString = fieldData['flower_ratio']

        flowers = []
        ratios = []

        flowerRatios = flowerString.split(',')
        for flowerRatio in flowerRatios:
            flower, ratio = flowerRatio.split(':')
            flowers.append(flower)
            ratios.append(float(ratio))

        for r in range(fieldData['height']):
            fieldContainer.grid_rowconfigure(r, minsize=23)
        for c in range(fieldData['width']):
            fieldContainer.grid_columnconfigure(c, minsize=23)

        for r in range(fieldData['height']):
            for c in range(fieldData['width']):
                randomFlower = random.choices(flowers, weights=ratios, k=1)[0]
                cellIcon = ctk.CTkImage(Image.open(f"./src/app/img/flowers/{randomFlower}.png"))
                cell = ctk.CTkLabel(fieldContainer, text="", width=23, height=23, corner_radius=0, image=cellIcon)
                cell.grid(row=r, column=c)





    #save pattern to use for later
    def savePatternAsImage(self, field, output_path="output.png"):
        print(field)
        fieldData = None
        for index, data in self.fieldTable.items():
            if data['display_name'] == field:
                fieldData = data
                break

        if not fieldData:
            raise ValueError(f"Field '{field}' not found.")

    # Load flower types and ratios
        flowerString = fieldData['flower_ratio']
        flowers = []
        ratios = []

        flowerRatios = flowerString.split(',')
        for flowerRatio in flowerRatios:
            flower, ratio = flowerRatio.split(':')
            flowers.append(flower)
            ratios.append(float(ratio))

        cell_size = 23
        width_px = fieldData['width'] * cell_size
        height_px = fieldData['height'] * cell_size

    # Create a blank image
        output_image = Image.new("RGBA", (width_px, height_px), (255, 255, 255, 0))

        for r in range(fieldData['height']):
            for c in range(fieldData['width']):
                randomFlower = random.choices(flowers, weights=ratios, k=1)[0]
                flower_img = Image.open(f"./src/app/img/flowers/{randomFlower}.png").convert("RGBA").resize((cell_size, cell_size))
                output_image.paste(flower_img, (c * cell_size, r * cell_size), flower_img)


    # Save the final image
        output_image.save(output_path)
        print(f"Pattern saved as {output_path}")
