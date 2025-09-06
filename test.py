from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])

chain = LLMChain(llm=llm, prompt=prompt)

output = chain.stream("tell me a joke")

for message in output:
    print(message)

# messages = prompt.format_messages(content="tell me a joke")

# output = chat.stream(messages)

# for message in output:
#     print(message.content)

