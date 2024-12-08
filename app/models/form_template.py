from typing import Dict

from beanie import Document


class FormTemplate(Document):
    name: str
    # fields: словарь {field_name: field_type},
    # field_type in ["email", "phone", "date", "text"]
    fields: Dict[str, str]

    class Settings:
        name = "form_templates"
