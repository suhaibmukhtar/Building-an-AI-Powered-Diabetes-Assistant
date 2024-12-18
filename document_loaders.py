from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_community.document_loaders import JSONLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.document_loaders import BSHTMLLoader
from langchain_community.document_loaders import UnstructuredXMLLoader
from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders import Docx2txtLoader


def load_document(url):
    # Load the document from the given URL or path
    extention=url.split(".")[-1]
    if extention == "pdf":
        loader = PDFPlumberLoader(url)
        content = loader.load()
        return content
    elif extention == "csv":
        loader = CSVLoader(url)
        content = loader.load()
        return content
    elif extention == "json":
        loader = JSONLoader(url,
                            jq_schema=".",
                            json_lines=True)
        content = loader.load()
        return content
    elif extention == "md":
        loader = UnstructuredMarkdownLoader(url,encoding='utf-8')
        content = loader.load()
        return content
    elif extention == "html":
        loader = BSHTMLLoader(url,encoding='utf-8')
        content = loader.load()
        return content
    elif extention == "xml":
        loader = UnstructuredXMLLoader(url,encoding='utf-8')
        content = loader.load()
        return content
    elif extention == "txt":
        loader = TextLoader(url,encoding='utf-8')
        content = loader.load()
        return content
    elif extention == "docx":
        loader=Docx2txtLoader(url)
        content = loader.load()
        return content

