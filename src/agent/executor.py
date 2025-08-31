from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.llms import Ollama
from typing import List

from tools import SearchPapersTool

class ResearchAgentExecutor:
    """
    Configurate and execute the agent
    """
    def __init__(self):
        self.tools: List = [SearchPapersTool()]

        self.llm = Ollama(model="llama3")

        prompt = hub.pull("hwchase17/react")


        agent = create_react_agent(self.llm, self.tools, prompt)


        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True  
        )

    def run(self, query: str):
        """
        Run the agent with a query
        """
        result = self.agent_executor.invoke({"input": query})
        return result['output']