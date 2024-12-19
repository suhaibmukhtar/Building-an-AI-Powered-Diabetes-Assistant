# LLMs and Embedding Techniques using HuggingFace
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

#embedding technique "sentence transformer"

#loading environment variables
load_dotenv()

#setting the environment variables
os.environ['HUGGINGFACE_API_KEY']=os.getenv('HUGGINGFACE_API_KEY')

embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2") #using the "all-MiniLM-L6-v2" model for embed

text="What are main concerns of diabetes"
query_embed=embeddings.embed_query(text) #embedding the text
print(query_embed) #printing the embedding of the text
print(len(query_embed))

#to calculate embedding of multiple sentences
text=["What are main concerns of diabetes","What are main concerns of cancer"]
query_docs=embeddings.embed_documents(text) #embedding the text
print("docs\n",query_docs) #printing the embedding of the text
print("Length of embedding-matrix\n",len(query_docs))