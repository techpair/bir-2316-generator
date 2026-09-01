import os
from generator import generate_2316  # Make sure this matches your actual import

def main():
    template_path = os.path.join("templates", "2316_template.pdf")
    output_path = "2316_test_output.pdf"

    test_payload = {
        "period_from": "0101",
        "period_to": "1231",
        "tin_part_1": "123",
        "tin_part_2": "456",
        "tin_part_3": "789",
        "tin_part_4": "0000",
        "employee_name": "CLONE-ACUÑA, EMILIA",
        "registered_address": "123 TEST STREET, BRGY. NCR",
        "local_home_address": "SAME AS ABOVE",
        "date_of_birth": "05151990",
        "contact_number": "09171234567",
        "employer_name": "PMCFOODPARKS BY RAINTREE INC",
        "employer_address": "6F SALUSTIANA TY TOWER MAKATI CITY",
        "employer_zip": "1200",
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