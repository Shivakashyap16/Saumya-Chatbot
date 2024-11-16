from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS

# Configure the API key
API_KEY = 'Paste you API Key here'
genai.configure(api_key=API_KEY)

# Initialize the chat model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/chat', methods=['POST'])
def chat_with_bot():
    user_message = request.json.get('message')
    logging.debug(f"Received message: {user_message}")
    if user_message:
        try:
            response = chat.send_message(user_message)
            logging.debug(f"Bot response: {response.text}")
            return jsonify({'reply': response.text})
        except Exception as e:
            logging.error(f"Error interacting with the bot: {e}")
            return jsonify({'error': 'Failed to get a response from the chatbot.'}), 500
    else:
        return jsonify({'error': 'No message provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
