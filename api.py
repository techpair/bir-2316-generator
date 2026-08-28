from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import FileResponse
from pydantic import BaseModel
from generator import generate_2316
import os

app = FastAPI()

# Define the expected incoming data structure
class PayrollData(BaseModel):
    employee_name: str
    gross_compensation: str
    tin_part_1: str
    tin_part_2: str
    tin_part_3: str
    tin_part_4: str
    # Add other fields as you map them

def cleanup_file(path: str):
    """Deletes the PDF after it is sent to save server space."""
    if os.path.exists(path):
        os.remove(path)

@app.post("/generate-2316")
def create_pdf(data: PayrollData, background_tasks: BackgroundTasks):
    # Create a unique filename
    output_path = f"2316_{data.employee_name.replace(' ', '_')}.pdf"
    template_path = os.path.join("templates", "2316_template.pdf")
    
    # Run your existing generator
    generate_2316(data.dict(), template_path, output_path)
    
    # Schedule cleanup to run immediately after the file is downloaded
    background_tasks.add_task(cleanup_file, output_path)
    
    # Return the PDF file directly to the requesting system
    return FileResponse(
        output_path, 
        media_type="application/pdf", 
        filename=output_path
    )   