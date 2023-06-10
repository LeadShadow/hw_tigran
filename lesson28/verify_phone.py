import re
# +38093(93)-31-389 -> 380939331389
def verify_phone(phone: str) -> str:
    new_phone = re.sub(r'\+|\(|\)|-| |[a-zA-ZА-Я-а-я]', '', phone)
    return new_phone
