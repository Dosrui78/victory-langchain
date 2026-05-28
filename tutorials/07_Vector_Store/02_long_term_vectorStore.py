import os
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path
from langchain_chroma import Chroma
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import DashScopeEmbeddings

vector_store = Chroma(collection_name="stu",  # collection_name 类似于数据库表表名
                      embedding_function=DashScopeEmbeddings(dashscope_api_key=os.getenv("QWEN_API_KEY")),  # 向量化
                      persist_directory=str(Path(__file__).parent / "vector_store_directory")  # 持久化路径
                      )

loader = CSVLoader(
    file_path=Path(__file__).parent.parent.parent / "data" / "text_files" / "program.csv", 
    encoding="utf-8", 
    csv_args={"delimiter": "，"}, 
    source_column="level"
    )

docs = loader.load()

# 向量存储的新增、删除、检索
vector_store.add_documents(
    documents=docs,             # 被添加的文档
    ids=["id" + str(i) for i in range(1, len(docs) + 1)]  # 给添加的文档提供id（字符串）
)

# 向量存储的删除 传入[id, id...]
# vector_store.delete(ids=["id1","id2","id3"])

# 检索 返回类型[Document, Document...]
result = vector_store.similarity_search("Is Python easy to learn?", k=3, filter={"source": "easy"})

print(result)