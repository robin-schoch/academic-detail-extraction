
from parser import InputModel
from jinja2 import Environment, FileSystemLoader

from output_model import EducationRequirementOutput

def save_to_markdown(title: str, wrong_items: list[tuple[InputModel, EducationRequirementOutput]], correct_items: list[tuple[InputModel, EducationRequirementOutput]], failed_items: list[InputModel]):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('src/template.jinja')
    output = template.render(
        test=title,
        correct=len(correct_items),
        wrong=len(wrong_items),
        failed=len(failed_items),
        correct_items=correct_items,
        wrong_items=wrong_items,
        failed_items=failed_items
    )
    with open(f'results/{title.replace(" ", "_")}-output.md', 'w') as f:
        f.write(output)
