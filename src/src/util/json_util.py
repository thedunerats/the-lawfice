
def validate_email_request_json(email_json) -> (bool, str):
    if email_json.get('your-phone') is None:
        return False, "EMPTY PHONE NUMBER"
    if email_json.get('your-email') is None:
        return False, "EMPTY EMAIL ADDRESS"
    if email_json.get('your-message') is None:
        return False, "EMPTY MESSAGE"
    if email_json.get('your-name') is None:
        return False, "EMPTY NAME"
    if email_json.get('your-case') is None:
        return False, "EMPTY CASE"
    return True, "NO REASON"

