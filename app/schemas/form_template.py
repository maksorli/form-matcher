from typing import Dict

from pydantic import BaseModel, RootModel


class InputData(RootModel[dict[str, str]]):
    pass


class FormTemplateOut(BaseModel):
    name: str
    fields: Dict[str, str]
