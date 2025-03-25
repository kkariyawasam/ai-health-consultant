import { useState } from "react";
import "./App.css";


export default function MedicalChatbot() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    try {
      const res = await fetch("http://localhost:5000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error("Error fetching response:", error);
    }
    setLoading(false);
  };

  return (
    <div className="chat-container">
      <h1 className="chat-title">Medical Chatbot</h1>
      <textarea
        className="chat-input"
        rows="3"
        placeholder="Ask a medical question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button
        className="chat-button"
        onClick={handleAsk}
        disabled={loading}
      >
        {loading ? "Thinking..." : "Ask"}
      </button>

      {response && (
        <div className="chat-response">
          <p className="response-title">Answer:</p>
          <p>{response.answer}</p>
          <p className="chat-disclaimer">
            {response.disclaimer}
          </p>
        </div>
      )}
    </div>
  );
}
