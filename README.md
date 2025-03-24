# Medical Chatbot using FAISS and OpenAI

This project is a backend and frontend implementation of a medical chatbot that answers user questions based on medical data. The backend uses Flask, FAISS, and OpenAI GPT-4 to process and retrieve information, while the frontend is built with React to provide a user-friendly interface.

## UI Preview

<img width="712" alt="image" src="https://github.com/user-attachments/assets/f985a377-0d96-4d4d-a3e7-407e3088e026" />


## Key Features

- **FAISS Integration**: The project utilizes FAISS (Facebook AI Similarity Search) to search through medical documents and retrieve the most relevant information for user queries. This enables fast, efficient, and accurate document retrieval.
- **OpenAI GPT-4**: GPT-4 is used to generate human-like responses based on the retrieved documents, making the answers contextually relevant to the user's question.
- **Medical Data**: The backend loads medical data from verified sources and splits it into smaller chunks for better search and retrieval performance.
- **Flask Backend**: The backend is built using Flask, which exposes an API endpoint that receives a question and returns a medical answer.
- **React Frontend**: The frontend is a simple React-based interface that allows users to ask questions and view responses from the chatbot.

## Backend Setup (Flask)

### Dependencies

- `Flask`
- `langchain_community`
- `llama_index`
- `langchain_openai`
- `langchain_core`
- `faiss`
- `flask_cors`
- `dotenv`

### Installation

1. Clone the repository.

2. Set up your `.env` file with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```
3. Place your medical data in the `medical_data` folder.

### Running the Backend

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. The backend will be running on `http://localhost:5000`.

## Frontend Setup (React)

### Installation

1. Clone the repository.
2. Install the necessary React dependencies:
   ```bash
   npm install
   ```

### Running the Frontend

1. Run the React app:

   ```bash
   npm start
   ```

2. The frontend will be running on `http://localhost:3000`.

## How It Works

1. **Frontend**: The user asks a medical question through the React-based interface.
2. **Backend**: The Flask server receives the user's question and processes it. It uses FAISS to retrieve the most relevant documents from the medical data.
3. **OpenAI GPT-4**: The backend sends the retrieved documents and the user’s question to the GPT-4 model, which generates a response.
4. **Response**: The backend sends the generated answer back to the frontend, which displays it along with a disclaimer.
