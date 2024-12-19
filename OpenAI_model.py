from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from document_loaders import load_document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
# from langchain_chroma import Chroma
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
load_dotenv()


DATA_DIR="data"
#loading the documents from data-sources
data_files=os.listdir(DATA_DIR)
full_content=[]
for file in data_files:
    data_file_path = os.path.join(DATA_DIR, file)
    content = load_document(data_file_path)
    
    # Normalize the content to a string
    if isinstance(content, list):  # If the loader returns a list
        content = " ".join([str(item) for item in content])
    elif isinstance(content, dict):  # If the loader returns a dictionary
        content = " ".join([f"{key}: {value}" for key, value in content.items()])
    else:  # If the loader returns plain text
        content = str(content)
    
    full_content.append(content)

# Combine all content into one string for splitting
combined_content = " ".join(full_content)

# Apply the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=150
)
splitted_texts = text_splitter.split_text(combined_content)

#Specifying the openai model for converting text into vectors
embeddings=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=1024)

# text='This is my first practice'
# query_result=embeddings.embed_query(text) #will convert this into 1024 embeddings
# print(query_result)
# print(len(query_result))
# Wrap each chunk in a Document object
documents = [Document(page_content=text) for text in splitted_texts]

#Creating the embeddings and storing them inside a vector database
vector_db = Chroma.from_documents(documents,embeddings)

#query 
query="How diabetes can be prevented"
query_result=vector_db.similarity_search(query)
print(query_result)