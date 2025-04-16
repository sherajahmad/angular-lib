import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# 🔑 Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-..."

# 📂 Load all .ts and .html files from data/
loader = DirectoryLoader("data", glob="**/*.ts", loader_cls=TextLoader)
documents = loader.load()

# ✂️ Split the docs into chunks (so LLM can process better)
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = splitter.split_documents(documents)

# 🔍 Embed & store in FAISS
vector_store = FAISS.from_documents(docs, OpenAIEmbeddings())

# 🧠 Build RAG Chain
retriever = vector_store.as_retriever(search_kwargs={"k": 3})
llm = ChatOpenAI(model="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 🤖 Ask a question
query = "do we have click event UiButtonComponent?"
response = qa_chain.run(query)

print("\n🧠 RAG Answer:")
print(response)
