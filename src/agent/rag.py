from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama 
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class VectorStoreManager:
    """
    Generate the creation and storage of text embeddings on a vectorial database
    """
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 100):
        """
        Inicialize the vectorial database manager

        Args:
            chunk_size (int): Lenght of each piece of text
            chunk_overlap (int): Overlap bewtween consecutives chunks
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )
        self.embedding_function = SentenceTransformerEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
        # Initialize ChromaDB
        self.vector_store = Chroma(
            persist_directory="./data/chroma_db",
            embedding_function=self.embedding_function
        )

    def index_text(self, text: str, source: str):
        """
        Process one text, split it into chunks and add them to the vectorial database

        Args:
            text (str): Full text content to be stored
            source (str): Identifier for text origin
        """
        print(f"Creating chunks for the document: {source}...")
        # Split the text into chunks
        chunks = self.text_splitter.split_text(text)
        
        print(f"Generating and saving embeddings for {len(chunks)} chunks...")

        # Add chunks to the database
        self.vector_store.add_texts(
            texts=chunks,
            metadatas=[{"source": source} for _ in chunks] 
        )

        self.vector_store.persist()
        print("Indexation done.")


    def get_retriever(self, k: int = 4):
        """
        Get a retriever from the vectorial database
        Retriever does the search by similarity

        Args:
            k (int): number of relevants chunks to return

        Returns:
            Langchain retriever
        """
        return self.vector_store.as_retriever(search_kwargs={"k": k})



class RAGChain:
    """
    RAG Logic
    """
    def __init__(self, retriever):
        self.retriever = retriever
        
        # LLM that will be used
        self.llm = Ollama(model="llama3")

        # Promp engineering
        template = """
        Based solely on the following CONTEXT, answer the QUESTION.
        If the answer is not in the context, say, “I did not find information about this in the context provided.”
        Be concise and direct.

        CONTEXT:
        {context}

        QUESTION:
        {question}

        ANSWER:
        """
        self.prompt = PromptTemplate.from_template(template)

    def create_chain(self):
        """
        Create and returns a RAG chain usiong LangChain Expression Language (LCEL)
        """
        chain = (
            {"context": self.retriever, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
        return chain