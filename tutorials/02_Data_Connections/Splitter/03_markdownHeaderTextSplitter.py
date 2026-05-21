from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown_document = "# Chapter 1\n\n    ## Section 1\n\nHi this is the 1st section\n\nWelcome\n\n ### Module 1 \n\n Hi this is the first module \n\n ## Section 2\n\n Hi this is the 2nd section"

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

spliter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
splits = spliter.split_text(markdown_document)

for split in splits:
    print("=" * 100)
    print(split)