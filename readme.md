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
