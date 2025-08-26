# Ficheiro: src/agent/executor.py

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.llms import Ollama
from typing import List

# Importa a ferramenta que acabámos de definir
from .tools import SearchPapersTool

class ResearchAgentExecutor:
    """
    Configura e executa o agente de pesquisa.
    """
    def __init__(self):
        # 1. As ferramentas que o nosso agente pode usar
        self.tools: List = [SearchPapersTool()]

        # 2. O LLM que vai potenciar o agente
        self.llm = Ollama(model="llama3")

        # 3. O prompt que ensina o agente a comportar-se (estilo ReAct)
        # Puxamos um prompt testado e comprovado do LangChain Hub
        prompt = hub.pull("hwchase17/react")

        # 4. Criar o Agente
        # O agente é a combinação do LLM, das ferramentas e do prompt.
        # Ele é o "cérebro" que toma as decisões.
        agent = create_react_agent(self.llm, self.tools, prompt)

        # 5. Criar o Executor do Agente
        # O executor é o que de facto "corre" o agente num loop,
        # chamando as ferramentas e registando os resultados.
        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True  # 'verbose=True' mostra o processo de pensamento do agente
        )

    def run(self, query: str):
        """
        Executa o agente com uma determinada query.
        """
        # O método 'invoke' corre o loop do agente até ele decidir que terminou
        result = self.agent_executor.invoke({"input": query})
        return result['output']