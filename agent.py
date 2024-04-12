from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain_core.prompts import SystemMessagePromptTemplate
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolset, App
from prompts import BASE_SYSTEM_MESSAGE
from config import OPENAI_API_KEY

llm = ChatOpenAI(model='gpt-4-1106-preview', temperature=0,api_key=OPENAI_API_KEY)

prompt = OpenAIFunctionsAgent.create_prompt(
  system_message=SystemMessagePromptTemplate.from_template(BASE_SYSTEM_MESSAGE)
)

tools = ComposioToolset(apps=[App.SLACK, App.LINEAR])

agent = OpenAIFunctionsAgent(
  llm=llm,
  tools=tools,
  prompt=prompt
)

agent_executor = AgentExecutor(
  agent=agent, 
  tools=tools, 
  verbose=True
)