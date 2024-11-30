from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Gmail credentials
GMAIL_EMAIL = "myaesender@gmail.com"
GMAIL_PASSWORD = "cfsm uhmn edru tqvl"  # Use an app password if 2FA is enabled
GMAIL_SMTP_SERVER = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587

# Function to send an email
def send_email(recipient, subject, body):
    try:
        with smtplib.SMTP(GMAIL_SMTP_SERVER, GMAIL_SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(GMAIL_EMAIL, GMAIL_PASSWORD)

            # Create the email
            msg = MIMEMultipart()
            msg["From"] = GMAIL_EMAIL
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            server.sendmail(GMAIL_EMAIL, recipient, msg.as_string())
            print(f"Email sent to {recipient} with subject: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Flask routes for the front-end
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_test_email', methods=['POST'])
def send_test_email():
    recipient = request.form['recipient']
    subject = request.form['subject']
    body = request.form['body']
    send_email(recipient, subject, body)
    return jsonify({"status": f"Email sent to {recipient}!"})

if __name__ == '__main__':
    app.run(debug=True)