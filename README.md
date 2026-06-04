# 🚧 RoadOCR

RoadOCR is a Python-based desktop application that automates text extraction from road inspection images using Optical Character Recognition (OCR). It processes images in bulk, extracts structured metadata, renames files based on extracted information, and exports results into an Excel spreadsheet.

---

## 🚀 Features

- OCR text extraction using EasyOCR  
- Automatic parsing of structured data:
  - Date
  - Time
  - Coordinates (S / W)
  - Kilometer marker (Km)
  - Road side (North, South, East, West)
- Automatic image renaming based on KM value
- Excel report generation (.xlsx)
- Graphical folder selection (Tkinter file dialog)
- Duplicate-safe file renaming system
- Console-based execution with real-time logs

---

## 🧠 How It Works

1. User selects a folder containing images  
2. Each image is processed using OCR  
3. Text is extracted and parsed using regex patterns  
4. Metadata is structured into fields  
5. Images are renamed based on KM value  
6. Data is saved into Excel spreadsheet (relatorio.xlsx)

---

## 📂 Project Structure

RoadOCR/
├── main.py
├── ocr_manager.py
├── sheet_manager.py
├── config.py
├── assets/
│   └── icon.ico
├── relatorio.xlsx
└── dist/
    └── RoadOCR.exe

---

## ⚙️ Installation (Development)

git clone https://github.com/CelmarPA/road_ocr.git
cd RoadOCR
python -m venv venv
venv\Scripts\activate
pip install easyocr openpyxl pyinstaller

---

## ▶️ Run

python main.py

---

## 🏗️ Build Executable

pyinstaller --onefile --name RoadOCR --console --icon=assets/icon.ico main.py

Output:
dist/RoadOCR.exe

---

## 📊 Output

| Date | Time | S | W | Km | Side | Photo |

---

## 👨‍💻 Author

https://github.com/CelmarPA
