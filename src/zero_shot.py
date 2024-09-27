from langchain_core.prompts import PromptTemplate
from llm import build_fined_tuned_mistra_small, build_structured_mistral_large, build_structured_mistral_small

prompt = PromptTemplate.from_template("""
    Your Goal is to extract strucutred information on which education backgrounds are required. Make it match the following Output format:
        {{
            "high_school='No',
            apprenticeship='No',
            bachelor='Yes',
            master='No',
            phd='No'
        }}
    Please output the extracted information in JSON format. Provide nothing else
    input: {query}
     """)

fine_tuned_llm =  build_fined_tuned_mistra_small()
fine_tuned_chain = prompt | fine_tuned_llm

small_llm = build_structured_mistral_small()
small_chain = prompt | small_llm

large_llm = build_structured_mistral_large()
large_chain = prompt | large_llm

if __name__ == "__main__":
    response = fine_tuned_chain.invoke({"query": "- Higher degree in Data Science, Computer Science, Math or other analytical intense specialties"})
    print(response)
