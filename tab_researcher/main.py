from langchain.llms.openai import OpenAI
# from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent
import openai
from dotenv import load_dotenv

load_dotenv()

# chat_completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages = [
#         {
#             "role": "user",
#             "content": "Hello, how are you?"
#         }
#     ]
# )

# print(chat_completion)

# llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
llm = OpenAI(temperature=0)

# result = llm("Hello, how are you?")

# print(type(result))


tools = load_tools(["serpapi"], llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

result = agent.run("What tablet phones are available under Rs. 20,000? List the name and prices.")

print(result)



# print(llm(prompt))