from generator import generate_2316
import os

def main():
    template_path = os.path.join("templates", "2316_template.pdf")
    output_path = "2316_test_output.pdf"

    # Split the TIN into its components (you will do this programmatically later in the backend)
    full_tin = "123-456-789-0000"
    tin_parts = full_tin.split("-")

    dummy_data = {
        "employee_name": "Alvarez, Mateo S.",
        "gross_compensation": "80,000.00",
        
        # Map the TIN chunks
        "tin_part_1": tin_parts[0] if len(tin_parts) > 0 else "",
        "tin_part_2": tin_parts[1] if len(tin_parts) > 1 else "",
        "tin_part_3": tin_parts[2] if len(tin_parts) > 2 else "",
        "tin_part_4": tin_parts[3] if len(tin_parts) > 3 else ""
    }

    generate_2316(dummy_data, template_path, output_path)

if __name__ == "__main__":
    main()