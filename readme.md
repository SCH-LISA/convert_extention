## TRC to TXT Converter

## Introduction
TRC to TXT Converter is a Python-based graphical user interface (GUI) application that reads a `.trc` file containing CAN communication data and converts it to the `.txt` file format. The application automatically starts the conversion process when the user selects a `.trc` file and provides a progress bar that displays the progress of the conversion.

## Functions.
- File selection: Allows the user to browse and select `.trc` files on the system.
- Auto-convert: Automatically starts the conversion to `.txt` format when a file is selected.
- Progress display: A progress bar is provided to show the progress in real-time during the file conversion process.
- Error management: Notifies the user of any errors that may occur during the conversion.
- Duplicate file management: Allows the user to decide whether to overwrite files for output filenames that already exist.

## Installation requirements
This application requires Python version 3.x, and the following Python libraries must be installed:
- `tkinter`
- `customtkinter`
- `pandas`

## How to install
1. install Python (https://www.python.org/downloads/)
2. install the required Python libraries:
   ```bash
   pip install customtkinter pandas

## How to use it
To start the application, run the following command in the source code directory:
```bash
python converter_app.py
```
1. Click the 'Select TRC File' button to select the .trc file to convert.
2. You can see the conversion process in the progress bar.
3. When the conversion is complete, the resulting file will be saved in .txt format in the same directory.