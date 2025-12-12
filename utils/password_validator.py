def has_uppercase(p):
    return any(c.isupper() for c in p)

def has_lowercase(p):
    return any(c.islower() for c in p)

def has_digit(p):
    return any(c.isdigit() for c in p)

def has_special_char(p):
    specials = "!@#$%^&*()-_=+[]{};:,<.>/?"
    return any(c in specials for c in p)

def has_min_length(p, length=8):
    return len(p) >= length

def is_strong_password(password):
    errors = []

    if not has_uppercase(password):
        errors.append("Missing uppercase letter")
    if not has_lowercase(password):
        errors.append("Missing lowercase letter")
    if not has_digit(password):
        errors.append("Missing number")
    if not has_special_char(password):
        errors.append("Missing special character")
    if not has_min_length(password):
        errors.append("Must be at least 8 characters long")

    return errors if errors else ["Password is strong!"]