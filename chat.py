from flask import Flask, request, jsonify
from flask import url_for
from chatterbot import ChatBot
import pandas as pd
import random
from waitress import serve

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return url_for('static', filename='data:,')

bot = ChatBot("TravelBot") 
df = pd.read_csv("E:\chat\ChatbotFaqs.csv")

# Define common travel queries
common_queries = [
    df['questions']
]

@app.route('/', methods=['GET', 'POST'])
def get_greeting():
    """Returns a greeting message for the chatbot."""
    return jsonify ("Hi! Welcome to the TravelBot. How can I help you today?\ 1. Queries\ 2. Complaint\ 3. Escalate Technical Issue")


@app.route('/handle_queries', methods=['POST'])
def handle_queries():
    choice = request.json.get('choice')
    try:
        choice = int(choice) - 1
        if 0 <= choice < len(df):
            answer = df.iloc[choice, 1]
            return jsonify(answer=answer)
        else:
            return jsonify(error="Invalid choice. Please try again."), 400
    except (ValueError, TypeError):
        return jsonify(error="Invalid input. Please enter a number."), 400


@app.route('/handle_complaint', methods=['POST'])
def handle_complaint():
    name = request.json.get('name')
    email = request.json.get('email')
    complaint = request.json.get('complaint')
    reference_number = random.randint(1000, 9999)
    # Implement logic to handle the complaint
    return jsonify(message=f"Thank you, {name}. We'll look into your complaint (Comp-{reference_number}) shortly.")



@app.route('/handle_technical_issue', methods=['POST'])
def handle_technical_issue():
    name = request.json.get('name')
    email = request.json.get('email')
    description = request.json.get('description')
    reference_number = random.randint(1000, 9999)
    return jsonify(message=f"Thank you, {name}. We'll investigate the issue (Tech-{reference_number}) shortly.")





if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=9090) 