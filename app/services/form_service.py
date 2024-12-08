from typing import Optional

from app.models.form_template import FormTemplate
from app.utils.validation import deduce_type


async def find_matching_template(form_dict: dict) -> Optional[str]:

    templates = await FormTemplate.find({}).to_list()

    for template in templates:
        match = True
        for field_name, field_type in template.fields.items():
            if field_name not in form_dict:
                match = False
                break
            detected_type = deduce_type(form_dict[field_name])
            if detected_type != field_type:
                match = False
                break
        if match:
            return template.name
    return None
