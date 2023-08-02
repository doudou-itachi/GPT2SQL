import os
import random
from langchain.chat_models import ChatOpenAI


class LLMInterface:
    def __init__(self, api_keys: list[str], model_name: str, temperature: int):
        self.api_keys = api_keys
        self.model_name = model_name
        self.temperature = temperature

    @property
    def get_api_key(self) -> str:
        return random.choice(self.api_keys)

    @property
    def create_llm_instance(self) -> ChatOpenAI:
        os.environ["OPENAI_API_KEY"] = self.get_api_key
        return ChatOpenAI(verbose=True, temperature=self.temperature, model_name=self.model_name)
