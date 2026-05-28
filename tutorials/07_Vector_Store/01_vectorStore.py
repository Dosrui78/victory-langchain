import os
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path
from langchain_community.document_loaders import CSVLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings


vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(dashscope_api_key=os.getenv("QWEN_API_KEY")))

loader = CSVLoader(
    file_path=Path(__file__).parent.parent.parent / "data" / "text_files" / "stu.csv",
    encoding="utf-8",
    csv_args={
        "delimiter": "，",       # 分隔符
        "quotechar": '"',       # 引用符
        "fieldnames": ["name", "age", "gender", "hobby"],     # 列名
    },
)

docs = loader.load()

# 向量存储的新增、删除、检索
vector_store.add_documents(
    documents=docs,             # 被添加的文档
    ids=["id" + str(i) for i in range(1, len(docs) + 1)]  # 给添加的文档提供id（字符串）
)

result = vector_store.similarity_search("吴诗琪是男的吗", k=3)

print(result)