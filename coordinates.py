# Note: In PyMuPDF, (0,0) is the TOP-LEFT corner of the page.

# Format: "field_name": {"coords": (x, y), "spacing": optional_x_offset_per_character}

# Moving X left = smaller number. Moving Y down = larger number.

FIELDS = {
    # -----------------------------------------------------------
    # HEADER: PERIOD
    # -----------------------------------------------------------
    # Top right corner. Spaced for MM DD boxes.
    "period_from": {"coords": (260, 105), "spacing": 14.5},
    "period_to": {"coords": (360, 105), "spacing": 14.5},

    # -----------------------------------------------------------
    # PART I: EMPLOYEE INFORMATION
    # -----------------------------------------------------------
    "tin_part_1": {"coords": (88, 138), "spacing": 14.5},  
    "tin_part_2": {"coords": (136, 138), "spacing": 14.5}, 
    "tin_part_3": {"coords": (188, 138), "spacing": 14.5}, 
    "tin_part_4": {"coords": (240, 138), "spacing": 14.5}, 
    
    "employee_name": {"coords": (45, 162)}, 
    
    # Drops ~25 points per row from employee_name
    "registered_address": {"coords": (45, 187)},
    "local_home_address": {"coords": (45, 212)},
    
    # Date of Birth aligns its X with the TIN boxes
    "date_of_birth": {"coords": (88, 262), "spacing": 14.5},
    
    # Contact Number sits to the right of DOB
    "contact_number": {"coords": (200, 262), "spacing": 14.5},

    # -----------------------------------------------------------
    # PART II: EMPLOYER INFORMATION (PRESENT)
    # -----------------------------------------------------------
    # Drops down to the next main section
    "employer_name": {"coords": (45, 385)},
    "employer_address": {"coords": (45, 410)},
    
    # Zip code boxes align on the right side of the left panel
    "employer_zip": {"coords": (420, 410), "spacing": 14.5},

    # -----------------------------------------------------------
    # PART IV-B: FINANCIAL DETAILS (RIGHT COLUMN)
    # -----------------------------------------------------------
    # All amounts share the exact same X coordinate (485)
    "gross_compensation": {"coords": (485, 155)}, 
    
    # Item 36: SSS, GSIS, PHIC, PAG-IBIG
    "total_contributions": {"coords": (485, 275)},
    
    # Item 38: Total Non-Taxable/Exempt
    "non_taxable_compensation": {"coords": (485, 310)},
    
    # Item 51/54: Taxable Compensation
    "taxable_compensation": {"coords": (485, 600)}, # Estimated bottom section
    
    # Item 55/58: Tax Withheld
    "tax_withheld": {"coords": (485, 680)} # Estimated bottom section
}