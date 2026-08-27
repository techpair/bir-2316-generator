import fitz  # PyMuPDF
from coordinates import FIELDS

def generate_2316(data_payload, template_path, output_path):
    doc = fitz.open(template_path)
    page = doc[0] 

    for field_key, text_value in data_payload.items():
        if field_key in FIELDS:
            config = FIELDS[field_key]
            start_x, y = config["coords"]
            
            # If the field has a "spacing" rule (like TIN or Zip Code)
            if "spacing" in config:
                current_x = start_x
                # Loop through each digit and stamp it individually
                for char in str(text_value):
                    page.insert_text(
                        point=fitz.Point(current_x, y),
                        text=char,
                        fontsize=10, # Slightly larger for boxes
                        fontname="helv", 
                        color=(0, 0, 0)
                    )
                    current_x += config["spacing"] # Move X right for the next box
            
            # Normal continuous text (like Names and Amounts)
            else:
                page.insert_text(
                    point=fitz.Point(start_x, y),
                    text=str(text_value),
                    fontsize=9,
                    fontname="helv",
                    color=(0, 0, 0)
                )

    doc.save(output_path)
    doc.close()
    print(f"Successfully generated: {output_path}")