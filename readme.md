```markdown
# BIR Form 2316 PDF Generator

A standalone Python microservice designed to programmatically generate the official Philippine Bureau of Internal Revenue (BIR) Form 2316. 

Instead of relying on unstable PDF-to-Excel conversions or expensive third-party subscriptions, this tool uses precise X/Y coordinate mapping to overlay employee payroll data directly onto the official blank BIR PDF template.

> ⚠️ **IMPORTANT COMPLIANCE NOTE**  
> Tax regulations and official document layouts change periodically. **always ensure you are using the most up-to-date version of BIR Form 2316**. 
> 
> You can verify and download the latest official PDF templates directly from the **[BIR Official Forms Website](https://www.bir.gov.ph/index.php/bir-forms/certificates.html)**.

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
   git clone [https://github.com/your-username/bir-2316-generator.git](https://github.com/your-username/bir-2316-generator.git)
   cd bir-2316-generator

```

2. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install PyMuPDF

```


4. **Add the Template:**
Download the latest BIR Form 2316 from the [BIR website](https://www.google.com/url?sa=E&source=gmail&q=https://www.bir.gov.ph/index.php/bir-forms/certificates.html) and place the PDF at `templates/2316_template.pdf`.

## 💻 Usage

To test the generator or calibrate coordinates, run the test script:

```bash
python test_run.py

```

This will read the dummy payload, stamp the text onto the template, and output a new file named `2316_test_output.pdf` in the root directory.

## 📁 Project Structure

```text
bir-2316-generator/
├── templates/
│   └── 2316_template.pdf    # The blank official BIR form
├── coordinates.py           # Configuration file for all X/Y points
├── generator.py             # The core PyMuPDF engine
├── test_run.py              # Local testing and calibration script
└── README.md

```

## 📐 How to Calibrate Coordinates (`coordinates.py`)

The PDF engine uses a typographical point system where **(0,0) is the top-left corner** of the page.

* Increasing **X** moves the text to the **RIGHT**.
* Increasing **Y** moves the text **DOWN**.

### Standard Fields

For standard continuous text (like Names or Amounts), provide the starting `X` and `Y` coordinates:

```python
"gross_compensation": {"coords": (485, 168)}

```

### Segmented/Spaced Fields (TIN, Zip Code, Dates)

For fields that require one digit per box, provide the starting coordinate and a `spacing` value (the distance in points between each character). The engine will automatically step through the string and place each character in its respective box:

```python
"tin_part_1": {"coords": (90, 141), "spacing": 14.5}

```

## 🔗 Future Integration

This tool is designed to be imported into a primary backend (like Django, FastAPI, or Flask). The main application will aggregate the employee's yearly payroll totals into a JSON dictionary and pass it directly to the `generate_2316(data_payload, template_path, output_path)` function.
