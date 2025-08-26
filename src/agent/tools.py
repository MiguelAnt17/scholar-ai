import arxiv
from dataclasses import dataclass
from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


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
                pdf_url=result.pdf_url
            )
            papers.append(paper)
        
        print(f"Found {len(papers)} papers in arXiv about '{query}'.")
        return papers
    
# Just need to add a new method in this class if i want to change the data source



class SearchInput(BaseModel):
    query: str = Field(description="Tha search topic for the academics articles.")

class SearchPapersTool(BaseTool):
    name = "SearchPapersTool"
    description = "Use this tool to search for academic articles on arXiv on a specific topic."
    args_schema: Type[BaseModel] = SearchInput
    
    def _run(self, query: str) -> str:
        
        fetcher = PaperFetcher()
        papers = fetcher.search(query)
        if not papers:
            return f"No articles found on '{query}'."
        
      
        results_str = [
            (
                f"Title: {p.title}\n"
                f"Authors: {', '.join(p.authors)}\n"
                f"URL of the PDF: {p.pdf_url}\n"
                f"Summary: {p.summary[:500]}..." # only the first 500 characters
            )
            for p in papers
        ]
        return "\n---\n".join(results_str)

    def _arun(self, query: str):
        raise NotImplementedError("Cannot support asyncronous execution.")