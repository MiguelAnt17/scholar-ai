import requests
import fitz  # PyMuPDF
import tempfile
import os

class PDFProcessor:
    """
    Class for PDF Files processing
    Upload a PDF from an URL and extract his content
    """
    def text_from_pdf(self, url: str) -> str:
        """
        Upload on PDF from and URL, extract his text and return it as a string

        Args:
            url (str): URL for the PDF.

        Returns:
            str: Content extracted from the PDF
        """
        try:
            print(f"Uploading the PDF: {url}...")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                response = requests.get(url, stream=True)
                response.raise_for_status()  
                # Temporary file
                for chunk in response.iter_content(chunk_size=8192):
                    temp_file.write(chunk)
                
                temp_filename = temp_file.name

            print("Download finished. Extracting text...")
            doc = fitz.open(temp_filename)
            
            full_text = []
            for page in doc:
                full_text.append(page.get_text())
            
            doc.close()

            # Join all texts from all pages in one
            final_text = "".join(full_text)
            
            cleaned_text = ' '.join(final_text.replace('\n', ' ').split())
            
            print("Text extraction concluded.")
            return cleaned_text

        except requests.exceptions.RequestException as e:
            print(f"Error uploading the file: {e}")
            return ""
        except Exception as e:
            print(f"Error processing the PDF: {e}")
            return ""
        finally:
            if 'temp_filename' in locals() and os.path.exists(temp_filename):
                os.remove(temp_filename)