import arxiv
from dataclasses import dataclass


@dataclass
class Paper:
    """Data structure to save the paper information"""
    title: str
    authors: list[str]
    summary: str
    pdf_url: str

# Class Paper is created to convert the format of the arXiv results into an internal format "Paper" - Abstraction

class PaperFetcher:
    """
    Class to search and obatin the papers from academics sources as arXiv
    """
    def search_arxiv(self, query: str, max_results: int = 3) -> list[Paper]:
        """
        Search in arXiv for one "query" and returns one list with Paper objects

        Args:
            query (str): Search string/word
            max_results (int): Max number of returned results

        Returns:
            list[Paper]: List of Paper objects elements
        """

        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        results = search.results()

        papers = []
        for result in results:
            # For each result, i created a Paper data structure
            # The code is independent of arXiv
            paper = Paper(
                title=result.title,
                authors=[author.name for author in result.authors],
                summary=result.summary,
                pdf_url=result.pdf_link
            )
            papers.append(paper)
        
        print(f"Found {len(papers)} papers in arXiv sobre '{query}'.")
        return papers
    
# Just need to add a new method in this class if i want to change the data source