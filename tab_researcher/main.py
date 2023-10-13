from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")

# tools = load_tools(["serpapi"], llm=llm)

# agent = initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent="zero-shot-react-description",
#     verbose=True
# )

# result = agent.run("Tablets under Rs.20000")

# print(result)
question = "Do you know what you are looking for in a Tablet phone? (Yes/No)"

while True:
    response = input(question + " ")
    if response.lower().startswith('y'):
        break
    print("\nPlease answer 'Yes' or 'No'\n")




# print(llm(prompt))