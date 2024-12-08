from typing import List

from fastapi import APIRouter

from app.models.form_template import FormTemplate
from app.schemas import FormTemplateOut, InputData
from app.services.form_service import find_matching_template
from app.utils.validation import deduce_type

router = APIRouter()


@router.post("/get_form")
async def get_form(data: InputData):
    form_dict = data.root  # Здесь ваш словарь полей
    template_name = await find_matching_template(form_dict)

    if template_name:
        return {"template_name": template_name}

    # Если подходящий шаблон не найден
    result = {f_name: deduce_type(f_value) for f_name, f_value in form_dict.items()}
    return result


@router.get("/templates", response_model=List[FormTemplateOut])
async def get_templates():
    templates = await FormTemplate.find({}).to_list()
    return templates
