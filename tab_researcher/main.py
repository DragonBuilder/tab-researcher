from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(temperature=0)

tools = load_tools(["serpapi"], llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

result = agent.run("Tablets under Rs. 20000")

print(result)