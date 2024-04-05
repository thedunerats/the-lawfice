import re


def is_phone_number(number) -> bool:
    phone_pattern = r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$"
    if re.match(phone_pattern, number):
        return True
    return False
