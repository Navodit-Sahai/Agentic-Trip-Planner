from typing import Optional
from pydantic import Field
from langchain_groq import ChatGroq
from utils.config_loader import load_config
from pydantic import BaseModel
import os




class ConfigLoader:
    def __init__(self):
        print(f"Loaded config.....")
        self.config = load_config()
    
    def __getitem__(self, key):
        return self.config[key]




class ModelLoader(BaseModel):
    model_provider="groq"
    config: Optional[ConfigLoader]=Field(default=None,exclude=True)

    def model_post_init(self, __context:any) -> None:
        self.config=ConfigLoader()

    class Config:
        arbitrary_types_allowed=True

    def load_llm(self):
        """It loads and return the LLM Model"""
        print("LLM loading...")
        print("loading model from model provider: {self.model_provider}")
        groq_api_key=os.getenv("GROQ_API_KEY")
        model_name=self.config["llm"]["groq"]["model_name"]
        llm=ChatGroq(model_name="llama-3.3-70b-versatile",api_key=groq_api_key)

        return llm 