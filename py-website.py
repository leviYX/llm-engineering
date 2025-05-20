import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

load_dotenv("./.env")
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("api-key 未发现设置!")
elif not api_key.startswith("sk-proj-"):
    print("api-key 有问题")
else:
    print("ok，api-key没问题了")

openai = OpenAI()
message = "你好 gpt,你知道520是什么节日吗?"
response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":message}])
print(response.choices[0].message.content)
# 爬取网页
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
class Website:
    def __init__(self, url):
        """
        初始化一个操作对象
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

ed = Website("https://gushitong.baidu.com/index/ab-000001")

print("************")
print(ed.url)
print(ed.title)
print(ed.text)
