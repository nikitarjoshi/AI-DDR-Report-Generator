# 🏠 AI DDR Report Generator

## 📌 Overview

This project generates a structured **Detailed Defect Report (DDR)** by analyzing:

* Inspection Reports
* Thermal Reports

It uses AI to combine both reports and produce a clean, professional report.

---

## ⚙️ Features

* Extracts data from PDF reports
* Combines multiple report types
* Generates structured DDR report
* Saves output in TXT and PDF formats

---

## 🛠️ Tech Stack

* Python
* PyMuPDF (for PDF extraction)
* python-docx (for Word file generation)
* Google Generative AI

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the project:

```bash
python main.py
```

---

## 📂 Project Structure

```
AI-DDR-Report-Generator/
│
├── main.py
├── DDR_Report.txt
├── DDR_Report.pdf
├── requirements.txt
├── README.md
```

---

## 📄 Output

* DDR_Report.txt
* DDR_Report.pdf

---

## 🎥 Demo Video

(Add your Loom video link here)

---

## ⚠️ Limitations

* Does not extract images from reports
* Depends on API quota availability
* Accuracy depends on input report quality

---

## 🚀 Future Improvements

* Add image extraction
* Improve report formatting
* Add web-based interface

---

## 💡 Note

This project demonstrates real-world AI-based report structuring using multi-source data.
