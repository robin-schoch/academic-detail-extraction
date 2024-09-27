import os
from pydantic import SecretStr, BaseModel
import getpass
from langchain_mistralai import ChatMistralAI
from langchain_core.runnables import Runnable
from langchain_core.language_models import LanguageModelInput
from typing import Union, Dict

from output_model import EducationRequirementOutput

if "MISTRAL_API_KEY" not in os.environ:
    os.environ["MISTRAL_API_KEY"] = getpass.getpass("Enter your Mistral API key: ")

API_KEY = os.getenv("MISTRAL_API_KEY")
if API_KEY is None:
    raise Exception("Missing Mistral API Key")
MISTRAL_API_KEY = SecretStr(API_KEY)

def build_fined_tuned_large_mistra_small() -> Runnable[LanguageModelInput, Union[Dict, BaseModel]]:
    base_model = ChatMistralAI(api_key=MISTRAL_API_KEY, model_name="ft:mistral-large-latest:d77d9de1:20240927:8f545463", temperature=0, max_retries=1, timeout=15)
    structured_llm = base_model.with_structured_output(EducationRequirementOutput)
    return structured_llm

def build_fined_tuned_mistra_small() -> Runnable[LanguageModelInput, Union[Dict, BaseModel]]:
    base_model = ChatMistralAI(api_key=MISTRAL_API_KEY, model_name="ft:mistral-small-latest:d77d9de1:20240927:3f86568f", temperature=0, max_retries=1, timeout=10)
    structured_llm = base_model.with_structured_output(EducationRequirementOutput)
    return structured_llm

def build_structured_mistral_small() -> Runnable[LanguageModelInput, Union[Dict, BaseModel]]:
    base_model = ChatMistralAI(api_key=MISTRAL_API_KEY, model_name="mistral-small-latest", temperature=0, max_retries=1, timeout=5)
    structured_llm = base_model.with_structured_output(EducationRequirementOutput)
    return structured_llm

def build_structured_mistral_large() -> Runnable[LanguageModelInput, Union[Dict, BaseModel]]:
    base_model = ChatMistralAI(api_key=MISTRAL_API_KEY, model_name="mistral-large-latest", temperature=0, max_retries=1, timeout=10)
    structured_llm = base_model.with_structured_output(EducationRequirementOutput)
    return structured_llm

if __name__ == "__main__":
    build_structured_mistral_small()
