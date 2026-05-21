from pathlib import Path
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

embeddings = DashScopeEmbeddings()

loader = CSVLoader(file_path=Path(__file__).parent.parent.parent.parent / "data" / "text_files" / "stu.csv", encoding="utf-8")

docs = loader.load()

for doc in docs:
    print(embeddings.embed_query(doc.page_content))