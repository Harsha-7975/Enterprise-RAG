import logfire
from unstructured.partition.auto import partition

def parse_office(file_path: str):
    """
    Parses Office documents (.docx, .pptx) using the Unstructured library.
    Unlike PDFs, these formats are structured and lightweight, so they are processed locally.
    
    """
    with logfire.span("Office Parsing",filename=file_path):
        try:
            elements = partition(filename=file_path)
            full_text = "\n".join([str(el) for el in elements])

            if not full_text.strip():
                logfire.warning(f" Unstructured retuned empty text for {file_path}")
            else:
                logfire.info(f"Successfully parsed {len(full_text)} characters from {file_path} ")

            return full_text
        except Exception as e:
            logfire.error(f"Error parsing Office file {file_path}: {e}")
            raise e