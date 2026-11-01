from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import FileResponse
from pydantic import BaseModel
from generator import generate_2316
import os

app = FastAPI()

# Define the expected incoming data structure
class PayrollData(BaseModel):
    # Part I
    tin: str = ""  # Replaced the 4 parts with a single TIN field
    tin_part_1: str = ""
    tin_part_2: str = ""
    tin_part_3: str = ""
    tin_part_4: str = ""
    employee_name: str = ""
    registered_address: str = ""
    local_home_address: str = ""
    date_of_birth: str = ""
    contact_number: str = ""
    
    # Part II
    employer_name: str = ""
    employer_address: str = ""
    employer_zip: str = ""
    
    # Financials
    gross_compensation: str = ""
    taxable_compensation: str = ""
    non_taxable_compensation: str = ""
    total_contributions: str = ""
    tax_withheld: str = ""
    
    # Headers
    period_from: str = ""
    period_to: str = ""

def cleanup_file(path: str):
    """Deletes the PDF after it is sent to save server space."""
    if os.path.exists(path):
        os.remove(path)

@app.post("/generate-2316")
def create_pdf(data: PayrollData, background_tasks: BackgroundTasks):
    # Convert payload to a mutable dictionary
    payload = data.dict()
    
    # Normalize and split only a supplied single-string TIN.
    raw_tin = payload.pop("tin", "")
    if raw_tin:
        raw_tin = raw_tin.replace("-", "").replace(" ", "")
        payload["tin_part_1"] = raw_tin[0:3]
        payload["tin_part_2"] = raw_tin[3:6]
        payload["tin_part_3"] = raw_tin[6:9]
        payload["tin_part_4"] = raw_tin[9:]

    # Create a unique filename
    safe_name = payload["employee_name"].replace(" ", "_").replace(",", "")
    output_path = f"2316_{safe_name}_{os.urandom(16).hex()}.pdf"
    template_path = os.path.join("templates", "2316_template.pdf")
    
    # Run the generator with the modified payload
    generate_2316(payload, template_path, output_path)
    
    # Schedule cleanup to run immediately after the file is downloaded
    background_tasks.add_task(cleanup_file, output_path)
    
    # Return the PDF file directly to the requesting system
    return FileResponse(
        output_path, 
        media_type="application/pdf", 
        filename=output_path
    )