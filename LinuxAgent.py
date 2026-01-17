import os

os.environ["GOOGLE_API_KEY"] = ""

# AI LLM Model Access
from langchain_google_genai import ChatGoogleGenerativeAI

google_llm = ChatGoogleGenerativeAI( model="gemini-2.5-flash", temperature=0, max_tokens=1000)

response = google_llm.invoke("tell me how to check total ram free in linux")

print(response.content)