from generator import generate_2316
import os

def main():
    # Define paths
    template_path = os.path.join("templates", "2316_template.pdf")
    output_path = "2316_test_output.pdf"

    # Dummy data from your "backend"
    dummy_data = {
        "employee_name": "Alvarez, Mateo S.",
        "tin_part_1": "123",
        "gross_compensation": "80,000.00"
    }

    # Run the generator
    generate_2316(dummy_data, template_path, output_path)

if __name__ == "__main__":
    main()