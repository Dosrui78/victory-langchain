from pathlib import Path
from langchain_community.document_loaders import CSVLoader


loader = CSVLoader(
    file_path=Path(__file__).parent.parent.parent.parent / "data" / "text_files" / "stu.csv",
    encoding="utf-8",
    csv_args={
        "delimiter": "，",       # 分隔符
        "quotechar": '"',       # 引用符
        "fieldnames": ["name", "age", "gender", "hobby"],     # 列名
    },
)

documents = loader.load()
print(documents)

