import re
from datetime import datetime

# пишем свою валидацию для проверки данных на лету
# стандартнач проверка на email
EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

# проверка на количество цифр и знак плюс
PHONE_REGEX = PHONE_REGEX = re.compile(r"^\+?\d{1,11}$")


def is_date(value: str) -> bool:
    # Проверим два формата: DD.MM.YYYY и YYYY-MM-DD
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            # проверка с помощью datetime
            datetime.strptime(value, fmt)
            return True
        except ValueError:
            pass
    return False


def is_phone(value: str) -> bool:
    return bool(PHONE_REGEX.match(value))


def is_email(value: str) -> bool:
    return bool(EMAIL_REGEX.match(value))


def deduce_type(value: str) -> str:

    if is_date(value):
        return "date"
    if is_phone(value):
        return "phone"
    if is_email(value):
        return "email"
    return "text"
