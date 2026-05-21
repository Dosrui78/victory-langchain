from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

loader = TextLoader(file_path=Path(__file__).parent.parent.parent.parent / "data" / "text_files" / "text.txt", encoding="utf-8")
docs = loader.load()

spliter = CharacterTextSplitter(
    separator = "\n\n",
    chunk_size = 100,
    chunk_overlap  = 0,
    length_function = len,
)

docs = spliter.split_documents(docs)
print(docs)
for doc in docs:
    print("=" * 100)
    print(doc)
    print("=" * 100)