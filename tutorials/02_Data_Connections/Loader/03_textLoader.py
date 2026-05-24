from pathlib import Path
from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path=Path(__file__).parent.parent.parent.parent / "data" / "text_files" / "text.txt", encoding="utf-8")
docs = loader.load()

print(docs)