# BIR Form 2316 PDF Generator

This project generates a filled BIR Form 2316 PDF by placing text at exact coordinate positions on the official template using PyMuPDF. It is designed as a lightweight, backend-friendly generator that can be used directly from Python or exposed through a FastAPI endpoint.

> ⚠️ Compliance note: BIR form layouts and tax requirements can change over time. Always confirm that you are using the latest official BIR Form 2316 template before production use.

## Features

- Precise PDF stamping using X/Y coordinates
- Support for segmented fields such as TIN and ZIP code fields
- Simple Python API for local generation
- FastAPI endpoint for remote integration
- Automatic cleanup of generated temporary files after download

## Project structure

- generator.py: main PDF rendering logic
- api.py: FastAPI service and HTTP contract
- coordinates.py: field coordinates and per-character spacing rules
- test_run.py: sample script that generates a test PDF
- templates/2316_template.pdf: blank template used for stamping

## Requirements

- Python 3.10+
- PyMuPDF
- FastAPI
- Uvicorn
- Pydantic

Install dependencies:

```bash
pip install pymupdf fastapi uvicorn pydantic
```

## Quick start

### 1. Generate a local PDF using the sample script

```bash
python test_run.py
```

This creates a file named 2316_test_output.pdf in the project root using the sample payload in test_run.py.

### 2. Start the API

```bash
uvicorn api:app --host 127.0.0.1 --port 8231
```

The service exposes:

```http
POST http://127.0.0.1:8231/generate-2316
```

## API contract

The request body is a JSON object matching the PayrollData model in api.py.

### Accepted fields

- tin: single TIN string such as 123-456-789-0000
- employee_name
- registered_address
- local_home_address
- date_of_birth
- contact_number
- employer_name
- employer_address
- employer_zip
- gross_compensation
- taxable_compensation
- non_taxable_compensation
- total_contributions
- tax_withheld
- period_from
- period_to

The code normalizes the TIN internally by removing spaces and hyphens, then splits it into four numbered chunks required by the template mapping.

### Example request

```json
{
  "tin": "123-456-789-0000",
  "employee_name": "DOE, JANE M.",
  "registered_address": "123 GENERIC BLVD., SAMPLE CITY",
  "local_home_address": "SAME AS ABOVE",
  "date_of_birth": "01011990",
  "contact_number": "09990000000",
  "employer_name": "SAMPLE COMPANY INC.",
  "employer_address": "456 BUSINESS DIST., METRO CITY",
  "employer_zip": "1000",
  "gross_compensation": "250,000.00",
  "taxable_compensation": "209,600.00",
  "non_taxable_compensation": "25,000.00",
  "total_contributions": "15,400.00",
  "tax_withheld": "12,500.00",
  "period_from": "0101",
  "period_to": "1231"
}
```

### Example client call

```python
import requests

response = requests.post(
    "http://127.0.0.1:8231/generate-2316",
    json={
        "tin": "123-456-789-0000",
        "employee_name": "DOE, JANE M.",
        "registered_address": "123 GENERIC BLVD., SAMPLE CITY",
        "local_home_address": "SAME AS ABOVE",
        "date_of_birth": "01011990",
        "contact_number": "09990000000",
        "employer_name": "SAMPLE COMPANY INC.",
        "employer_address": "456 BUSINESS DIST., METRO CITY",
        "employer_zip": "1000",
        "gross_compensation": "250,000.00",
        "taxable_compensation": "209,600.00",
        "non_taxable_compensation": "25,000.00",
        "total_contributions": "15,400.00",
        "tax_withheld": "12,500.00",
        "period_from": "0101",
        "period_to": "1231",
    }
)

if response.status_code == 200:
    with open("2316_output.pdf", "wb") as f:
        f.write(response.content)
```

## Direct Python usage

You can also call the generator directly from Python:

```python
from generator import generate_2316

payload = {
    "period_from": "0101",
    "period_to": "1231",
    "tin": "111-222-333-4444",
    "employee_name": "DOE, JANE M.",
    "registered_address": "123 GENERIC BLVD., SAMPLE CITY",
    "local_home_address": "SAME AS ABOVE",
    "date_of_birth": "01011990",
    "contact_number": "09990000000",
    "employer_name": "SAMPLE COMPANY INC.",
    "employer_address": "456 BUSINESS DIST., METRO CITY",
    "employer_zip": "1000",
    "gross_compensation": "250,000.00",
    "total_contributions": "15,400.00",
    "non_taxable_compensation": "25,000.00",
    "taxable_compensation": "209,600.00",
    "tax_withheld": "12,500.00",
}

generate_2316(payload, "templates/2316_template.pdf", "2316_output.pdf")
```

## Notes

- The generator uses the top-left corner of the PDF page as the origin for coordinates.
- Fields with segmented data use custom spacing values defined in coordinates.py.
- The API returns the generated PDF as a downloadable file and removes the temporary output file after the response is sent.

## Important

This project stamps data onto a PDF template; it does not validate tax rules or generate legal tax advice. For production use, keep the template up to date and verify field placement against the current BIR form layout.

```