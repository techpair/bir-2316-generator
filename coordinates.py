# Note: In PyMuPDF, (0,0) is the TOP-LEFT corner of the page.

# Format: "field_name": {"coords": (x, y), "spacing": optional_x_offset_per_character}

# Moving X left = smaller number. Moving Y down = larger number.

# Note: In PyMuPDF, (0,0) is the TOP-LEFT corner of the page.
# Format: "field_name": {"coords": (x, y), "spacing": optional_x_offset_per_character}

FIELDS = {
    # --- HEADER: PERIOD ---
    "period_from": {"coords": (390  , 107), "spacing": 16.5},
    "period_to": {"coords": (515, 107), "spacing": 16.5},

    # --- PART I: EMPLOYEE INFORMATION ---
    "tin_part_1": {"coords": (88, 138), "spacing": 14.5},  
    "tin_part_2": {"coords": (136, 138), "spacing": 14.5}, 
    "tin_part_3": {"coords": (188, 138), "spacing": 14.5}, 
    "tin_part_4": {"coords": (240, 138), "spacing": 14.5}, 
    "employee_name": {"coords": (45, 158)}, 
    "registered_address": {"coords": (45, 186)},
    "local_home_address": {"coords": (45, 212)},
    
    "date_of_birth": {"coords": (46, 262), "spacing": 13.5},
    "contact_number": {"coords": (167, 262), "spacing": 13.5},

    # --- PART II: EMPLOYER INFORMATION ---
    "employer_name": {"coords": (45, 376)},
    "employer_address": {"coords": (45, 400)},
    "employer_zip": {"coords": (265, 400), "spacing": 12},

    # --- PART IV: FINANCIAL DETAILS ---
    "gross_compensation": {"coords": (485, 155)}, 
    "total_contributions": {"coords": (485, 292)}, 
    "non_taxable_compensation": {"coords": (485, 330)}, 
    "taxable_compensation": {"coords": (485, 675)}, 
    "tax_withheld": {"coords": (230, 723)} 
}