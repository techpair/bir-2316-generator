import os
from generator import generate_2316

def main():
    template_path = os.path.join("templates", "2316_template.pdf")
    output_path = "2316_test_output.pdf"

    test_payload = {
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
        "tax_withheld": "12,500.00"
    }

    generate_2316(test_payload, template_path, output_path)
    print(f"Test PDF successfully generated at: {output_path}")

if __name__ == "__main__":
    main()