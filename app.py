from flask import Flask, request, jsonify
from langchain_community.chat_models import ChatOpenAI
from llama_index.core import SimpleDirectoryReader
from llama_index.core import GPTVectorStoreIndex
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document  
from flask_cors import CORS
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os

app = Flask(__name__)
CORS(app)  # Allow all origins


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Load documents from verified medical sources
docs = SimpleDirectoryReader("medical_data").load_data()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # Adjust based on document size
    chunk_overlap=100  # Ensures continuity between chunks
)

split_docs = []
for doc in docs:
    chunks = text_splitter.split_text(doc.get_content())
    for chunk in chunks:
        split_docs.append(Document(page_content=chunk))

# Initialize FAISS with chunked documents
embeddings = OpenAIEmbeddings()
vector_db = FAISS.from_documents(split_docs, embeddings)

# Initialize Chat Model
chat_model = ChatOpenAI(model_name="gpt-4")

@app.route("/ask", methods=["POST"])
def ask_question():
    user_input = request.json.get("question")
    if not user_input:
        return jsonify({"error": "Question is required"}), 400
    
    # Retrieve relevant documents
    similar_docs = vector_db.similarity_search(user_input, k=3)
    texts = [doc.page_content for doc in similar_docs]
    
    # Generate response
    response = chat_model.predict(f"Use the following medical data to answer: {texts}\n\n{user_input}")
    
    return jsonify({"answer": response,"disclaimer": "⚠️ Disclaimer: This response is generated based on available medical documents and AI processing. It may not be 100% accurate or up-to-date. Please consult a qualified healthcare professional for medical advice."})

if __name__ == "__main__":
    app.run(debug=True)