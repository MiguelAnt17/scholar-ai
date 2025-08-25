import chromadb

def inspect_chroma_database():
    """
    Conecta-se à base de dados ChromaDB persistente e mostra o seu conteúdo.
    """
    # Passo 1: Conectar-se à mesma base de dados persistente
    client = chromadb.PersistentClient(path="./data/chroma_db")

    print("--- Coleções na Base de Dados ---")
    collections = client.list_collections()
    if not collections:
        print("Nenhuma coleção encontrada.")
        return

    for collection in collections:
        print(f"- Nome da Coleção: {collection.name}")

        # Passo 2: Obter um manipulador para a coleção
        # LangChain por defeito cria uma coleção chamada "langchain"
        db_collection = client.get_collection(name=collection.name)

        # Passo 3: Usar o método .get() para obter os dados
        # Podemos pedir para incluir os documentos (o texto dos chunks) e os metadados
        data = db_collection.get(include=["metadatas", "documents"])
        
        num_items = len(data['ids'])
        print(f"  A coleção '{collection.name}' tem {num_items} itens (chunks).")
        print("-" * 20)

        # Imprime os 5 primeiros itens como amostra
        for i in range(min(5, num_items)):
            doc_id = data['ids'][i]
            document_text = data['documents'][i][:100] + "..." # Mostra os primeiros 100 caracteres
            metadata = data['metadatas'][i]

            print(f"Item {i+1}:")
            print(f"  ID: {doc_id}")
            print(f"  Metadata (Fonte): {metadata}")
            print(f"  Documento (início): '{document_text}'\n")


if __name__ == "__main__":
    inspect_chroma_database()