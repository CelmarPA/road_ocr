import os
import tkinter as tk
from tkinter import filedialog

from config import EXTENSIONS, LANGUAGE, EXCEL_FILE
from sheet_manager import SpreadsheetManager
from ocr_manager import OCRManager


def get_directory() -> str:
    """
    Open a graphical file dialog for the user to select a directory.

    Returns:
        str: Path to the selected directory. Returns an empty string if canceled.
    """

    root = tk.Tk()
    root.withdraw()  # Hide main Tkinter window

    directory = filedialog.askdirectory(
        title="Select the image folder"
    )

    return directory


def main() -> None:
    """
    Main execution pipeline:

    - Opens a folder selection dialog
    - Iterates through image files
    - Runs OCR processing
    - Saves extracted data into Excel spreadsheet
    """

    directory = get_directory()

    if not directory:
        print("No directory selected.")
        return

    ocr = OCRManager(LANGUAGE)
    sheet_manager = SpreadsheetManager(EXCEL_FILE)

    for file in os.listdir(directory):

        if not file.lower().endswith(EXTENSIONS):
            continue

        full_path = os.path.join(directory, file)

        print(f"Processing {file}...")

        data = ocr.get_data(full_path)

        if data:
            sheet_manager.update(data)


if __name__ == "__main__":
    print("Starting OCR pipeline...")
    main()
