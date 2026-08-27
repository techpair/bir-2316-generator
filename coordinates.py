# Note: In PyMuPDF, (0,0) is the TOP-LEFT corner of the page.

# Format: "field_name": {"coords": (x, y), "spacing": optional_x_offset_per_character}

# Moving X left = smaller number. Moving Y down = larger number.

FIELDS = {
    # Perfect, leave as is!
    "employee_name": {"coords": (45, 162)}, 
    
    # Moved DOWN into the center of the box (Y from 159 -> 164)
    "gross_compensation": {"coords": (485, 155)}, 
    
    # TIN Adjustments:
    # - Y moved DOWN into the boxes (133 -> 138)
    # - All X starting points pushed RIGHT
    # - Spacing bumped to 14.5 so the digits spread nicely
    "tin_part_1": {"coords": (88, 138), "spacing": 14.5},  
    "tin_part_2": {"coords": (136, 138), "spacing": 14.5}, 
    "tin_part_3": {"coords": (188, 138), "spacing": 14.5}, 
    "tin_part_4": {"coords": (240, 138), "spacing": 14.5}, 
}