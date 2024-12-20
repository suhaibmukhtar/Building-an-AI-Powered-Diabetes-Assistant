# LLMs and Embedding Techniques using HuggingFace
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from document_loaders import load_document
from langchain_core.documents import Document

#embedding technique "sentence transformer"

#loading environment variables
load_dotenv()

#setting the environment variables
os.environ['HUGGINGFACE_API_KEY']=os.getenv('HUGGINGFACE_API_KEY')


#loading the text-documents from data-sources
Data_dir="data"
files = os.listdir(Data_dir)
combined_content=[]
for file in files:
    file_path=os.path.join(Data_dir,file)
    content=load_document(file_path)
    if isinstance(content,list):
        content=" ".join([str(item) for item in content])
    elif isinstance(content,dict):                       
        content=" ".join([f"{key}:{value}" for key,value in content.items()])
    else:
        content=str(content)
    combined_content.append(content)

text=" ".join(combined_content)

text_splitter=RecursiveCharacterTextSplitter(
                    chunk_size=600,
                    chunk_overlap=150
                    )
text_chunks=text_splitter.create_documents(combined_content)

# #coverting into doc type
# docs=[]
# for chunk in text_chunks:
#     # Create a Document object for each chunk
#     doc = Document(page_content=chunk.page_content)
#     docs.append(doc)

embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2") #using the "all-MiniLM-L6-v2" model for embed

vector_db=FAISS.from_documents(text_chunks,embeddings)
query="What is diabetes"
#not best way to directly query the vectordb
query_result=vector_db.similarity_search(query)
# print(query_result)

## Better way converting vector database as a retriever
retriever=vector_db.as_retriever()
query_result=retriever.invoke(query)
# print(query_result)

#saving Vector database on local
vector_db.save_local("faiss_index")

#loading vector database
loaded_db=FAISS.load_local('faiss_index',embeddings,allow_dangerous_deserialization=True)
query_result=loaded_db.similarity_search(query)
print(query_result)

# #FAISS :- Facebook ai similarity search, is a library for efficient similarty seacrch and clustering of dense
# #vectors. It contains algorithms that search in sets of vectors of any size up to ones that possibily do not 
# # fit in RAM. it also contains supporting code for evaluation and parameter tuning.
