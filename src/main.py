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