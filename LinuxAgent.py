import os

os.environ["GOOGLE_API_KEY"] = ""

# AI LLM Model Access
from langchain_google_genai import ChatGoogleGenerativeAI

google_llm = ChatGoogleGenerativeAI( model="gemini-2.5-flash", temperature=0)

# response = google_llm.invoke("how to install package on amazon linux")

# print(response.content)

from langchain_community.tools import ShellTool

shell_tool = ShellTool()

# print(shell_tool.run({"commands": ["free -h", "date"]}))

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

tools = [shell_tool]

# Agent
agent = create_agent(
    model=google_llm,
    tools=tools

)

userPrompt = input("Enter Your Requirement ")

system_msg = SystemMessage("""
                            you are linux administrator, and always give final output only
                           """)

input_message = HumanMessage(content=userPrompt)

messages = [
    system_msg,
    input_message
]

# Invoke (replacement for .run)
result = agent.invoke({
"messages":messages
})

# print(result)

messages = result["messages"]

# Find the last assistant message (the graph may end on a ToolMessage otherwise)
last_ai_message = next(m for m in reversed(messages) if isinstance(m, AIMessage))

# Access the content
final_text_content = last_ai_message.content
print(f"Final AI response content: {final_text_content}")