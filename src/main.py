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
        print(f"URL of PDF: {paper.pdf_url}\n")'''