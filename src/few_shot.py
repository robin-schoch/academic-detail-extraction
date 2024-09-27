from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import PromptTemplate
from llm import build_fined_tuned_mistra_small, build_structured_mistral_large, build_structured_mistral_small


examples = [
    {
        "input": "- Bachelor's degree or Master's degree in Computer Engineering, Computer Science, Mathematics, Electrical Engineering, Information Systems, or IT",
        "output": "{{'High School': 'No', 'Apprenticeship': 'No', 'Bachelor': 'Yes', 'Master': 'Yes', 'PhD': 'No'}}"
    },
    {
        "input": "- Graduate degree in biostatistics or related discipline.",
        "output": "{{'High School': 'No', 'Apprenticeship': 'No', 'Bachelor': 'No', 'Master': 'Yes', 'PhD': 'No'}}"
    },
    {
        "input": "- Currently has, or is in the process of obtaining a Bachelor's degree in Computer Science, Computer Engineering, relevant technical field, or equivalent practical experience. Degree must be completed prior to joining Meta.",
        "output": "{{'High School': 'No', 'Apprenticeship': 'No', 'Bachelor': 'Yes', 'Master': 'No', 'PhD': 'No'}}"
    },
    {
        "input": "- MS in Machine Learning (PhD preferred)",
        "output": "{{'High School': 'No', 'Apprenticeship': 'No', 'Bachelor': 'No', 'Master': 'Yes', 'PhD': 'Yes'}}"
    },
    {
        "input": "- You hold an advanced degree (PhD preferred) or equivalent career experience in Computer Science, Applied Mathematics, Statistics or a related technical discipline.",
        "output": "{{'High School': 'No', 'Apprenticeship': 'No', 'Bachelor': 'No', 'Master': 'No', 'PhD': 'Yes'}}"
    },
]

example = PromptTemplate.from_template(" Extract the education needed to qualify for a job: {input} {output} ")
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example,
    suffix="Input: {query}",
    input_variables=["query"],
)

small_llm =  build_structured_mistral_small()
few_shot_small = few_shot_prompt | small_llm

fine_tuned_llm = build_fined_tuned_mistra_small()
few_shot_fine_tuned = few_shot_prompt | fine_tuned_llm

large_llm = build_structured_mistral_large()
few_shot_large = few_shot_prompt | large_llm

if __name__ == "__main__":
    response = few_shot_small.invoke({"query": "- Higher degree in Data Science, Computer Science, Math or other analytical intense specialties"})
    print(response)
