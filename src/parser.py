from pydantic import BaseModel
from output_model import EducationRequirementOutput
import json
import logging

class InputModel(BaseModel):
    input: str
    output: EducationRequirementOutput

def parse_input(file_path: str) -> list[InputModel]:
    items = []
    with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            try:
                item['output'] = json.loads(item['output'].replace("'", '"'))
                items.append(InputModel(**item))
            except Exception:
                logging.info("invalid item", item)
    return items
