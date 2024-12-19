<h1>Steps for Ollma</h1>
<li>1. Go to "Ollama.com" and download the Ollama model.</li>
<li>Ollama Supports various Open-source models such as Llama 3, Phi 3 Mini, Phi 3 Medium, Gemma, Mistral etc.</li>
<li>2. After downloading and installation of the Ollama model, Open the Command Prompt to verify installation</li>
<p> For downloading any of these open-source models, specific commands are shown in github of Ollama e.g. for downloading "Gemma" with 2B parameters, we run command <b>"ollama run gemma:2b"</b></p><p>This command pulls the open source model from github and then downloads that in our machine. If already download then it will run this model, and you can chat with model.</p>
<h2><b>Ollama</b><h2>
<li>The Ollama is an open-source AI model that can be used for various purposes, including chatbots, language translation, text generation etc.</li>
<li>Ollama also supports embedding-models, making it suitable to build RAG applications, and is mainly used when we are dealing with sensitive data, that company doesn't want to share with others</li>
<li>The Ollama combines the prompts with the related data feteched from the loaded documents, whose embeddings are stored inside the vector stores.</li>
<li> In order to use any model for Embeddings, we need to install it</li>
<li>Whatever Open-source model we will download initally just put the name of that in embeddings.</li>

<p>from langchain_community.embeddings import OllamaEmbeddings<br>
embeddings=(<br>
    OllamaEmbeddings(model='gemma:2b') #by default it uses llama2 <br>
)<br>
</p>
<p>
This embed_documents takes input list of sentence<br>
r1=embeddings.embed_documents( <br>
    [<br>
        "Alpha is the first letter of Greek alphabet.",<br>
        "Beta is the second letter of Greek alphabet.",<br>
    ]<br>
)<br>
</p>
The above code snippet is used to embed these two sentences.<br>
print(f1[0]) #will display the 2048 size vector for sentence one<br>
print(f1[1]) #will display the 2048 embedding vector for sentence two<br>

query_result=embeddings.embed_query("what is the second letter of Greek alphabet")<br>
#it will match with second sentence embeddings <br>

<h5>to download any vector embedding model or open-source model in cmd just run below command</h5>
<h6>ollama pull exbai-embed-large</h6>
