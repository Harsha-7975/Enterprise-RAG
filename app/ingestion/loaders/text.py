import logfire

def parse_text(file_path: str):
    """
    Parses normal text files
    
    """
    with logfire.span("Text parsing",filename=file_path):
        try:
            with open(file_path,"r",encoding="utf-8",errors="ignore") as f:
                return f.read()
        except Exception as e:
            logfire.error(f"Text Parse failed: {e}")
            raise e