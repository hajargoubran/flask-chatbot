from flask import Flask, request, jsonify
from chatterbot import ChatBot
import pandas as pd
import random
""" import smtplib
from email.mime.text import MIMEText """

app = Flask(__name__)
bot = ChatBot("TravelBot")
df = pd.read_csv("ChatbotFaqs.csv")

# Define common travel queries
common_queries = [
    df['questions']
]


def get_greeting():
    """Returns a greeting message for the chatbot."""
    return "Hi! Welcome to the TravelBot. How can I help you today?\n" \
           "1. Queries\n" \
           "2. Complaint\n" \
           "3. Escalate Technical Issue"


def handle_queries():
    """Presents common travel queries and returns the answer based on selection."""
    for i, query in enumerate(common_queries):
        print(f"{i+1}. {query}")
    choice = input("Enter the number of your query (or 'q' to quit): ")
    if choice.lower() == 'q':
        return "Have a nice day!"
    try:
        choice = int(choice ) -1
        if 0 <= choice < len(df):
            answer = df.iloc[choice, 1]
            return answer
        else:
            return "Invalid choice. Please try again."
    except ValueError:
        return "Invalid input. Please enter a number."

""" def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string()) """

def handle_complaint():
    
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    complaint = input("Describe your complaint: ")
    numbers = list(range(100000000, 10000000))
    reference_number =  random.choice(numbers)
    print(f"Complaint received. Your reference number is Comp-{reference_number}.")
    # Send complaint data (name, email, complaint) with reference number to back office (implement logic here)
    """ subject = f"Comp-{reference_number}"
    body = complaint
    sender = "T.chatbot@gmail.com"
    recipients = ["travelmania.backoffice@gmail.com" ]
    password = "Travel@161446"
    send_email(subject, body, sender, recipients, password)"""
    return f"Thank you, {name}. We'll look into your complaint (Comp-{reference_number}) shortly." 


def handle_technical_issue():

    
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    description = input("Describe the technical issue: ")
    numbers1 = list(range(100000000, 10000000))
    reference_number = random.choice(numbers1)
    print(f"Technical issue received. Your reference number is Tech-{reference_number}.")
    # Send technical issue data (name, email, description) with reference number to back office
    """  subject = f"Tech-{reference_number}"
    body = description
    sender = "T.chatbot@gmail.com"
    recipients = ["travelmania.backoffice@gmail.com" ]
    password = "Travel@161446"
    send_email(subject, body, sender, recipients, password) """
    return f"Thank you, {name}. We'll investigate the issue (Tech-{reference_number}) shortly."



    
@app.route('/greeting', methods=['GET'])
def greeting():
    return jsonify({'response': get_greeting()})

@app.route('/queries', methods=['POST'])
def queries():
    choice = request.json['choice']
    response = handle_queries(choice)
    return jsonify({'response': response})

@app.route('/complaint', methods=['POST'])
def complaint():
    data = request.json
    response = handle_complaint(data)
    return jsonify({'response': response})

@app.route('/technical_issue', methods=['POST'])
def technical_issue():
    data = request.json
    response = handle_technical_issue(data)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)