# 🌐 Professional Portfolio Website

A modern, responsive multi-page personal portfolio website built with **Python (Flask)** and **Bootstrap 5**. It features a custom aesthetic, dynamic routing, and a fully functional secure contact form.

---

## ✨ Features

* **Multi-Page Layout:** Includes Home, About, and Contact pages with a unified navigation bar.
* **Custom Aesthetic:** Designed with a custom theme using modern CSS.
* **Interactive Contact Form:** Allows visitors to send direct messages, utilizing server-side validation and feedback via Flask `flash` messages.
* **Secure Email Integration:** Uses Python's built-in `smtplib` and environment variables (`python-dotenv`) to safely handle email submissions.
* **Responsive Design:** Fully optimized for both desktop and mobile screens using Bootstrap components.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons
* **Email Handling:** Python `smtplib`, `email.message`
* **Security:** `python-dotenv` for environment variable management

---

## 🚀 Setup & Installation Locally

Follow these steps to run the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aapka-username/portfolio-website.git](https://github.com/aapka-username/portfolio-website.git)
   cd portfolio-website

Create and activate a virtual environment:
Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:
Bash
pip install flask python-dotenv

⚙️ Configuration (Important for Running Contact Form)
This project uses environment variables to keep sensitive data secure. Because the .env file is ignored by Git, you must create your own .env file to make the contact form work.

Create a file named .env in the root directory of the project.

Add your own Gmail credentials and a secret key in the following format:

Code snippet
SECRET_KEY=your_flask_secret_key_here
EMAIL_ADDRESS=your_personal_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password_here
Note for Gmail Users: Do not use your regular Gmail account password. Instead, generate an App Password from your Google Account security settings (under 2-Step Verification) and use that in the EMAIL_PASSWORD field.

▶️ Running the Application
After setting up your .env file, run the application using:
Bash
python main.py
Open your browser and navigate to http://127.0.0.1:5000/.

🔒 Security Practices
Sensitive credentials (such as email passwords and secret keys) are managed securely using .env and are strictly excluded from version control via .gitignore to protect user data.
