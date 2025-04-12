from langchain_community.document_loaders import UnstructuredFileLoader  #extracting text from a file
from langchain_community.document_loaders import DirectoryLoader         #load all the files from data
from langchain_text_splitters import CharacterTextSplitter               #splitting the text into smaller chunks
from langchain_huggingface import HuggingFaceEmbeddings                  #convert those chunks into vector embeddings
from langchain_chroma import Chroma                                      #store those enbeddings to chromaDB 
import onnxruntime

#Loading the embedding Model
embeddings = HuggingFaceEmbeddings()
loader = DirectoryLoader(path="data",
                         glob="./*.pdf",                                 #load all the pdf files
                         loader_cls=UnstructuredFileLoader)              #using unstructuredfileloader   

documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=2000,
                                      chunk_overlap=500)
text_chunks = text_splitter.split_documents(documents)

Vectordb = Chroma.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    persist_directory="Vector_db_directory"
)

print("Documents Vectorized")
