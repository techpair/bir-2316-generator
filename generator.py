import fitz  # PyMuPDF
from coordinates import FIELDS

def generate_2316(data_payload, template_path, output_path):
    doc = fitz.open(template_path)
    page = doc[0] 

    # Intercept and split the TIN natively inside the generator
    if "tin" in data_payload:
        raw_tin = data_payload.pop("tin").replace("-", "").replace(" ", "")
        data_payload["tin_part_1"] = raw_tin[0:3]
        data_payload["tin_part_2"] = raw_tin[3:6]
        data_payload["tin_part_3"] = raw_tin[6:9]
        data_payload["tin_part_4"] = raw_tin[9:]

    for field_key, text_value in data_payload.items():
        if field_key in FIELDS:
            config = FIELDS[field_key]
            start_x, y = config["coords"]
            
            # If the field has a "spacing" rule (like TIN or Zip Code)
            if "spacing" in config:
                current_x = start_x
                for char in str(text_value):
                    page.insert_text(
                        point=fitz.Point(current_x, y),
                        text=char,
                        fontsize=10, 
                        fontname="helv", 
                        color=(0, 0, 0)
                    )
                    current_x += config["spacing"]
            
            # Normal continuous text
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