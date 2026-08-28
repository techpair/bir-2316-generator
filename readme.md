# BIR Form 2316 PDF Generator

A standalone Python microservice designed to programmatically generate the official Philippine Bureau of Internal Revenue (BIR) Form 2316. 

Instead of relying on unstable PDF-to-Excel conversions or expensive third-party subscriptions, this tool uses precise X/Y coordinate mapping to overlay employee payroll data directly onto the official blank BIR PDF template.

> ⚠️ **IMPORTANT COMPLIANCE NOTE**  
> Tax regulations and official document layouts change periodically. **Always ensure you are using the most up-to-date version of BIR Form 2316**. 
> 
> You can verify and download the latest official PDF templates directly from the **[BIR Official Forms Website](https://www.bir.gov.ph/bir-forms)**.

## ✨ Features
* **Precision Stamping:** Uses `PyMuPDF` to write data at exact typographical points, completely independent of screen resolution.
* **Character Stepping & Chunking:** Intelligently handles government forms with segmented boxes (like TIN, RDO, and Zip Codes) by iterating through characters with custom spacing.
* **Decoupled Architecture:** Built as an independent tool, making it highly scalable and ready to be integrated into any main backend (e.g., Truds Payroll) as an imported package or API service.

## 🛠️ Prerequisites
* Python 3.10 or higher
* `PyMuPDF` library

## 🚀 Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/bir-2316-generator.git
cd bir-2316-generator


```markdown
## 🌐 Running as an API Microservice

This generator is wrapped in a lightweight FastAPI server, allowing it to run independently and accept data from any backend framework (Django, Flask, Node.js, Laravel) via HTTP POST requests.

### 1. Install API Dependencies
Ensure you have the API and server packages installed in your virtual environment:
```bash
pip install fastapi uvicorn pydantic

```

### 2. Start the Server

Run the API on a dedicated unprivileged port (e.g., `8231`). Binding to `127.0.0.1` ensures the service is only accessible internally by your main application server.

```bash
uvicorn api:app --host 127.0.0.1 --port 8231

```

### 3. API Contract

* **Endpoint:** `POST http://127.0.0.1:8231/generate-2316`
* **Content-Type:** `application/json`
* **Response:** Returns the generated `application/pdf` file directly as a downloadable stream.

**Example Request Payload:**

```json
{
  "employee_name": "Alvarez, Mateo S.",
  "gross_compensation": "80,000.00",
  "tin_part_1": "123",
  "tin_part_2": "456",
  "tin_part_3": "789",
  "tin_part_4": "0000"
}

```

### 4. Integration Example (Python/Requests)

Here is how your main backend application calls the microservice and downloads the PDF:

```python
import requests

url = "[http://127.0.0.1:8231/generate-2316](http://127.0.0.1:8231/generate-2316)"
payload = {
    "employee_name": "Alvarez, Mateo S.",
    "gross_compensation": "80,000.00",
    "tin_part_1": "123",
    "tin_part_2": "456",
    "tin_part_3": "789",
    "tin_part_4": "0000"
}

# Send the data to the generator
response = requests.post(url, json=payload)

# Save the returned PDF stream
if response.status_code == 200:
    with open("downloads/2316_Alvarez.pdf", "wb") as f:
        f.write(response.content)

```

```
```