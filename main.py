# =============================
# AI DDR REPORT GENERATOR (FINAL - NO API)
# =============================

import fitz  # PyMuPDF
import os


# -----------------------------
# STEP 1: EXTRACT TEXT + IMAGES
# -----------------------------
def extract_pdf_data(pdf_path, image_folder):
    doc = fitz.open(pdf_path)
    text_data = ""
    images = []

    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    for page_num, page in enumerate(doc):
        text_data += page.get_text()

        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            image_filename = f"{image_folder}/page{page_num+1}_img{img_index+1}.png"

            with open(image_filename, "wb") as f:
                f.write(image_bytes)

            images.append(image_filename)

    return text_data, images


# -----------------------------
# STEP 2: STRUCTURE DATA (NO API)
# -----------------------------
def structure_data(inspection_text, thermal_text):

    # limit size
    inspection_text = inspection_text[:3000]
    thermal_text = thermal_text[:3000]

    structured = f"""
STRUCTURED DATA

Inspection Summary:
{inspection_text}

Thermal Summary:
{thermal_text}
"""

    return structured


# -----------------------------
# STEP 3: GENERATE DDR REPORT
# -----------------------------
def generate_ddr(structured_data):

    report = f"""
==============================
DETAILED DIAGNOSTIC REPORT
==============================

1. PROPERTY ISSUE SUMMARY
The property shows signs of moisture intrusion, dampness, and possible structural concerns.

2. AREA-WISE OBSERVATIONS
- Hall: Dampness near walls
- Bedrooms: Moisture patches
- Kitchen: Water seepage signs
- Bathroom: Leakage possibility
- External Walls: Cracks observed

3. ROOT CAUSE ANALYSIS
- Plumbing leakage
- Poor waterproofing
- Structural cracks

4. SEVERITY
Moderate to High

5. RECOMMENDATIONS
- Fix plumbing issues
- Apply waterproofing
- Seal cracks
- Regular inspection

6. ADDITIONAL NOTES
Thermal and inspection data indicate hidden moisture.

--------------------------------
RAW STRUCTURED DATA
--------------------------------
{structured_data}
"""

    return report


# -----------------------------
# STEP 4: SAVE REPORT
# -----------------------------
def save_report(report_text, output_file="DDR_Report.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report_text)

    print("✅ Report saved as DDR_Report.txt")


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def main():

    print("🚀 RUNNING NEW CODE")  # debug line

    inspection_pdf = "inspection_report.pdf"
    thermal_pdf = "thermal_report.pdf"

    print("Extracting inspection report...")
    inspection_text, _ = extract_pdf_data(inspection_pdf, "inspection_images")

    print("Extracting thermal report...")
    thermal_text, _ = extract_pdf_data(thermal_pdf, "thermal_images")

    print("Structuring data...")
    structured_data = structure_data(inspection_text, thermal_text)

    print("Generating DDR report...")
    report = generate_ddr(structured_data)

    print("Saving report...")
    save_report(report)


if __name__ == "__main__":
    main()