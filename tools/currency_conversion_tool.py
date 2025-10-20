from dotenv import load_dotenv
from utils.currency_converter import CurrencyConverter
from langchain.tools import tool
import os


class CurrencyConverterTool:
    def __init__(self):
        load_dotenv()
        self.api_key=os.environ.get("EXCHANGE_RATE_API_KEY")
        self.currency_service=CurrencyConverter(self.api_key)
        self.currency_converter_tool_list=self._setup_tools

    def _setup_tools(self):
        """setup all tools for currency converter tool"""
        @tool
        def convert_currency(amount:float,from_currency:str,to_currency:str):
            """convert amount from one currency to another."""
            return self.currency_service.convert(amount,from_currency,to_currency)
        return [convert_currency]