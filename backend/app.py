
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client

app = Flask(__name__)
CORS(app)

def get_supabase():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")

    if not url or not key:
        raise RuntimeError("Supabase environment variables are missing.")

    return create_client(url, key)

@app.get("/")
def home():
    return jsonify({
        "message": "Question Bank Generator API is running"
    })

@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/api/questions")
def get_questions():
    try:
        supabase = get_supabase()
        result = (
            supabase.table("question_bank_questions")
            .select("*")
            .order("id")
            .execute()
        )
        return jsonify(result.data)
    except Exception:
        app.logger.exception("Failed to fetch questions")
        return jsonify({"error": "Could not fetch questions"}), 500
    
@app.post("/api/questions")
def add_question():
    try:
        data = request.get_json()

        required = [
            "question_text", "subject", "unit",
            "marks", "question_type", "difficulty"
        ]

        if not data or any(field not in data for field in required):
            return jsonify({"error": "Missing required fields"}), 400

        supabase = get_supabase()
        result = (
            supabase.table("question_bank_questions")
            .insert({
                "question_text": data["question_text"],
                "subject": data["subject"],
                "unit": data["unit"],
                "marks": data["marks"],
                "question_type": data["question_type"],
                "difficulty": data["difficulty"],
                "previously_asked": data.get("previously_asked", False)
            })
            .execute()
        )

        return jsonify(result.data), 201

    except Exception:
        app.logger.exception("Failed to add question")
        return jsonify({"error": "Could not add question"}), 500
if __name__ == "__main__":
    app.run(debug=True)

