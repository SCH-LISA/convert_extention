import tkinter as tk
import customtkinter as ctk
import pandas as pd
import os
from tkinter import filedialog, messagebox, PhotoImage

def convert_trc_to_txt(input_file, output_file, update_progress):
    skip_rows = 0
    with open(input_file, 'r') as file:
        for line in file:
            if line.strip().startswith(';'):
                skip_rows += 1
            elif line.strip() == '':
                skip_rows += 1
            else:
                break

    data = pd.read_csv(input_file, skiprows=skip_rows, delimiter=r"\s+", names=[
        "No", "Time_Offset", "Type", "ID", "Data_Length", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Label"
    ])

    data.fillna(-1, inplace=True)
    total_rows = len(data)
    data.to_csv(output_file, index=False, sep=' ')

    update_frequency = max(1, total_rows // 100)
    
    for index in range(total_rows):
        if index % update_frequency == 0:
            update_progress((index + 1) / total_rows * 100)

    update_progress(100)
    return True, total_rows

class ConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("system")

        self.title("TRC to TXT Converter")
        self.geometry("600x300")

        logo_image = PhotoImage(file="assets/lisa_logo.png")
        self.iconphoto(False, logo_image)

        self.label = ctk.CTkLabel(self, text="Select a TRC file and convert it to TXT", font=("Roboto", 20))
        self.label.pack(pady=12)

        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(pady=20, padx=20)
        self.progress.set(0)

        self.convert_button = ctk.CTkButton(self, text="Select TRC File", command=self.convert)
        self.convert_button.pack(pady=15)

        self.close_button = ctk.CTkButton(self, text="Close", command=self.destroy)
        self.close_button.pack(pady=15)

    def update_progress_bar(self, value):
        self.progress.set(value)

    def convert(self):
        input_file = filedialog.askopenfilename(filetypes=[("TRC files", "*.trc")])
        if input_file:
            directory, filename = os.path.split(input_file)
            name, ext = os.path.splitext(filename)
            output_file = os.path.join(directory, f"{name}-converted.txt")
            if os.path.exists(output_file):
                response = messagebox.askyesno("Confirm Overwrite", "Output file exists. Overwrite?")
                if response:
                    success, total_rows = convert_trc_to_txt(input_file, output_file, self.update_progress_bar)
                    if success:
                        messagebox.showinfo("Success", f"File has been converted successfully!\nTotal lines processed: {total_rows}")
                    else:
                        messagebox.showerror("Error", "Failed to convert the file.")
            else:
                success, total_rows = convert_trc_to_txt(input_file, output_file, self.update_progress_bar)
                if success:
                    messagebox.showinfo("Success", f"File has been converted successfully!\nTotal lines processed: {total_rows}")
                else:
                    messagebox.showerror("Error", "Failed to convert the file.")

if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()
