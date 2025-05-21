import os

from dotenv import load_dotenv
from openai import OpenAI


class OpenAiUtil:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def buildOpenAiClient() -> OpenAI:
        load_dotenv("./.env")
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("api-key 未发现设置!")
        elif not api_key.startswith("sk-proj-"):
            print("api-key 有问题")
        else:
            print("ok，api-key没问题了")
        return OpenAI()