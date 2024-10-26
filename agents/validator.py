import re
import json

def validator(resume_data):
    """
    Validates extracted resume data and identifies issues
    """
    errors = []
    
    def validate_email(email):
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return bool(re.match(pattern, email))

    def validate_phone(phone):
        pattern = r"^\+?[1-9]\d{1,14}$"
        return bool(re.match(pattern, str(phone)))
    print(resume_data)
    resume_data = json.loads(resume_data)
    # Validate personal information
    personal_info = resume_data.get("personal_info", {})
    if not validate_email(personal_info.get("email", "")):
        errors.append("Invalid email format")
    if not validate_phone(personal_info.get("phone_no")):
        errors.append("Invalid phone number format")
        
    return errors if errors else "valid"