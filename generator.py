import fitz  # PyMuPDF
from coordinates import FIELDS

def generate_2316(data_payload, template_path, output_path):
    # 1. Open the blank BIR 2316 template
    doc = fitz.open(template_path)
    page = doc[0] # The 2316 is usually a single page

    # 2. Loop through the incoming data and stamp it onto the PDF
    for field_key, text_value in data_payload.items():
        if field_key in FIELDS:
            x, y = FIELDS[field_key]
            
            # Stamp the text at the specific coordinates
            page.insert_text(
                point=fitz.Point(x, y),
                text=str(text_value),
                fontsize=9,
                fontname="helv", # Standard Helvetica
                color=(0, 0, 0)  # Black text
            )

    # 3. Save the newly filled PDF
    doc.save(output_path)
    doc.close()
    print(f"Successfully generated: {output_path}")