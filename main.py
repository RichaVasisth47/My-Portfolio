import os
from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# .env file se variables load karne ke liye
load_dotenv()

app = Flask(__name__)
# Environment variable se secret key uthayega
app.secret_key = os.environ.get('SECRET_KEY')

# Environment variables se email credentials uthayega
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        msg = EmailMessage()
        msg['Subject'] = f"New Contact Form Submission from {name}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg.set_content(f"Name: {name}\nEmail: {email}\nMessage:\n{message}")

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            flash(f"Error sending message: {e}", "danger")

        return redirect(url_for('contact'))

    return render_template("contact.html")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)