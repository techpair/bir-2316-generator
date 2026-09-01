# Note: In PyMuPDF, (0,0) is the TOP-LEFT corner of the page.

# Format: "field_name": {"coords": (x, y), "spacing": optional_x_offset_per_character}

# Moving X left = smaller number. Moving Y down = larger number.

FIELDS = {
    # --- HEADER: PERIOD ---
    "period_from": {"coords": (325, 75), "spacing": 14.5},
    "period_to": {"coords": (405, 75), "spacing": 14.5},

    # --- PART I: EMPLOYEE INFORMATION ---
    "tin_part_1": {"coords": (88, 138), "spacing": 14.5},  
    "tin_part_2": {"coords": (136, 138), "spacing": 14.5}, 
    "tin_part_3": {"coords": (188, 138), "spacing": 14.5}, 
    "tin_part_4": {"coords": (240, 138), "spacing": 14.5}, 
    "employee_name": {"coords": (45, 164)}, 
    "registered_address": {"coords": (45, 192)},
    "local_home_address": {"coords": (45, 218)},
    "date_of_birth": {"coords": (88, 275), "spacing": 14.5},
    "contact_number": {"coords": (220, 275), "spacing": 14.5},

    # --- PART II: EMPLOYER INFORMATION ---
    "employer_name": {"coords": (45, 360)},
    "employer_address": {"coords": (45, 385)},
    "employer_zip": {"coords": (420, 385), "spacing": 14.5},

    # --- PART IV: FINANCIAL DETAILS ---
    # Right Column (Amounts align at X: 485)
    "gross_compensation": {"coords": (485, 164)}, 
    "total_contributions": {"coords": (485, 298)}, # Box 36
    "non_taxable_compensation": {"coords": (485, 335)}, # Box 38
    "taxable_compensation": {"coords": (485, 680)}, # Box 52
    
    # Left Column (Amounts align at X: 230)
    "tax_withheld": {"coords": (230, 715)} # Box 28
}