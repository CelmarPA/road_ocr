import os
import re
from typing import Dict

import easyocr


class OCRManager:
    """
    Handles OCR processing, text extraction, parsing structured data,
    and image file renaming based on extracted information.
    """

    def __init__(self, language: list[str]) -> None:
        """
        Initialize the OCR engine.

        Args:
            language (list[str]): List of languages for EasyOCR (e.g. ["pt"]).
        """
        self.reader = easyocr.Reader(language)

    def extract_text(self, file: str) -> str:
        """
        Extract raw text from an image using OCR.

        Args:
            file (str): Path to the image file.

        Returns:
            str: Extracted text joined into a single string.
        """
        result = self.reader.readtext(file)
        return "\n".join(item[1] for item in result)

    @staticmethod
    def parse_data(full_text: str, file_name: str) -> Dict[str, str]:
        """
        Parse structured information from OCR text using regex.

        Args:
            full_text (str): Raw OCR extracted text.
            file_name (str): Original image file name.

        Returns:
            Dict[str, str]: Structured data extracted from text.
        """

        date_time = re.search(
            r'(\d{2}/\d{2}/\d{4})\s+(\d{2}[.:]\d{2})',
            full_text
        )

        coordinates = re.search(
            r'([\d,]+)\s*[Ss]\s+([\d,]+)\s*[Ww]',
            full_text
        )

        km_match = re.search(
            r'Km\s*([\d,]+)',
            full_text,
            re.IGNORECASE
        )

        side_match = re.search(
            r'(Leste|Oeste|Norte|Sul)',
            full_text,
            re.IGNORECASE
        )

        return {
            "date": date_time.group(1) if date_time else "",
            "time": date_time.group(2).replace(".", ":") if date_time else "",
            "s": coordinates.group(1) if coordinates else "",
            "w": coordinates.group(2) if coordinates else "",
            "km": km_match.group(1) if km_match else "",
            "side": side_match.group(1) if side_match else "",
            "new_name": file_name
        }

    @staticmethod
    def rename_image_file(file_path: str, data: Dict[str, str]) -> str:
        """
        Rename image file based on extracted KM value.

        Args:
            file_path (str): Original file path.
            data (Dict[str, str]): Parsed OCR data.

        Returns:
            str: New file name after renaming (or original if unchanged).
        """

        if not data.get("km"):
            return file_path

        clean_km = data["km"].replace(",", "_")
        directory = os.path.dirname(file_path)
        extension = os.path.splitext(file_path)[1]

        new_name = f"Km_{clean_km}{extension}"
        new_path = os.path.join(directory, new_name)

        count = 1
        while os.path.exists(new_path):
            new_name = f"Km_{clean_km}_{count}{extension}"
            new_path = os.path.join(directory, new_name)
            count += 1

        os.rename(file_path, new_path)

        return new_path

    def get_data(self, file: str) -> Dict[str, str]:
        """
        Full OCR pipeline:
        extract text → parse data → rename image → return structured data.

        Args:
            file (str): Path to image file.

        Returns:
            Dict[str, str]: Extracted and processed data.
        """

        full_text = self.extract_text(file)
        data = self.parse_data(full_text, file)

        new_name = self.rename_image_file(file, data)

        data["new_name"] = os.path.basename(new_name)

        return data
