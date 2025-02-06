import os
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from dotenv import load_dotenv

load_dotenv()
# Add some debug logging
print("Initializing agent...")

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("How long would it take for an elephant to cross the united states from florida to california?")
