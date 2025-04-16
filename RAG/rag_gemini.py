import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain.chains import RetrievalQA

# 🔑 Set your Google API Key (Gemini)
os.environ["GOOGLE_API_KEY"] = "AI"  # Replace with your Gemini API key

# 1️⃣ Load Angular source files from 'data/' folder
loader = DirectoryLoader("data", glob="**/*.*", loader_cls=TextLoader)
raw_docs = loader.load()

# 2️⃣ Chunk the documents for embedding
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = splitter.split_documents(raw_docs)

# 3️⃣ Embed the documents using Gemini Embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.from_documents(docs, embeddings)

# 4️⃣ Set up retriever and Gemini LLM
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash", temperature=0.3)

# 5️⃣ Combine into a RAG pipeline
rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 6️⃣ Ask a question related to your Angular UI library
query = "do we have doulble click event UiButtonComponent? if yes how to ues it give example ? if no then tell me how to implement it ?"
response = rag_chain.run(query)

# 🔁 Output the result
print("\n🧠 Gemini RAG Answer:")
print(response)
