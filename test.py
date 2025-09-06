from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

chat = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])

messages = prompt.format_messages(content="tell me a joke")

output = chat.stream(messages)

for message in output:
    print(message.content)

