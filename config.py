from typing import Tuple, List


"""
Application configuration file.

This module centralizes all constants used across the OCR pipeline,
including OCR language settings, supported image extensions, and
output Excel file path.
"""

# OCR language configuration (EasyOCR format)
LANGUAGE: List[str] = ["pt"]

# Supported image file extensions
EXTENSIONS: Tuple[str, ...] = (".jpg", ".jpeg", ".png")

# Output Excel file name
EXCEL_FILE: str = "report.xlsx"
