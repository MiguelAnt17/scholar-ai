import os
from agent.rag import VectorStoreManager

def test_indexing():

    data_dir = "data"
    # Lista todos os ficheiros .txt na pasta de dados
    txt_files = [f for f in os.listdir(data_dir) if f.endswith(".txt")]

    if not txt_files:
        print("No .txt file founded on folder /data. Execute the pipeline first.")
        return

    # Pega no primeiro ficheiro para o teste
    first_file_path = os.path.join(data_dir, txt_files[0])
    print(f"--- Testing the indexation in file: {first_file_path} ---")

    try:
        with open(first_file_path, "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        print(f"Error: No file found {first_file_path}")
        return
    except Exception as e:
        print(f"Error reading the file: {e}")
        return
        
    manager = VectorStoreManager()
    manager.index_text(text_content, source=txt_files[0])

if __name__ == "__main__":
    test_indexing()











'''
PHASE 2 MAIN.PY

import argparse
import os
from agent.tools import PaperFetcher
from processing.parser import PDFProcessor

def main(query: str, num_papers: int = 3):
    """
    1. Search for articles.
    2. Process the PDF for each article and extract the text.
    3. Save the extracted text in .txt files.
    """
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)

    # 1
    fetcher = PaperFetcher()
    papers = fetcher.search_arxiv(query, max_results=num_papers)

    if not papers:
        print(f"No article found for the query: '{query}'")
        return

    # 2 and 3
    processor = PDFProcessor()
    for i, paper in enumerate(papers):
        print(f"\n--- Processing article {i+1}/{len(papers)}: {paper.title} ---")
        
        extracted_text = processor.text_from_pdf(paper.pdf_url)
        
        if extracted_text:
            safe_filename = "".join(c for c in paper.title if c.isalnum() or c in (' ', '.')).rstrip()
            output_path = os.path.join(output_dir, f"{safe_filename}.txt")
            
            try:
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(extracted_text)
                print(f"Text from the article saved at: {output_path}")
            except IOError as e:
                print(f"Error saving the file {output_path}: {e}")
        else:
            print(f"Cannot extract text from the article : {paper.title}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search AI Agent for academics articles.")
    parser.add_argument("--query", type=str, required=True, help="Search topic.")
    args = parser.parse_args()
    
    main(args.query)

# The prompt line was: python src/main.py --query "transformers models"'''


'''
TESTING tools.py

from agent.tools import PaperFetcher

if __name__ == "__main__":
    fetcher = PaperFetcher()
    query = "transformer models"
    papers = fetcher.search_arxiv(query)

    for i, paper in enumerate(papers):
        print(f"--- Article {i+1} ---")
        print(f"Title: {paper.title}")
        print(f"Authors: {', '.join(paper.authors)}")
        print(f"URL of PDF: {paper.pdf_url}\n")
        

        
TESTING parser.py
        
from agent.tools import PaperFetcher
from processing.parser import PDFProcessor 

if __name__ == "__main__":
    fetcher = PaperFetcher()
    processor = PDFProcessor() 
    
    query = "transformer models"
    papers = fetcher.search_arxiv(query)

    if not papers:
        print("No article found.")
    else:
        first_paper = papers[0]
        
        print(f"\n--- Processing Article 1: {first_paper.title} ---")
        
        extracted_text = processor.text_from_pdf(first_paper.pdf_url)
        
        if extracted_text:
            print("\n--- Sample of extracted text (first 500 car.) ---")
            print(extracted_text[:500] + "...")
        else:
            print("Cannot extract text from the PDF.")



'''