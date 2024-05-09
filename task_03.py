import re

def normalize_phone(phone_number: str) -> str:
    # Define pattern to remove all non-digit characters
    pattern = r"[^\d\+]"
    
    # Remove non-digit characters from the phone number
    normalized_phone_number = re.sub(pattern, "", phone_number)
    
    # Check if the number starts with '38' or '380' and prepend '+' accordingly
    if normalized_phone_number.startswith("+38"):
        return normalized_phone_number
    elif normalized_phone_number.startswith("380"):
        return "+" + normalized_phone_number
    else:
        # If it starts with neither '38' nor '380', assume it's a local Ukrainian number
        return "+38" + normalized_phone_number

# List of raw phone numbers with various formats
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Normalize each phone number in the list
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Print the normalized phone numbers
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)