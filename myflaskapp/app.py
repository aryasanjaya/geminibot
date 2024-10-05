# Imports for JSON handling and web framework
import os
import json
from flask import Flask, jsonify, request, send_file, send_from_directory

# Imports from langchain libraries
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Flask application initialization
app = Flask(__name__)

# Set environment variable (consider a secure way to store API keys)
os.environ["GOOGLE_API_KEY"] = "AIzaSyCDuZH1Bu9EEblE0leOoW_mo3ZxKHEzKEY"  # Replace with actual key

# Define error handler for improved logging and user experience
@app.errorhandler(Exception)
def handle_exception(error):
    # Log the error for debugging
    print(f"An error occurred: {error}")

    # Return a user-friendly error message
    return jsonify({"error": "An internal error occurred. Please try again later."}), 500

# Home page route
@app.route("/")
def home():
    return send_file("web/index.html")

# API route for text generation
@app.route("/api/generate", methods=["POST"])
def generate_api():
    if request.method == "POST":
        try:
            # Get JSON data from the request body
            req_body = request.get_json()

            # Extract content and model (consider validation)
            content = req_body.get("contents")
            model_name = req_body.get("model")

            # Create ChatGoogleGenerativeAI model and HumanMessage with content
            model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
            message = HumanMessage(content=content)

            # Stream model response with improved error handling
            response_stream = model.stream([message])

            # Stream response chunks with JSON formatting
            def stream():
                for chunk in response_stream:
                    yield f"data: {json.dumps({'text': chunk.content})}\n\n"

            return stream(), {"Content-Type": "text/event-stream"}

        except Exception as e:
            # Handle specific exceptions here if applicable
            # Otherwise, return a generic error response
            return jsonify({"error": str(e)}), 500

# Static file serving route
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("web", path)

# Run the Flask app in debug mode (consider a production-ready server for deployment)
if __name__ == "__main__":
    app.run(debug=True)